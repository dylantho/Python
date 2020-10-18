"""
Program: date_time.py
Author: Dylan Thomas
Last date modified: 10/17/2020
"""


from datetime import datetime, timedelta


def half_birthday(birthday):
    next_half_bday = birthday + timedelta(days=182)
    print('Next half birthday:', str(next_half_bday))

    return str(next_half_bday)


if __name__ == '__main__':
    pass
