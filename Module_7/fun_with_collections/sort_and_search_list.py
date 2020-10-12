"""
Program: sort_and_search_list.py
Author: Dylan Thomas
Last date modified: 10/12/2020
"""


def sort_list():
    pass


def search_list(list, item):
    try:
        found = list.index(item)
    except ValueError:
        return -1

    return found


if __name__ == '__main__':
    pass
