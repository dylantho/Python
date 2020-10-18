"""
Program: dictionary_update.py
Author: Dylan Thomas
Last date modified: 10/17/2020
"""


def get_test_scores():
    scores_dict = dict()
    num_scores = int(input('Enter the number of test scores: '))

    while num_scores < 0:
        num_scores = int(input('Less than zero, please enter the number of test scores: '))

    count = num_scores

    '''For now storing the test key as an increasing number {1: 95, 2: 97} 
    for future assignment can add user input to get test name {Exam 1: 95, Quiz 4: 86}'''
    test_counter = 1

    while count > 0:
        score = int(input('Enter a test score: '))

        while score < 0:
            score = int(input('Enter a test score above or equal to 0: '))

        count = count - 1
        scores_dict.update({test_counter: score})
        test_counter = test_counter + 1

    return scores_dict


def average_scores(scores_dict):
    total_length = len(scores_dict)
    length_count = len(scores_dict)
    total = 0

    while length_count > 0:
        total = scores_dict[length_count] + total
        length_count = length_count - 1

    average = total/total_length

    return average


if __name__ == '__main__':
    print(get_test_scores())
    print(average_scores(get_test_scores()))
