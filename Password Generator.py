import string
import random


def generate_password(plen):
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    
    s= []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    
    random.shuffle(s)
    password = "".join(s[0:plen])
    return password

while True:
    try:
        plen = int(input("Enter the Length of the Password (8 or more reccommended ):"))
        if plen < 8:
            print("Password length should be 8 or more characters.")
            continue
        password = generate_password(plen)
        print("Your password is :",password)
        break
        
    except ValueError:
        print("Please Enter the valid integer for Password length")
      
            