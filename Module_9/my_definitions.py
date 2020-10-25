"""
Program: my_definitions.py
Author: Dylan Thomas
Last date modified: 10/25/2020
"""


def greeting():
    print("Hello, welcome to my program!")


def message():
    print("This program was written by Dylan Thomas.")


def print_dict(user_dict):
    for key, value in user_dict.items():
        print("Key :", key, " Value :", value)


def print_set(user_set):
    for key, value in user_set.items():
        print("Key :", key, " Value :", value)


if __name__ == '__main__':
    pass
