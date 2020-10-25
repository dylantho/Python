"""
Program: basic_gui_assignment.py
Author: Dylan Thomas
Last date modified: 10/25/2020
"""

import tkinter


def pick_breakfast():
    label.config(text="Pancakes?")


def pick_second_breakfast():
    label.config(text="Toast?")


def pick_lunch():
    label.config(text="Sandwiches?")


def pick_dinner():
    label.config(text="Pizza?")


if __name__ == '__main__':
    m = tkinter.Tk()

    m.title('Favorite Meal')

    label = tkinter.Label(m, text="Waiting")
    label.grid(row=5)

    var1 = tkinter.IntVar()
    check = tkinter.Checkbutton(m, text="Breakfast", variable=var1, command=pick_breakfast).grid(row=0)

    var2 = tkinter.IntVar()
    check = tkinter.Checkbutton(m, text="Second Breakfast", variable=var2, command=pick_second_breakfast).grid(row=1)

    var3 = tkinter.IntVar()
    check = tkinter.Checkbutton(m, text="Lunch", variable=var3, command=pick_lunch).grid(row=2)

    var4 = tkinter.IntVar()
    check = tkinter.Checkbutton(m, text="Dinner", variable=var4, command=pick_dinner).grid(row=3)

    exit_button = tkinter.Button(m, text='Exit', width=25, command=m.destroy)
    exit_button.grid(row=6)

    m.mainloop()
