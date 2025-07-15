#password generator

import random
import string

def generate_password(length, use_digits, use_symbols, use_uppercase):
    characters = string.ascii_lowercase  # base: lowercase letters

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character types selected."

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# ---- Main Program ----
try:
    length = int(input("Enter password length: "))

    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols (e.g., !@#)? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    result = generate_password(length, use_digits, use_symbols, use_uppercase)
    print("Generated password:", result)

except ValueError:
    print("Please enter a valid number for password length.")
