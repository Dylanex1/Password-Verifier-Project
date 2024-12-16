validpasswordlength = 8
capital = False
number = False
special = False
length = False


print("\nWelcome to PasswordTester I need you to try and write a password you think is good enough\n")

s1 = input("Enter the Password:")

if (len(s1) >= 8):
    print("Password has sufficent length")
    length = True 
else:
    print("Password does not have sufficent length")
for i in s1:
    letter = i
    if (ord(letter) >= 65 and ord(letter) <= 90 and capital == False):
        print("Password has at least one capital letter")
        capital = True
    if (ord(letter) >= 48 and ord(letter) <=57 and number == False):
        print("Password has at least one Digit")
        number = True
    if ( (letter == '_' or letter == '@' or letter == '$') and special == False):
        print("Password has at least one special charecter")
        special = True

if length and capital and number and special:
    print("\nThis is a strong passsword!")
else:
    print("\nThis password is not strong enough")