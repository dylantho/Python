"""
Program: validation_with_try.py
Author: Dylan Thomas
Last date modified: 09/21/2020
"""


def average(score1, score2, score3):
    return ((score1+score2+score3)/3)


def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    age = input('Enter your age: ')
    score1 = int(input('Enter your first score: '))
    score2 = int(input('Enter your second score: '))
    score3 = int(input('Enter your third score: '))
    average_scores = average(score1, score2, score3)

    print(f"{last_name}, {first_name} Age: {age} Average score: {average_scores} ")

if __name__ == '__main__':
    main()
