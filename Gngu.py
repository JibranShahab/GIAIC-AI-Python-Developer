import random

# Function to play the Guess the Number game
def guess_the_number():
    print("Welcome to the Guess the Number Game!")
    
    # The computer selects a random number between 1 and 100
    target_number = random.randint(1, 100)
    attempts = 0
    
    print("I have selected a number between 1 and 100. Try to guess it!")
    
    # While loop for the guessing process
    while True:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Provide feedback based on the guess
            if guess < target_number:
                print("Too low! Try again.")
            elif guess > target_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {target_number} correctly in {attempts} attempts.")
                break  # Exit the loop if the correct guess is made
        except ValueError:
            print("Please enter a valid number.")
    
# Call the function to start the game
guess_the_number()
