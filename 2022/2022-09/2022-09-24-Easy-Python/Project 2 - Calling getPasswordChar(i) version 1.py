import random as r
# import module random and name as r
# Available modules available to be called include:
#
# random.randint(a, b):  Returns a random integer N such that
#                        a <= N and N <= b.
#
# random():  returns a float between 0 and 1.
#
# choice(listName):  which returns an item from the list

# --------------------------------------------------------------
# Initialise CONSTANTS
CHAR_S = "!@#$%^&*()"
CHAR_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CHAR_L = "abcdefghijklmnopqrstuvwxyz"
CHAR_N = "0123456789"

# --------------------------------------------------------------
# Initialise variables
s = ""
password = ""
lowNum = 1
highNum = 4

# --------------------------------------------------------------
def getPasswordChar(i):
# --------------------------------------------------------------
# getPasswordChar(i)
#   Input:   i, an integer.
#   Output:  s, a string character .
# --------------------------------------------------------------
#   Purpose:
#      Takes an input integer (i) and tests whether it is one of
#      one of the integers 1, 2, 3, 4. The value of i
#      corresponds with a random character chosen from:
#         1. the set of Special characters.
#         2. the set of Uppercase characters.
#         3. the set of Lowercase characters.
#         4. the set of Numeric characters.
#      
#      Then a random value from the corresponding character set
#      is chosen is assigned to the variable s. If an integer
#      other than (1, 2, 3, 4) is received the value of value of
#      "." (not including the "") is assigned to the variable s.
#      
# --------------------------------------------------------------
  if i == 1:
    # List of Special characters
    characterList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    # Randomly choose one of the Special characters
    s = r.choice(characterList)

  elif i ==2:
    # List of Uppercase characters
    characterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    # Randomly choose one of the Uppercase characters
    s = r.choice(characterList)
    
  elif i ==3:
    # List of Lowercase characters
    characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # Randomly choose one of the Lowercase characters
    s = r.choice(characterList)
    
  elif i ==4:
    # List of Numeric characters
    characterList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # Randomly choose one of the Numeric characters
    s = r.choice(characterList)

  else:
    s = "."

  return s

# --------------------------------------------------------------
#### #### #### #### #### #### MAIN #### #### #### #### #### #### 
# --------------------------------------------------------------
print("===============================")
print("Terry's Secure Password Creator")
print("===============================")
print()
print("  Characters sets available:")
print("  --------------------------")
print("    Special characters:  ", CHAR_S)
print("    Uppercase characters:", CHAR_U)
print("    Lowercase characters:", CHAR_L)
print("    Numeric characters:  ", CHAR_N)
print()
# pLength is assigned a random integer between 1 and 40
# inclusively. That means the smallest value that is returned
# is 1 & the largest returned is 40. 
print("  Setting the password length:")
print("  --------------------------")
print("    Setting password length by calling a random number")
print("    between (and including) the numbers of 1 and 40:")
print()
print("      pLength = r.randint(1, 40)")
print()
pLength = r.randint(1, 40)

print("    The value of pLength is:", pLength)
print()
print("      (Remember, password length will change each time")
print("       you run this program)")
print()

# Looping from 0 .. 6 and sending the value of count to
# getPasswordChar and receiving a random character per the module.
print("  Running a quick loop (0...6) calling getPasswordChar")
print("  ----------------------------------------------------")
#print("  The values: 0, and 5 return the character: .")
#print("              1: Special,   2: Uppercase,")
#print("              3: Lowercase, 4: Numbers.")
#print()
for count in range(6):
  passwordChar = getPasswordChar(count)
  print("    The value of:", count, "receives the char -> ", passwordChar)
  print("      passwordChar = getPasswordChar(" + str(count) + ")")
  print("      passwordChar = " + passwordChar)
  print()

# (Using variables) Initialise lowNum and highNum for getting a
# random number instead of hardcoded numbers. The variables lowNum
# and highNum were initialised in lines 23, and 24.
print("  Building the password line by line")
print("  ----------------------------------")
print("     +--------> f - the value that increments in the line:")
print("     |            for f in range(pLength)")
print("     |")
print("     | +------> charSet - the value of charSet that is returned in the line:")
print("     | |          charSet = r.randint(lowNum, highNum)")
print("     | |")
print("     | | +----> passwordChar - the value of passwordChar that is returned in the line:")
print("     | | |        passwordChar = getPasswordChar(charSet)")
print("     | | |")
print("     | | | +--> password - the value of password that is returned in the line:")
print("     | | | |      password = password + passwordChar")
for f in range(pLength):
  charSet = r.randint(lowNum, highNum)
  passwordChar = getPasswordChar(charSet)
  password = password + passwordChar
  print("    " + str(f + 1).zfill(2), charSet, passwordChar, password)

print()
print("  The password details")
print("  --------------------")
print("    Password length:", pLength)
print("    Password:", password)
print()
print("+-----------------------------------------+")
print("| Terry thanks you for all your hard work |")
print("+-----------------------------------------+")