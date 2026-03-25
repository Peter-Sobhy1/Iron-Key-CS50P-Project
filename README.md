# 🔑 Iron Key — Password Generator & Analyzer



## 📝Description

A command-line password manager built in Python for CS50P's final project.
Iron Key lets you generate strong random passwords, analyze the strength of existing ones, and optionally save them to a file.

---
## URL
🎬 https://youtu.be/XwMjWvmA_qs

---
## 💡Features

- Generate a random password of any length using letters, numbers, and symbols
- Analyze the strength of any password and rate it as **Strong**, **Intermediate**, or **Weak**
- Save generated passwords to a file with the name of the app or website they belong to
- Supports custom file paths for saving passwords
- Input validation with clear error messages

---

## 🛠️Tools & Technologies

- Python 3.10+
- VS Code

---

## How to Run

```bash
python project.py
```

You will be greeted with the Iron Key welcome screen and prompted to choose between two modes.

---

## Usage

### Mode 1 — Generate a Password

1. Choose `1` when prompted
2. Enter the desired password length (minimum 4)
3. Iron Key generates a random password and rates its strength
4. Choose whether to save the password to a file
5. If saving, enter the app or website name the password belongs to
6. Choose the default save path or enter a custom file path

### Mode 2 — Analyze a Password

1. Choose `2` when prompted
2. Enter any existing password
3. Iron Key rates its strength as **Strong**, **Intermediate**, or **Weak**

---

## Strength Rating System

| Criteria | Points |
|---|---|
| Length is greater than or equal to 12 characters | +1 |
| Mix of uppercase and lowercase | +1 |
| Contains at least one digit | +1 |
| Contains at least one special character | +1 |


| Score | Rating |
|---|---|
| 4 | Strong |
| 2–3 | Intermediate |
| 0–1 | Weak |

---

## 🧱Project Structure

```
project.py          # Main application
test_project.py     # Pytest test suite
README.md           # This file
```

---
## Imported Libraries
### String & Random
```python
import random
import string as s
```

## 🦾 Functions

### `generate_password(length)`
Generates a random password of the given length using all ASCII letters, digits, and punctuation characters.

```python
def generate_password(length):
    """Generates a random password using letters, numbers, and symbols."""
    characters = s.ascii_letters + s.digits + s.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
```

### `evaluate_strength(password)`
Evaluates the strength of a given password based on length, character variety, digits, and special characters. Returns `"Strong"`, `"Intermediate"`, or `"Weak"`.

```python
def evaluate_strength(password):
    """Evaluates the strength of the password based on a few basic rules."""
    score = 0
    if len(password) >= 12:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in s.punctuation for c in password):
        score += 1

    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Intermediate"
    else:
        return "Weak"
```

### `save_to_file(password, app, filename="my_passwords.txt")`
Appends the password and its associated app name to a text file. Defaults to `my_passwords.txt` but accepts a custom file path.

```python
def save_to_file(password, app, filename="my_passwords.txt"):
    """Appends the generated password to a local text file."""
    line = f"{app}: {password}"
    with open(filename, "a") as file:
        file.write(line + "\n")
    print(f"Success! Password securely saved to {filename}.")
```

### `main()`
Controls the full application flow — displays the welcome message, handles user input, and calls the appropriate functions based on the user's choice.

```python
def main():
    """The function of the application."""
    print("--- Welcome to Iron Key the Password Generator & Analyzer ---")
    choice = input('Choose "1" to Generate Password\nChoose "2" to Analyze Password:\n')
    try:
        if choice == "1":
            user_input = input("How long do you want your password to be? (For Example: 16): ")
            length = int(user_input)
            if length < 4:
                print("For security, please choose a length of at least 4.")
                return
            new_password = generate_password(length)
            print(f"\nYour new password is: {new_password}")
            strength = evaluate_strength(new_password)
            print(f"Password Strength Rating: {strength}")
            save_choice = input("\nWould you like to save this password to a file? (y/n): ").strip().lower()
            if save_choice == 'y':
                app = input("This Password is for which APP/Website? ").strip()
                file_path = input('Choose "1" for Default Path\nor Enter Your File Path: ')
                if file_path == "1":
                    save_to_file(new_password, app)
                else:
                    save_to_file(new_password, app, file_path)
            else:
                print("Password not saved. Make sure to copy it!")
        elif choice == "2":
            print(evaluate_strength(input("Enter Your Password: ")))
        else:
            print('Please Choose "1" or "2"')
    except ValueError:
        print("Error: Please enter a valid whole number for the length.")
```

---

## Security Note

Passwords are saved in **plain text**. This is a learning project and is not intended for production use. For real password management, use a dedicated encrypted password manager.

---

## 🧐Tests

Run the test suite using pytest:

```bash
pytest test_project.py
```

### `test_generate_password()`
Verifies the generated password has the correct length and contains uppercase, lowercase, digits, and special characters.

### `test_evaluate_strength()`
Verifies the strength rating returns `"Strong"`, `"Intermediate"`, and `"Weak"` for known inputs.

### `test_save_to_file()`
Verifies that the password is saved correctly to a file and that the file contains the expected content.

```python
import project as p
import string as s
import os


# Test 1: For generate_password
def test_generate_password():
    pwd = p.generate_password(25)
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_punctuation = any(c in s.punctuation for c in pwd)
    assert len(pwd) == 25
    assert has_upper and has_lower and has_digit and has_punctuation

# Test 2: For evaluate_strength
def test_evaluate_strength():
    assert p.evaluate_strength("Pepo@741@852") == "Strong"
    assert p.evaluate_strength("Pe@741@852") == "Intermediate"
    assert p.evaluate_strength("Pep") == "Weak"

# Test 3: For save_to_file
def test_save_to_file():
    test_file = "test_data.txt"
    p.save_to_file("secret123", "Gmail", filename=test_file)
    assert os.path.exists(test_file)
    with open(test_file, "r") as f:
        assert "Gmail: secret123" in f.read()
    os.remove(test_file)
```

---

## ✍Author

Peter Sobhy — CS50P Final Project 2026
