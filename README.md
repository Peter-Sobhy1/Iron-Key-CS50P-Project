# 🔑 Iron Key — Password Generator & Analyzer

A command-line password manager built in Python for CS50P's final project.
Iron Key lets you generate strong random passwords, analyze the strength of existing ones, and optionally save them to a file.

---

## Features

- Generate a random password of any length using letters, numbers, and symbols
- Analyze the strength of any password and rate it as **Strong**, **Moderate**, or **Weak**
- Save generated passwords to a file with the name of the app or website they belong to
- Supports custom file paths for saving passwords
- Input validation with clear error messages

---

## Requirements

- Python 3.10+
- No external libraries required

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
3. Iron Key rates its strength as **Strong**, **Moderate**, or **Weak**

---

## Strength Rating System

| Criteria | Points |
|---|---|
| Length >= 12 characters | +1 |
| Mix of uppercase and lowercase | +1 |
| Contains at least one digit | +1 |
| Contains at least one special character | +1 |

| Score | Rating |
|---|---|
| 4 | Strong |
| 2–3 | Moderate |
| 0–1 | Weak |

---

## Project Structure

```
project.py          # Main application
test_project.py     # Pytest test suite
my_passwords.txt    # Default save file (created on first save)
README.md           # This file
```

---

## Functions

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
Evaluates the strength of a given password based on length, character variety, digits, and special characters. Returns `"Strong"`, `"Moderate"`, or `"Weak"`.

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
        return "Moderate"
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

---

## Security Note

Passwords are saved in **plain text**. This is a learning project and is not intended for production use. For real password management, use a dedicated encrypted password manager.

---

## Author

Peter Sobhy — CS50P Final Project 2026
