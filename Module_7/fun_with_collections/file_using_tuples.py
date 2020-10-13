"""
Program: file_using_tuples.py
Author: Dylan Thomas
Last date modified: 10/12/2020
"""


def write_to_file(student_info):
    f = open('student_info.txt', 'a')
    f.writelines(student_info)
    f.close()


def get_student_info(**kwargs):
    scores = ['Name = {name} Scores = '.format(**kwargs)]
    answer = ''
    while answer != 'f':
        answer = input('Please enter the scores for {name}, enter f to finish: '.format(**kwargs))
        if answer != 'f':
            scores.append(answer)
            scores.append(' ')
        else:
            print('Done entering scores for ', '{name}.'.format(**kwargs), '\n')
            scores.append('\n')

    student_info = tuple(scores)
    write_to_file(student_info)

    return student_info


def read_from_file(file):
    f = open('student_info.txt', 'r')
    line1 = f.read()
    print(line1)
    f.close()


if __name__ == '__main__':
    get_student_info(name='Dylan')
    get_student_info(name='Jacob')
    get_student_info(name='Maria')
    get_student_info(name='Alex')

    read_from_file('student_info.text')

    endprogram = input('Press any key to end')


