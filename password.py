import random
import string

def generate(length, numbers=True, special_char=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    character = letters
    if numbers:
        character += digits
    if special_char:
        character += special
    
    password = ""
    criteria = False
    has_num = False
    has_special = False

    while not criteria or len(password) < length:
        new_char = random.choice(character)
        password += new_char

        if new_char in digits:
            has_num = True
        elif new_char in special:
            has_special = True

        criteria = True
        if numbers:
            criteria = has_num
        if special_char:
            criteria = criteria and has_special

    return password

print("<RANDOM PASSWORD GENERATOR>")
n = int(input("Enter the length of your password:"))
has_number = input("Do you want numbers? (y/n)").lower() == "y"
has_special = input("Do you want special characters? (y/n)").lower() == "y"
password = generate(n, has_number, has_special)
print("Your random Generated Password : ",password)
password = ""