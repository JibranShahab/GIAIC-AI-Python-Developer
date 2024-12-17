import random

# Function to play the Rock, Paper, Scissors game
def rock_paper_scissors():
    # Options available in the game
    choices = ["rock", "paper", "scissors"]
    
    print("Welcome to Rock, Paper, Scissors Game!")
    
    # Loop to allow multiple rounds
    while True:
        # Get the user's choice
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'quit' to stop playing): ").lower()
        
        # Exit condition to quit the game
        if user_choice == 'quit':
            print("Thanks for playing! Goodbye!")
            break
        
        # Check for valid user input
        if user_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # Get the computer's random choice
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")
        
        # Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("You lose!")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break

# Call the function to start the game
rock_paper_scissors()
