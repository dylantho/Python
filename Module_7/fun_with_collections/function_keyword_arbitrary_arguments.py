"""
Program: function_keyword_arbitrary_arguments.py
Author: Dylan Thomas
Last date modified: 10/12/2020
"""


def average_scores(*args, **kwargs):
    total = 0
    count = 0
    for num in args:
        total = total + num
        count = count + 1
    average = total / count

    return 'Result: Name = {first_name} GPA = {gpa} Course = {course} with current average '.format(**kwargs) + str(average)


if __name__ == '__main__':
    print(average_scores(86, 95, 97, 91, first_name='Dylan', gpa=3.2, course='Python'))
    print(average_scores(75, 63, 86, 79, first_name='Jacob', gpa=2.8, course='Pre-Calculus'))
    print(average_scores(99, 100, 95, 93, first_name='Maria', gpa=3.8, course='Astronomy'))
