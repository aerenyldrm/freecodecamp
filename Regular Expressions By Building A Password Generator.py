import re
import secrets
import string
def generatePassword(length=11, number_count=1, special_character_count=1, uppercase_count=1, lowercase_count=1):
    letter_pool = string.ascii_letters
    digit_pool = string.digits
    symbol_pool = string.punctuation
    # above is to define probable caharacter for password
    entire_character_probability = letter_pool + digit_pool + symbol_pool
    # above is to combine entire character
    while True:
        password = ""
        for count in range(length):
            password += secrets.choice(entire_character_probability)
            # above is to generate password
        constraint_pool = [
            (number_count, r'\d'),
            (special_character_count, fr'[{symbol_pool}]'),
            (uppercase_count, r'[A-Z]'),
            (lowercase_count, r'[a-z]')
        ]
        number = 0
        if all(
            constraint <= len(re.findall(pattern, password)) for constraint, pattern in constraint_pool
        ):
            break
        else: pass
        # above is to check constraint pool
    return password
print(generatePassword(length=7, number_count=1, special_character_count=1, uppercase_count=1, lowercase_count=1))