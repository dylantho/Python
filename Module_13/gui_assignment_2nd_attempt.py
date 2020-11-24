"""
Program: gui_assignment_2nd_attempt.py
Author: Dylan Thomas
Last date modified: 11/23/2020
"""

from tkinter import *
from random import randrange


class NumberGuesser:
    # Constructor
    def __init__(self, guessed_list=[]):
        self.guessed_list = guessed_list

    # Used to check if guesses were being added
    def __str__(self):
        return 'Guesses: ={}'.format(self.guessed_list)

    # Add guess to list object
    def add_guess(self, guess):
        self.guessed_list.append(guess)
        return self.guessed_list.__str__()

# Initialize game
game = Tk()
game.title("Guessing Game")

# Start button and main labels
startButton = Button(game, text="Start Game", command=lambda: start_game()).grid(row=0, column=0, columnspan=5)
instruction = Label(game, text="Guess a number from 0 to 9").grid(row=1, column=0, columnspan=5)
space = Label(game, text="                                                                                  ").grid(row=3, column=0, columnspan=5)
space_bottom = Label(game, text="                                                                                  ").grid(row=14, column=0, columnspan=5)

# Create the number buttons in disabled state
buttons = []
for number in range(0, 10):
    button = Button(game, text=number, command=lambda number=number: check(number), state=DISABLED)
    buttons.append(button)
# Add buttons to the game grid
for row in range(0, 2):
    for col in range(0, 5):
        i = row * 5 + col
        buttons[i].grid(row=row+10, column=col)


# Global variables
guess = 0
answer = randrange(10)
newgame = NumberGuesser()
current_game = "none"


def start_game():
    global current_game
    # Make buttons clickable for use
    for b in buttons:
        b["state"] = NORMAL

    if current_game == "none":
        current_game = "In progress"
    else:
        current_game = "Reset"
        # call restart function
        restart_game()
    print("New game started")


# Reset game variables, hide previous result text
def restart_game():
    global buttons, guess, answer, newgame
    newgame.guessed_list = []
    answer = randrange(10)
    guess = 0
    hide_result = Label(game, text="                                                                        ").grid(row=13, column=0, columnspan=5)


# Check if the user guess correctly
def check(i):

    # Allow use of buttons list and newgame object
    global buttons, newgame
    guess = i

    # If user guessed correctly
    if guess == answer:
        answer_reaction_correct = Label(game, text="          Correct! You win!           ", fg="green").grid(row=13, column=0, columnspan=5)

        # If correct disable all buttons
        for button in buttons:
            button["state"] = DISABLED

    # If wrong add to guessed list, tell user
    else:
        newgame.add_guess(guess)
        answer_reaction_incorrect = Label(game, text="Incorrect. Try again!", fg="red").grid(row=13, column=0, columnspan=5)
    # if wrong disable button
    buttons[i]["state"] = DISABLED


game.mainloop()






