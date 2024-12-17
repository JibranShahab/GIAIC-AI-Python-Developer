import time

# Function to implement the countdown timer
def countdown_timer():
    # Ask the user for the time in seconds
    try:
        seconds = int(input("Enter the time in seconds for the countdown: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    # Check if the input is a valid positive integer
    if seconds <= 0:
        print("Please enter a number greater than zero.")
        return

    print(f"Countdown starting from {seconds} seconds...\n")

    # Countdown loop
    while seconds > 0:
        # Display the remaining time
        print(f"Time left: {seconds} seconds")
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease the time by 1 second
    
    # When the countdown reaches zero
    print("\nTime's up! The countdown has finished.")
    
# Call the function to start the countdown timer
countdown_timer()
