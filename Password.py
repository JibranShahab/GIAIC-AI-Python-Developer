import random
import string

# Function to generate a random password
def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    # Initialize the character pool based on user preferences
    char_pool = lowercase
    if use_uppercase:
        char_pool += uppercase
    if use_numbers:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars
    
    # Generate a random password by selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

# Function to get user preferences and generate the password
def password_generator():
    print("Welcome to the Password Generator!")
    
    # Get the password length from the user
    while True:
        try:
            length = int(input("Enter the length of the password (minimum 6 characters): "))
            if length < 6:
                print("Password length should be at least 6 characters. Please try again.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    # Get user preferences for the types of characters
    use_uppercase = input("Include uppercase letters? (yes/no): ").strip().lower() == "yes"
    use_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
    use_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"
    
    # Generate the password based on the user's choices
    password = generate_password(length, use_uppercase, use_numbers, use_special_chars)
    
    print("\nGenerated Password:")
    print(password)

# Call the function to start the password generator
password_generator()
