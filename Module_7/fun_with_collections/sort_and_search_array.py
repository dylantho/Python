"""
Program: sort_and_search_array.py
Author: Dylan Thomas
Last date modified: 10/12/2020
"""


def sort_array(array):
    pass


def search_array(array, item):
    try:
        found = array.index(item)
    except ValueError:
        return -1

    return found


if __name__ == '__main__':
    pass
