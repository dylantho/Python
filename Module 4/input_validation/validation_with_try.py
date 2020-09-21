"""
Program: validation_with_try.py
Author: Dylan Thomas
Last date modified: 09/21/2020
"""
import sys

def average(score1, score2, score3):
    if score1 < 0:
        raise ValueError
    elif score2 < 0:
        raise ValueError
    elif score3 < 0:
        raise ValueError

    return ((score1+score2+score3)/3)

first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
age = input('Enter your age: ')

def main():
    try:
        score1 = int(input('Enter your first score: '))
        if score1 < 0:
            raise ValueError

        score2 = int(input('Enter your second score: '))
        if score2 < 0:
            raise ValueError

        score3 = int(input('Enter your third score: '))
        if score3 < 0:
            raise ValueError


    except ValueError:
        print()
        print("Error: Please input a positive number next time")
        print()
        main()

    average_scores = average(score1, score2, score3)

    print(f"{last_name}, {first_name} Age: {age} Average score: {average_scores} ")

if __name__ == '__main__':
    main()
