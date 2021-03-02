"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.

    # Display an intro/welcome message to the player
    print("Welcome to the Guessing Game!")
    
    # Store a random number as the answer/solution
    answer = random.randint(0, 100)
    player_guess = "Wrong"
    NUMBER_OF_GUESSES = 0
    
    # Continuously prompt the player for a guess
    while player_guess == "Wrong":
    
        guessed_number = input("What number do you guess?  ")
        
        try:
            guessed_number = int(guessed_number)
            pass
        except:
            print("That is not a valid number. Please try inputting a number again")
            continue
            
        if guessed_number > answer:
            print("Your guess was {}".format(guessed_number))
            print("It's lower")
            NUMBER_OF_GUESSES += 1
            
        elif guessed_number < answer:
            print("Your guess was {}".format(guessed_number))
            print("It's higher")
            NUMBER_OF_GUESSES += 1
        
        else:
            print("Your guess was {}".format(guessed_number))
            print("Got it")
            print("It took you {} guesses".format(NUMBER_OF_GUESSES))
            print("Game Over")
            player_guess = "Right"

# Kick off the program by calling the start_game function.
start_game()
