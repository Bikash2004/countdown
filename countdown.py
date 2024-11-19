"""
Countdown Timer

This Python script allows you to set a countdown timer. You can specify the duration in seconds, 
and the program will display the time remaining in real-time.

To run the script:
1. Install Python (if not already installed) from https://www.python.org/.
2. Save this script as `countdown_timer.py`.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script using: python countdown_timer.py
5. Enter the countdown time in seconds when prompted.
"""

import time

def countdown_timer(seconds):
    """
    Function to run the countdown timer.
    
    Parameters:
    - seconds (int): Number of seconds to count down from.
    
    The function prints the time remaining in the format 'MM:SS'.
    """
    try:
        while seconds >= 0:
            # Calculate minutes and seconds
            minutes, secs = divmod(seconds, 60)
            
            # Format the time as MM:SS
            timer = f"{minutes:02}:{secs:02}"
            
            # Print the timer, overwriting the previous line
            print(timer, end="\r")
            
            # Wait for one second
            time.sleep(1)
            
            # Decrement the seconds
            seconds -= 1
        
        # Print the completion message
        print("Time's up! 🚨")
    
    except KeyboardInterrupt:
        # Handle manual interruption
        print("\nTimer interrupted. Exiting...")

if __name__ == "__main__":
    # Prompt the user for input duration
    try:
        duration = int(input("Enter the countdown time in seconds: "))
        if duration < 0:
            print("Please enter a positive number.")
        else:
            countdown_timer(duration)
    except ValueError:
        print("Invalid input. Please enter an integer value.")
