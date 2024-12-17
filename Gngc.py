import random

# Function to play the guessing game
def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initializing the number of attempts
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess what it is?")
    
    # While loop to keep the game running until the correct guess
    while True:
        # Get user input and ensure it's an integer
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess and give feedback
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break  # Exit the while loop when the correct guess is made
        except ValueError:
            print("Please enter a valid number.")
    
# Call the function to start the game
play_game()
