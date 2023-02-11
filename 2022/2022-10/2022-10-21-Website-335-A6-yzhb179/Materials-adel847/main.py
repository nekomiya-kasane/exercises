import hashlib

username = 'Carola'
retrieved_password = "e35bcfc55dcae41a28fe9f19ee117050"


def check_password(word):
    hs = hashlib.md5((username + ":" + word).encode()).hexdigest()
    # print(username + ":" + word)
    return hs[:32] == retrieved_password

def scan(filename):
    file = open(filename, "r", encoding='utf-8')
    for line in file:
        line_list = line.split('  ')
        if len(line_list) < 2:
            continue
        word = line_list[0].strip()

        if check_password(word):
            print(word)
        if check_password(word.lower()):
            print(word.lower())


scan(R"C:\dict.txt")
print("finished.")

