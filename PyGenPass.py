import random
import string

# ========================================
# ERROR MESSAGES - You can customize them
# ========================================
ERROR_MESSAGES = {
    'invalid_number': "Error: Please enter a valid number",
    'min_number': "Error: Please enter a number greater than or equal to {min}",
    'yes_no_error': "Error: Please enter 'yes' or 'no'",
    'no_character': "Error: You must select at least one character type!"
}

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*"
    
    return ''.join(random.choice(characters) for _ in range(length))

def get_yes_no(question):
    while True:
        answer = input(question).strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        print(ERROR_MESSAGES['yes_no_error'])

def get_number(question, minimum=1):
    while True:
        try:
            number = int(input(question))
            if number >= minimum:
                return number
            print(ERROR_MESSAGES['min_number'].format(min=minimum))
        except:
            print(ERROR_MESSAGES['invalid_number'])

print("=" * 40)
print("Strong Password Generator")
print("=" * 40)

num_passwords = get_number("\nHow many passwords do you want to be made? ")
min_length = get_number("Minimum password length (at least 6): ", 6)
max_length = get_number(f"Maximum password length (at least {min_length}): ", min_length)

while True:
    print("\nCharacter types:")
    use_lowercase = get_yes_no("Include lowercase letters (a-z)? (yes/no): ")
    use_uppercase = get_yes_no("Include uppercase letters (A-Z)? (yes/no): ")
    use_digits = get_yes_no("Include digits (0-9)? (yes/no): ")
    use_symbols = get_yes_no("Include symbols (!@#$%^&*)? (yes/no): ")
    
    if use_lowercase or use_uppercase or use_digits or use_symbols:
        break
    print(ERROR_MESSAGES['no_character'])

print("\n" + "=" * 40)
print("Generated Passwords:")
print("=" * 40)


passwords = []

for i in range(num_passwords):
    length = random.randint(min_length, max_length)
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    print(f"{i + 1}. {password} (length: {length})")
    passwords.append(password)


open('passwords.txt', 'a').write('\n'.join(passwords))

print("=" * 40)
print("✅ File saved: passwords.txt")
print("=" * 40)