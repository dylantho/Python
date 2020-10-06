"""
Program: validate_input_in_functions.py
Author: Dylan Thomas
Last date modified: 10/05/2020
"""


def score_input(test_name, test_score=0, invalid_message='Invalid test score, try again!'):
    """This function validates a test score then prints the user's exam name and score
    :param test_name, any string name of the test
    :param test_score, a positive integer with a default argument of 0
    :param invalid_message, the message that is displayed when the user enters an invalid input
    :returns The name of the test and score
    """
    while True:
        try:
            while (type(test_score) != int) or (test_score < 0) or (test_score > 100):

                print(invalid_message)
                raise ValueError
                test_score = int(input("Please enter a valid test score: "))
            break
        except ValueError:
            raise ValueError


    test_score = str(test_score)

    # return { test_name: test_score}
    return test_name + ": " + test_score




if __name__ == '__main__':
    pass
