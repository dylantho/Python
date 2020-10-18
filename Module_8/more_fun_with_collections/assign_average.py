"""
Program: assign_average.py
Author: Dylan Thomas
Last date modified: 10/17/2020
"""


def switch_average(argument):

    def test_a():
        return 97

    switch_dictionary = {
        'A': test_a,
    }

    function = switch_dictionary.get(argument, lambda: "Invalid key")
    return function()
