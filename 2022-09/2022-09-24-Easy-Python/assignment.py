import random as r

# --------------------------------------------------------------
# ---GIVEN METHOD-----------------------------------------------
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

# My codes

SPECIAL, UPPER, LOWER, NUMERIC = 0x1, 0x2, 0x4, 0x8
choices_map = { SPECIAL: 1, UPPER: 2, LOWER: 3, NUMERIC: 4 }

choices_names = { 
    SPECIAL: "Special",
    UPPER: "Uppercase",
    LOWER: "Lowercase",
    NUMERIC: "Numerical",
}

def get_passwd_charsets():
    HEADER = '''
    
        Special Charactors  : !@#$%^&*()
        Uppercase Charactors: ABCDEFGHIJKLMNOPQRSTUVWXYZ 
        Lowercase Charactors: abcdefghijklmnopqrstuvwxyz
        Numerical Charactors: 0123456789

    '''

    # print header
    print(HEADER)

    # get charactor catagories
    res = 0
    while not res:
        res = 0
        for k, v in choices_names.items():
            if input("Do you want include {} charactors? [Y/N] ".format(v.lower())).upper() == 'Y':
                res |= k
        print("")
        if not res:
            print("Error: You must choose at least one character set. \n")
    return list(filter(lambda x: res & x, [SPECIAL, UPPER, LOWER, NUMERIC]))

def get_passwd_length() -> int:
    # get password length
    length = 0
    while True:
        try:
            length = int(input("Please input the length of password you want to create [1~40]: "))
            print("")
            if length >= 1 and length <= 40:
                break
        except:
            pass
        print("Error: length should be between 1 and 40 (included).\n")
    return length

def create_passwd(charsets, length):
    # create password
    
    res = ''.join([getPasswordChar(choices_map[c]) for c in r.choices(charsets, k=length)])  # type: ignore
    return res

if __name__ == '__main__':
    while True:
        if input("Input S/D/G/P/X (case in sensitive) to start.").upper() in "SDGPX":
            break

    choices = get_passwd_charsets()
    length = get_passwd_length()
    res = create_passwd(choices, length)

    sets = list(map(lambda x: choices_names[x], choices))

    print("Requested password length: {}".format(str(length)))
    print("Requested charactor sets: {}".format(', '.join(sets) + " Characters"))
    print("--------------------------------------------------------------------")
    print("Generated Password: {}".format(res))