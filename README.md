# my_currency_converter

This project consists of three randomly named python files:pro.py,protest.py and proapp.py.
Pro.py is a module and consists entirely of functions like currency_response which accepts the currency to be converted from,
the currency to convert to and the amount to be converted.

When given these inputs, currency_response retrieves data from a static currency conversion site as a JSON string using 
the introcs python module only used in the Cornell University intro to programming class.

With the knowledge of string manipulation, the relevant parts of the JSON, like the result of the conversion, amount converted,
and the currencies involved in the extraction are obtained with the use of functions like get_to,get_from,before_space and
after_space.

The protest.py is made of well-thought out test cases for functions in the pro.py. 
When run, the script, protest.py, prints out, "Module pro passed all tests".

Proapp.py is a script run from the command-line. It accepts input from the user for a transaction, and prints out 
how much cash is expected to be received. proapp.py can be thought of as the interface of ATM machines at banks etc.
