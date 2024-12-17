import random

# List of words for the game
words = ["python", "hangman", "programming", "computer", "developer", "code", "algorithm", "function"]

# Function to play the Hangman game
def hangman():
    print("Welcome to Hangman!")
    
    # Select a random word
    word = random.choice(words)
    word_display = "_" * len(word)  # To display the word as underscores initially
    attempts_left = 6
    guessed_letters = []
    
    # Game loop
    while attempts_left > 0:
        print(f"\nWord to guess: {' '.join(word_display)}")
        print(f"Attempts left: {attempts_left}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        
        # Get the player's guess
        guess = input("Guess a letter: ").lower()
        
        # Validate input (must be a single letter)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
        
        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        # Add the guessed letter to the list of guessed letters
        guessed_letters.append(guess)
        
        # Check if the guess is correct
        if guess in word:
            print(f"Good guess! The letter '{guess}' is in the word.")
            # Update word_display with the correct guessed letter
            word_display = list(word_display)
            for i in range(len(word)):
                if word[i] == guess:
                    word_display[i] = guess
            word_display = "".join(word_display)
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            attempts_left -= 1
        
        # Check if the player has guessed the word
        if "_" not in word_display:
            print(f"\nCongratulations! You guessed the word: {word}!")
            break
    
    # If the player runs out of attempts
    if attempts_left == 0:
        print(f"\nSorry, you ran out of attempts. The word was: {word}")

# Call the function to start the game
hangman()
