"""
Program: average_scores.py
Author: Dylan Thomas
Last date modified: 09/14/2020
"""


def average():
    score1 = int(input('Enter your first score: '))
    score2 = int(input('Enter your second score: '))
    score3 = int(input('Enter your third score: '))
    return ((score1+score2+score3)/3)


def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    age = input('Enter your age: ')
    average_scores = average()

    print(f"{last_name}, {first_name} Age: {age} Average score: {average_scores} ")


#Test passed with scores of 85, 90, 95 and expected result of 90 (correct)
#Test failed with scores of 85, 90, 95 and expected result of 91 (incorrect)
#Test passed with scores of 89, 80, 98 and expected result of 89 (correct)
