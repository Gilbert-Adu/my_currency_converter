"""
Unit test for module pro

When run as a script, this module invokes several procedures that
test the various functions in the module a1.

Author: Gilbert Adu
Date:   7th February 2019
"""

import pro
import introcs


def testA():
    """
    Tests for part A
    """
#------------tests for before_space---------------------------------------------
    compare1=pro.before_space('678 322')
    introcs.assert_equals(compare1,'678')

    compare2=pro.before_space(' 678322')
    introcs.assert_equals(compare2,'')

    compare3=pro.before_space('     678322')
    introcs.assert_equals(compare3,'')

    compare4=pro.before_space('678322 ')
    introcs.assert_equals(compare4,'678322')

#----------------tests for after_space------------------------------------------
    compare5=pro.after_space('678 322')
    introcs.assert_equals(compare5,'322')

    compare6=pro.after_space(' 678 322')
    introcs.assert_equals(compare6,'678 322')

    compare7=pro.after_space('678322 ')
    introcs.assert_equals('',compare7)

    compare8=pro.after_space('     678322')
    introcs.assert_equals('    678322',compare8)

def testB():
    """
    Tests for part B
    """
#-----------tests for first_inside_quotes---------------------------------------
    compare1=pro.first_inside_quotes('A "B C" D')
    introcs.assert_equals(compare1,'B C')

    compare2=pro.first_inside_quotes('A B "C D" E "F" G ')
    introcs.assert_equals(compare2,'C D')

    compare3=pro.first_inside_quotes('A "" B C D')
    introcs.assert_equals(compare3,'')

    compare4=pro.first_inside_quotes('A B " " C D')
    introcs.assert_equals(compare4,' ')


#----------------tests for get_from---------------------------------------------

    compare5=pro.get_from('{ "valid" : true, "from" : "2 United States Dollars", "to" : "1.727138 Euros", "error" : "" }')
    introcs.assert_equals(compare5,'2 United States Dollars')

    compare6=pro.get_from('{ "valid" : false, "from" : "", "to" : "", "error" : "Source currency code is invalid." }')
    introcs.assert_equals(compare6,'')

    compare8=pro.get_from('{"from" : "2 United States Dollars","valid" : true,"error" : "","to" : "1.727138 Euros"}')
    introcs.assert_equals(compare8,'2 United States Dollars')

    compare9=pro.get_from('{ "valid" : true, "from":"2 United States Dollars", "to" : "1.727138 Euros", "error" : "" }')
    introcs.assert_equals(compare9,'2 United States Dollars')

#--------------------tests for get_to-------------------------------------------
    value1=pro.get_to('{ "valid" : true, "from" : "2 United States Dollars", "to" : "1.727138 Euros", "error" : "" }')
    introcs.assert_equals(value1,'1.727138 Euros')

    value2=pro.get_to('{ "valid" : false, "from" : "", "to" : "", "error" : "Source currency code is invalid." }')
    introcs.assert_equals(value2,'')

    value3=pro.get_to('{"from" : "2 United States Dollars","valid" : true,"error" : "","to" : "1.727138 Euros"}')
    introcs.assert_equals(value3,'1.727138 Euros')

    value4=pro.get_to('{ "valid" : true, "from":"2 United States Dollars", "to"     :       "1.727138 Euros", "error" : "" }')
    introcs.assert_equals(value4,'1.727138 Euros')


#-------------------tests for has_error-----------------------------------------

    value5=pro.has_error('{ "valid" : true, "from" : "2 United States Dollars", "to" : "1.727138 Euros", "error" : "" }')
    introcs.assert_equals(value5,False)

    value6=pro.has_error('{ "valid" : false, "from" : "", "to" : "", "error" : "Source currency code is invalid." }')
    introcs.assert_equals(value6,True)

    value7=pro.has_error('{"from" : "2 United States Dollars","valid" : true,"error" : "","to" : "1.727138 Euros"}')
    introcs.assert_equals(value7,False)

    value8=pro.has_error('{ "valid" : false, "from" : "", "to" : "", "error" : "Exchange currency code is invalid." }')
    introcs.assert_equals(True,value8)

    value9=pro.has_error('{ "valid" : false, "from" : "", "to" : "", "error" : "Currency amount is invalid." }')
    introcs.assert_equals(value9,True)


def testC():
    """
    Test for part C
    """

#----------------tests for currency_response------------------------------------
    compare1=pro.currency_response('USD','EUR',770)
    introcs.assert_equals(compare1,'{ "valid" : true, "from" : "770 United States Dollars", "to" : "670.89253 Euros", "error" : "" }')

    compare2=pro.currency_response('USD','EUR',-95)
    introcs.assert_equals(compare2,'{ "valid" : true, "from" : "-95 United States Dollars", "to" : "-82.772455 Euros", "error" : "" }')

    compare3=pro.currency_response('GHS','CAD',200)
    introcs.assert_equals(compare3,'{ "valid" : true, "from" : "200 Ghanaian Cedis", "to" : "52.824859437751 Canadian Dollars", "error" : "" }')

    compare4=pro.currency_response('CAD','GHS',3.35)
    introcs.assert_equals(compare4,'{ "valid" : true, "from" : "3.35 Canadian Dollars", "to" : "12.683422296457 Ghanaian Cedis", "error" : "" }')


def testD():
    """
    Test for part D
    """
#-----------tests for iscurrency------------------------------------------------
    value1=pro.iscurrency('USD')
    introcs.assert_true(value1)

    value2=pro.iscurrency('GHS')
    introcs.assert_true(value2)

    value3=pro.iscurrency('EUR')
    introcs.assert_true(value3)

    value4=pro.iscurrency('CAD')
    introcs.assert_true(value4)

#--------------------tests for exchange-----------------------------------------

    compare1=pro.exchange('USD','GHS',256.84)
    introcs.assert_floats_equal(compare1,1279.0632)

    compare2=pro.exchange('EUR','CAD',-0.96)
    introcs.assert_floats_equal(compare2,-1.4492613128365)

    compare3=pro.exchange('CAD','GHS',1200.01)
    introcs.assert_floats_equal(compare3,4543.3533104394)

    compare4=pro.exchange('EUR','USD',780.98)
    introcs.assert_floats_equal(compare4,896.35012033895)







testA()
testB()
testC()
testD()
print('Module pro passed all tests')
