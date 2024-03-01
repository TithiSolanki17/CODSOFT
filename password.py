import random
import string

def password(length, numbers, special_char):
    alpha = string.ascii_letters
    num = string.digits
    schar = string.punctuation

    char = alpha
    if numbers:
        char += num
    if special_char:
        char += schar
    
    passw = ""
    while len(passw) < length - 2:
        new_char = random.choice(char)
        passw += new_char

    if numbers:
        passw += random.choice(num)

    if special_char:
        passw += random.choice(schar)

    while(len(passw) < length):
        passw += random.choice(char)

    return passw

print("<RANDOM PASSWORD GENERATOR>")
n = int(input("Enter the length of your password:"))
number = input("Do you want numbers? (y/n): ").lower() == "y"
schar = input("Do you want special characters? (y/n): ").lower() == "y"
password = password(n, number, schar)
print("Your random Generated Password : ",password)
password = ""