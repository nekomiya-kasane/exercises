'''
  Practical Test 4

  testAccounts.py - program to test functions of accounts.py
  
  Student Name   :
  Student Number :
  Date/prac time :
'''
from accounts import *

print('\n<--- Bank Accounts Portfolio --->\n')
myAccounts = Portfolio()

myAccounts.addAccount("Castle", "999999-1", 1000)
myAccounts.addAccount("Shrubbery", "999999-2", 100)
myAccounts.addAccount("Grall", "999999-3", 100)

myAccounts.balances()

myAccounts.deposit("Castle", 100)
try:
  myAccounts.withdraw("Shrubbery", 10)
except InsufficientFundsError as e:
  print(" **** Exception: ", e)
try:
  myAccounts.withdraw("Shrubbery", 1000)
except InsufficientFundsError as e:
  print(" **** Exception: ", e)

myAccounts.balances()

try:
  myAccounts.withdraw("Grall", 1000)
except InsufficientFundsError as e:
  print("Insufficient funds for Grall. Balance remains unchanged.")
print(f"Number of accounts: {myAccounts.getNumAccounts()}")
print(f"Total balance: {myAccounts.getTotalBalance()}")

# add code for tasks here

#e.g.
#myAccounts.addAccount("Everyday", "1111-007", 1000)
#myAccounts.deposit("Everyday",200)
