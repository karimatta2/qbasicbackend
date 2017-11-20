
# Submitted by BFK Inc. for CISC 327
# Karim Atta
# Fangt Xu
# Brandon White
# Dean Wilkins-Reeves
# November 2017
# This is a python file to test qbasicbackend.py


#to test this shit just call backend() with the parameters that you have for your test case
#so that each test case is one call on backend
#so if i was testing where transactionList was ["NEW 1234567 000 0000000 Name"] and 
#masterAccount = [""] then i would call backend(["NEW 1234567 000 0000000 Name"], [""])

from qbasicbackend import backend
# Creation Transactions Testing
#   T1:
backend(["DEL 1234567 000 0000000 Name"], ["1234567 999 Name"])
#   T2:
backend(["NEW 1234567 000 0000000 Name"],[""])


'''
#Withdraw Transactions Testing
backend(["WDR 0000000 1000 1010101 ***"], ["1010102 5000 ***
1010101 5000 ***"])

backend(["DEP 1010101 1000 0000000 ***"], ["1010102 5000 ***
1010101 5000 ***"])

backend(["XFR 1010101 1000 1010102 ***"], ["1010103 5000 ***
1010101 5000 ***
1010102 5000 ***"])
'''
