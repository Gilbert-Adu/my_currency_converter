"""
User interface for module currency

When run as a script, this module prompts the user for two currencies and amount.
It prints out the result of converting the first currency to the second.

Author: Gilbert Adu
Date:   7th February 2019
"""

import pro

currency_from=input('3-letter code for original currency: ')
currency_to=input('3-letter code for the new currency: ')
amount_from=input('Amount of the original currency: ')
result=pro.exchange(currency_from,currency_to,float(amount_from))

print('You can exchange '+ amount_from+' '+  currency_from +' for '+ str(result)+ ' '+currency_to+'.')
