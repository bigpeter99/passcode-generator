import string
from random import choice

def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meet_criteria = False
    has_number = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters:
            meet_criteria = meet_criteria and has_special


    return pwd
    
minimum_length = int(input("Enter the minimum length: "))
has_number = str(input("Do you want to have numbers? [Y/n]: ")).lower() == 'y'
has_special = str(input("Do you want it to have special characters? [Y/n]: ")).lower() == 'y'
pwd = generate_password(minimum_length, has_number, has_special)
print(f"The generated passcode is {pwd}")
