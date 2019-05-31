"""
Module for currency exchange

This module provides several string parsing functions to implement a
simple currency exchange routine using an online currency service.
The primary function in this module is exchange.

Author: Gilbert Adu
Date:   7th February 2019
"""


#----------------------PART A---------------------------------------------------
import introcs

def before_space(s):
    """
    Returns: Substring of s; up to, but not including, the first space
    Parameter: s -- the string to slice
    Precondition: s has at least one space in it
    """

    space=s.index(' ')
    substring=s[:space]
    return substring





def after_space(s):
    """
    Returns: Substring of s after the first space
    Parameter: s -- the string to slice
    Precondition: s has at least one space in it
    """
    space=s.index(' ')
    substring=s[space+1:]
    return substring



#---------------PART B----------------------------------------------------------


def first_inside_quotes(s):
    """
    Returns: The first substring of s between two (double) quote characters
    A quote character is one that is inside a string, not one that delimits it.
    We typically use single quotes (') to delimit a string if want to use a double
    quote character (") inside of it.

    Example: If s is 'A "B C" D', this function returns 'B C'
    Example: If s is 'A "B C" D "E F" G', this function still returns 'B C'
    because it only picks the first such substring.
    Parameter: s -- a string to search
    Precondition: s is a string with at least two (double) quote characters inside.
    """

    first_quote=s.index('"')
    second_quote=s.index('"',first_quote+1)
    text=s[first_quote+1:second_quote]
    return text



def get_from(json):
    """
    Returns: The FROM value in the response to a currency query.
    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "from".
     For example, if the JSON is
    '{ "valid" : true, "from" : "2 United States Dollars", "to" : "1.727138
    Euros", "error" : "" }'
    then this function returns '2 United States Dollars' (not '"2 United
    States Dollars"').  It returns the empty string if the JSON is the
    result of an invalid query.
    Parameter: json -- a json string to parse
    Precondition: json is the response to a currency query
    """
    find_from=json.index('from')
    find_colon=json.index(':',find_from+1)
    after_colon=json[find_colon+1:]
    from_value=first_inside_quotes(after_colon)
    return from_value


def get_to(json):
    """
    Returns: The TO value in the response to a currency query.
    Given a JSON response to a currency query, this returns the string inside
    double quotes (") immediately following the keyword "to".
    For example, if the JSON is
    '{ "valid" : true, "from" : "2 United States Dollars", "to" : "1.727138
    Euros", "error" : "" }'
    then this function returns '1.727138 Euros' (not '"1.727138 Euros"').
    It returns the empty string if the JSON is the result of an invalid query.
    Parameter: json -- a json string to parse
    Precondition: json is the response to a currency query
    """
    find_to=json.index('to')
    find_colon=json.index(':',find_to+1)
    after_colon=json[find_colon+1:]
    to_value=first_inside_quotes(after_colon)
    return to_value



def has_error(json):
    """
    Returns: True if the query has an error; False otherwise.
    Given a JSON response to a currency query, this returns the opposite
    of the value following the keyword "valid".  For example, if the JSON is
    '{ "valid" : false, "from" : "", "to" : "", "error" : "Source currency
    code is invalid." }'
    then the query is not valid, so this function returns True
    (It does NOT return the message 'Source currency code is invalid').
    Parameter: json -- a json string to parse
    Precondition: json is the response to a currency query
    """

    find_error=json.index('error')
    find_colon=json.index(':',find_error+1)
    after_colon=json[find_colon+1:]
    error_value=first_inside_quotes(after_colon)
    if len(error_value)==0:
        return False
    else:
        return True


#----------------PART C---------------------------------------------------------


def currency_response(currency_from, currency_to, amount_from):
    """
    Returns: a JSON string that is a response to a currency query.
    A currency query converts amount_from money in currency currency_from
    to the currency currency_to. The response should be a string of the form
    '{ "valid" : true, "from" : "<old-amount>", "to" : "<new-amount>", "error" : "" }'
    where the values old-amount and new-amount contain the value and name for the
    original and new currencies. If the query is invalid, both old-amount and
    new-amount will be empty, while "valid" will be followed by the value false.

    Parameter: currency_from -- the currency on hand (the LHS)
    Precondition: currency_from is a string with no spaces

    Parameter: currency_to -- the currency to convert to (the RHS)
    Precondition: currency_to is a string with no spaces

    Parameter: amount_from -- amount of currency to convert
    Precondition: amount_from is a float
    """

    site='http://cs1110.cs.cornell.edu/2019sp/a1server.php?from='+currency_from+'&to='+currency_to+'&amount='+str(amount_from)
    my_json=introcs.urlread(site)
    return my_json


#---------------PART D----------------------------------------------------------
def iscurrency(currency):
    """
    Returns: True if currency is a valid (3 letter code for a) currency. It returns False otherwise.

    Parameter: currency -- the currency code to verify
    Precondition: currency is a string with no spaces.
    """
    the_json=currency_response(currency,'USD',7000)
    check=has_error(the_json)
    if check:
        return False
    else:
        return True


def exchange(currency_from, currency_to, amount_from):
    """
    Returns: amount of currency received in the given exchange.
    In this exchange, the user is changing amount_from money in currency
    currency_from to the currency currency_to. The value returned represents
    the amount in currency currency_to.
    The value returned has type float.

    Parameter: currency_from -- the currency on hand (the LHS)
    Precondition: currency_from is a string for a valid currency code

    Parameter: currency_to -- the currency to convert to (the RHS)
    Precondition: currency_to is a string for a valid currency code

    Parameter: amount_from -- amount of currency to convert
    Precondition: amount_from is a float
    """
    the_json=currency_response(currency_from,currency_to,amount_from)
    my_json=str(the_json)
    the_to=get_to(my_json)
    actual_value=before_space(the_to)
    return float(actual_value)
