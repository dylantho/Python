"""
Program: gui_assignment_orig.py
Author: Dylan Thomas
Last date modified: 11/23/2020
"""

from tkinter import *
from random import randrange

class NumberGuesser:
    # Constructor
    def __init__(self, guessed_list=[]):
        self.guessed_list = guessed_list

    def __str__(self):
        return 'Guesses: ={}'.format(self.guessed_list)

    def add_guess(self, guess):
        self.guessed_list.append(guess)
        # Line below confirms guessed list resets and guesses are added correctly
        # print(self.guessed_list.__str__())


newgame = NumberGuesser()


def start():
    # Pick random
    answer = randrange(10)
    # Allow use of number guesser object
    global newgame
    # Init guess list
    newgame.guessed_list = []

    # Buttons when the user has pressed start game
    noanswer = Label(root, text="", width=35, borderwidth=5).grid(row=3, column=0, columnspan=5)
    button_0 = Button(root, text="0", padx=40, pady=20, command=lambda: guess_click(0, answer)).grid(row=1, column=0)
    button_1 = Button(root, text="1", padx=40, pady=20, command=lambda: guess_click(1, answer)).grid(row=1, column=1)
    button_2 = Button(root, text="2", padx=40, pady=20, command=lambda: guess_click(2, answer)).grid(row=1, column=2)
    button_3 = Button(root, text="3", padx=40, pady=20, command=lambda: guess_click(3, answer)).grid(row=1, column=3)
    button_4 = Button(root, text="4", padx=40, pady=20, command=lambda: guess_click(4, answer)).grid(row=1, column=4)

    button_5 = Button(root, text="5", padx=40, pady=20, command=lambda: guess_click(5, answer)).grid(row=2, column=0)
    button_6 = Button(root, text="6", padx=40, pady=20, command=lambda: guess_click(6, answer)).grid(row=2, column=1)
    button_7 = Button(root, text="7", padx=40, pady=20, command=lambda: guess_click(7, answer)).grid(row=2, column=2)
    button_8 = Button(root, text="8", padx=40, pady=20, command=lambda: guess_click(8, answer)).grid(row=2, column=3)
    button_9 = Button(root, text="9", padx=40, pady=20, command=lambda: guess_click(9, answer)).grid(row=2, column=4)


def guess_click(guess, answer):
    if guess == answer:
        # Buttons disabled if the user gets the answer correct
        button_0 = Button(root, text="0", padx=40, pady=20, state=DISABLED).grid(row=1, column=0)
        button_1 = Button(root, text="1", padx=40, pady=20, state=DISABLED).grid(row=1, column=1)
        button_2 = Button(root, text="2", padx=40, pady=20, state=DISABLED).grid(row=1, column=2)
        button_3 = Button(root, text="3", padx=40, pady=20, state=DISABLED).grid(row=1, column=3)
        button_4 = Button(root, text="4", padx=40, pady=20, state=DISABLED).grid(row=1, column=4)

        button_5 = Button(root, text="5", padx=40, pady=20, state=DISABLED).grid(row=2, column=0)
        button_6 = Button(root, text="6", padx=40, pady=20, state=DISABLED).grid(row=2, column=1)
        button_7 = Button(root, text="7", padx=40, pady=20, state=DISABLED).grid(row=2, column=2)
        button_8 = Button(root, text="8", padx=40, pady=20, state=DISABLED).grid(row=2, column=3)
        button_9 = Button(root, text="9", padx=40, pady=20, state=DISABLED).grid(row=2, column=4)
        # Tell user correct guess
        bottom_label = Label(root, text="                         Correct answer!                           ", fg="green").grid(row=3, column=0, columnspan=5)

    else:
        # Whichever incorrect button was pressed becomes disabled
        if guess == 0:
            button_0 = Button(root, text="0", padx=40, pady=20, state=DISABLED).grid(row=1, column=0)
        elif guess == 1:
            button_1 = Button(root, text="1", padx=40, pady=20, state=DISABLED).grid(row=1, column=1)
        elif guess == 2:
            button_2 = Button(root, text="2", padx=40, pady=20, state=DISABLED).grid(row=1, column=2)
        elif guess == 3:
            button_3 = Button(root, text="3", padx=40, pady=20, state=DISABLED).grid(row=1, column=3)
        elif guess == 4:
            button_4 = Button(root, text="4", padx=40, pady=20, state=DISABLED).grid(row=1, column=4)
        elif guess == 5:
            button_5 = Button(root, text="5", padx=40, pady=20, state=DISABLED).grid(row=2, column=0)
        elif guess == 6:
            button_6 = Button(root, text="6", padx=40, pady=20, state=DISABLED).grid(row=2, column=1)
        elif guess == 7:
            button_7 = Button(root, text="7", padx=40, pady=20, state=DISABLED).grid(row=2, column=2)
        elif guess == 8:
            button_8 = Button(root, text="8", padx=40, pady=20, state=DISABLED).grid(row=2, column=3)
        elif guess == 9:
            button_9 = Button(root, text="9", padx=40, pady=20, state=DISABLED).grid(row=2, column=4)

        # Guess added to object
        newgame.add_guess(guess)
        # Tell user incorrect guess
        bottom_label = Label(root, text="Incorrect guess. Try Again!", fg="red").grid(row=3, column=0, columnspan=5)


root = Tk()
root.title("Guessing Game")

start = Button(root, text="Start Game", width=35, borderwidth=5, command=start).grid(row=0, column=0, columnspan=5, padx=10, pady=10)

# Initial state of buttons before start game is pressed
button_0 = Button(root, text="0", padx=40, pady=20, state=DISABLED).grid(row=1, column=0)
button_1 = Button(root, text="1", padx=40, pady=20, state=DISABLED).grid(row=1, column=1)
button_2 = Button(root, text="2", padx=40, pady=20, state=DISABLED).grid(row=1, column=2)
button_3 = Button(root, text="3", padx=40, pady=20, state=DISABLED).grid(row=1, column=3)
button_4 = Button(root, text="4", padx=40, pady=20, state=DISABLED).grid(row=1, column=4)

button_5 = Button(root, text="5", padx=40, pady=20, state=DISABLED).grid(row=2, column=0)
button_6 = Button(root, text="6", padx=40, pady=20, state=DISABLED).grid(row=2, column=1)
button_7 = Button(root, text="7", padx=40, pady=20, state=DISABLED).grid(row=2, column=2)
button_8 = Button(root, text="8", padx=40, pady=20, state=DISABLED).grid(row=2, column=3)
button_9 = Button(root, text="9", padx=40, pady=20, state=DISABLED).grid(row=2, column=4)

bottom_label = Label(root, text="", width=35, borderwidth=5).grid(row=3, column=0, columnspan=5, padx=10, pady=10)

root.mainloop()
