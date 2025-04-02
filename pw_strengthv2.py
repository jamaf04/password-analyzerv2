
import re
import random
import string

# Function to check password strength
def check_password_strength(password):  
    if len(password) < 8: 
        return "Weak: Password must be at least 8 characters long"
    
    if not re.search(r'[A-Z]', password):
        return "Weak: Password must contain at least one uppercase letter"
    
    if not re.search(r'[a-z]', password):  # Lowercase letter check
        return "Weak: Password must contain at least one lowercase letter"
    
    if not re.search(r'\d', password):
        return "Weak: Password must contain at least one digit"
    
    if not re.search(r'[^a-zA-Z0-9]', password):  # Special character check
        return "Weak: Password must contain at least one special character"

    return "Strong: Your password is strong!"


# Function to generate a strong password
def generate_strong_password(length=12):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation

    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_characters),
    ]

    all_characters = uppercase_letters + lowercase_letters + digits + special_characters
    password += random.choices(all_characters, k=length - 4)

    random.shuffle(password)

    return ''.join(password)


# Main function
def main():
    while True:  # Keeps the program running
        generate_password = input("Would you like me to generate a strong password for you? (yes/no/exit): ").strip().lower()

        if generate_password == 'yes':
            strong_password = generate_strong_password(12)
            print(f"Your generated strong password is: {strong_password}")
        
        elif generate_password == 'no':
            while True:
                password = input("Enter your password to check its strength (or type 'exit' to return to menu): ").strip()
                
                if password.lower() == 'exit':
                    break  # Returns to the main menu
                
                strength_result = check_password_strength(password)
                print(strength_result)  # Checks password strength
                
                if "Strong" in strength_result:
                    print("Exiting program. Your password is strong!")
                    exit()  # Exits the program immediately
        
        elif generate_password == 'exit':
            print("Goodbye!")
            break  # Ends the loop and exits the program
        
        else:
            print("Invalid input! Please enter 'yes', 'no', or 'exit'.")

if __name__ == "__main__":
    main()  # Ensures main() runs when script is executed
