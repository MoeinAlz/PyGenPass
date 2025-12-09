# 🔐 Strong Password Generator

A simple yet powerful Python program to generate secure random passwords with customizable options.

## 📋 Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Customization](#customization)
- [Example Output](#example-output)
- [File Structure](#file-structure)
- [Author](#author)

---

## ✨ Features

- ✅ Generate multiple passwords at once
- ✅ Customize password length (min and max)
- ✅ Choose character types:
  - Lowercase letters (a-z)
  - Uppercase letters (A-Z)
  - Digits (0-9)
  - Special symbols (!@#$%^&*)
- ✅ Automatic validation of user input
- ✅ Save passwords to a text file
- ✅ Customizable error messages
- ✅ Simple and clean interface

---

## 🔧 Requirements

- Python 3.6 or higher
- No external libraries required (uses built-in `random` and `string` modules)

---

## 📥 Installation

1. **Download the file:**
   ```bash
   # Clone or download the repository
   git clone <your-repo-url>
   ```

2. **Navigate to the directory:**
   ```bash
   cd password-generator
   ```

3. **Run the program:**
   ```bash
   python password_generator_english.py
   ```

---

## 🚀 Usage

1. **Run the program:**
   ```bash
   python password_generator_english.py
   ```

2. **Answer the questions:**
   - How many passwords do you want?
   - Minimum password length
   - Maximum password length
   - Which character types to include (yes/no)

3. **Get your passwords:**
   - Passwords are displayed on screen
   - Passwords are saved to `passwords.txt`

---

## 🔍 How It Works

### 1. **Import Libraries**
```python
import random  # For random selection
import string  # For character sets (a-z, A-Z, 0-9)
```

### 2. **Define Error Messages**
```python
ERROR_MESSAGES = {
    'invalid_number': "Error: Please enter a valid number",
    # ... more messages
}
```
- All error messages are stored in one dictionary
- Easy to customize in one place

### 3. **Generate Password Function**
```python
def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    characters = ""
    # Add selected character types
    # Generate random password
    return ''.join(random.choice(characters) for _ in range(length))
```

### 4. **Input Validation Functions**
- `get_yes_no()`: Validates yes/no responses
- `get_number()`: Validates numeric input with minimum value

### 5. **Main Program Flow**
1. Get user preferences
2. Generate passwords
3. Display passwords
4. Save to file

---

## 🎨 Customization

### Change Error Messages
Edit the `ERROR_MESSAGES` dictionary at the top of the file:

```python
ERROR_MESSAGES = {
    'invalid_number': "Oops! That's not a number!",
    'min_number': "Number must be at least {min}",
    'yes_no_error': "Please type 'yes' or 'no'",
    'no_character': "Choose at least one character type!"
}
```

### Add More Symbols
Modify line 23:
```python
characters += "!@#$%^&*()_+-=[]{}|;:,.<>?"  # Add more symbols
```

### Change File Name
Modify line 77:
```python
open('my_passwords.txt', 'w').write('\n'.join(passwords))
```

---

## 📝 Example Output

### Console Output:
```
========================================
Strong Password Generator
========================================

How many passwords do you want? 3
Minimum password length (at least 6): 8
Maximum password length (at least 8): 12

Character types:
Include lowercase letters (a-z)? (yes/no): yes
Include uppercase letters (A-Z)? (yes/no): yes
Include digits (0-9)? (yes/no): yes
Include symbols (!@#$%^&*)? (yes/no): yes

========================================
Generated Passwords:
========================================
1. aB3$xK9p (length: 8)
2. qR7@mN2sT (length: 9)
3. wT5!zY8dX1 (length: 10)
========================================
✅ File saved: passwords.txt
========================================
```

### File Output (passwords.txt):
```
aB3$xK9p
qR7@mN2sT
wT5!zY8dX1
```

---

## 📂 File Structure

```
password-generator/
│
├── password_generator_english.py   # Main program (English version)
├── password_generator_simple.py    # Main program (Persian version)
├── passwords.txt                   # Generated passwords (auto-created)
└── README.md                       # This file
```

---

## 🧠 Key Concepts Used

### Functions
- `generate_password()`: Creates random passwords
- `get_yes_no()`: Validates yes/no input
- `get_number()`: Validates numeric input

### Methods
- `.strip()`: Remove extra spaces
- `.lower()`: Convert to lowercase
- `.append()`: Add item to list
- `.join()`: Combine list into string
- `.format()`: Insert values into string

### Control Flow
- `if/elif/else`: Conditional statements
- `while True`: Infinite loop (until break)
- `for i in range()`: Loop with counter
- `try/except`: Error handling

### Data Structures
- Dictionary: Store error messages
- List: Store generated passwords
- String: Character sets and passwords

---

## 🎓 Learning Resources

This program demonstrates:
1. **Functions**: Reusable code blocks
2. **Error Handling**: `try/except` blocks
3. **Input Validation**: Checking user input
4. **File Operations**: Writing to text files
5. **String Manipulation**: `join()`, `format()`, etc.
6. **List Operations**: `append()`, iteration
7. **Random Selection**: `random.choice()`, `random.randint()`

---

## 📜 License

This project is open source and available for educational purposes.

---

## 👤 Author

Created as a learning project for understanding:
- Python basics
- Functions and methods
- File handling
- Input validation
- Random password generation

---

## 🤝 Contributing

Feel free to:
- Report bugs
- Suggest improvements
- Add new features
- Translate to other languages

---

## 📞 Support

If you have questions or need help:
1. Check the code comments
2. Review this README
3. Test with different inputs

---

## ⭐ Version History

- **v1.0** (2024): Initial release
  - Basic password generation
  - Character type selection
  - File saving functionality
  - Input validation

---

Made with ❤️ for learning Python programming!