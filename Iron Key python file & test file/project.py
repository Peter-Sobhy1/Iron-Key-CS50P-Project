import random
import string as s


def main():
    """The function of the application."""
    print("--- Welcome to \033[1m Iron Key \033[0m the Password Generator & Analyzer ---")
    # Choose either to generate or to analyze
    choice = input('Choose "1" to Generate Password\nChoose "2" to Analyze Password:\n')
    try:
        if choice == "1":
            # 1. Get user input
            user_input = input("How long do you want your password to be? (For Example: 16): ")
            length = int(user_input)
            
            if length < 4:
                print("For security, please choose a length of at least 4.")
                return

            # 2. Call Function 1: Generate
            new_password = generate_password(length)
            print(f"\nYour new password is: {new_password}")

            # 3. Call Function 2: Evaluate
            strength = evaluate_strength(new_password)
            print(f"Password Strength Rating: {strength}")

            # 4. Call Function 3: Save (Optional based on user choice)
            save_choice = input("\nWould you like to save this password to a file? (y/n): ").strip().lower()
            if save_choice == 'y':
                # asking for the name of the APP/Website
                app = input("This Password is for which APP/Website? ").strip()
                # asking if the user want to save in the default path or other path
                file_path = input('Choose "1" for Default Path Password\nor Enter Your File Path: ')
                if file_path == "1":
                    save_to_file(new_password, app)
                else:
                    save_to_file(new_password, app,file_path)
            else:
                print("Password not saved. Make sure to copy it!")

        elif choice == "2":
            print(evaluate_strength(input("Enter Your Password: ")))
        else:
            print('Please Choose "1" or "2"')

    except ValueError:
                print("Error: Please enter a valid whole number for the length.")


def generate_password(length):
    """Generates a random password using letters, numbers, and symbols."""
    # Combine all possible characters we want to use
    characters = s.ascii_letters + s.digits + s.punctuation
    
    # Randomly pick characters up to the requested length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def evaluate_strength(password):
    """Evaluates the strength of the password based on a few basic rules."""
    score = 0
    
    # Check for length
    if len(password) >= 12: 
        score += 1
    # Check for mix of upper and lower case
    if any(c.islower() for c in password) and any(c.isupper() for c in password): 
        score += 1
    # Check for numbers
    if any(c.isdigit() for c in password): 
        score += 1
    # Check for special characters
    if any(c in s.punctuation for c in password): 
        score += 1

    # Return a readable rating
    if score == 4:
        return "Strong"
    elif score >= 2:
        return "Intermediate"
    else:
        return "Weak"

def save_to_file(password, app,filename="my_passwords.txt"):
    """Appends the generated password to a local text file."""
    # Using "a" mode appends to the file instead of overwriting it
    line = f"{app}: {password}"
    with open(filename, "a") as file:
        file.write(line + "\n")
    print(f"Success! Password securely saved to {filename}.")


if __name__ == "__main__":
    main()