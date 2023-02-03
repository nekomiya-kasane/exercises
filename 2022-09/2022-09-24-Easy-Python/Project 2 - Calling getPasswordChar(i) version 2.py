import random as r

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
#   Output:  s, a string character.
# --------------------------------------------------------------
#   Purpose:
#   Takes an input integer (i) and tests whether it is one of
#   the integers 1, 2, 3, 4. The value of i corresponds with a
#   random character chosen from: (1) Special, (2) Uppercase
#   (3) Lowercase, & (4) Numeric characters. Then a random value
#   from the corresponding character set is chosen is assigned
#   to the variable s. If an integer other than (1, 2, 3, 4) is
#   received the value of value of "." (not including the "")
#   is assigned to the variable s.
# --------------------------------------------------------------
  if i == 1:
    # List of Special characters
    characterList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
    s = r.choice(characterList)

  elif i ==2:
    # List of Uppercase characters
    characterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    s = r.choice(characterList)
    
  elif i ==3:
    # List of Lowercase characters
    characterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    s = r.choice(characterList)
    
  elif i ==4:
    # List of Numeric characters
    characterList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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
pLength = r.randint(1, 40)

print("  Running a quick loop (0...6) calling getPasswordChar")
print("  ----------------------------------------------------")
for count in range(6):
  passwordChar = getPasswordChar(count)
  print("    The value of:", count, "receives the char -> ", passwordChar)

print()
print("  Generating the password")
print("  -----------------------")
for f in range(pLength):
  charSet = r.randint(lowNum, highNum)
  passwordChar = getPasswordChar(charSet)
  password = password + passwordChar

print("    Password length:", pLength)
print("    Password:",        password)
print()
print("+-----------------------------------------+")
print("| Terry thanks you for all your hard work |")
print("+-----------------------------------------+")