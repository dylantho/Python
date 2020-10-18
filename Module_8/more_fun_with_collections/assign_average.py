"""
Program: assign_average.py
Author: Dylan Thomas
Last date modified: 10/17/2020
"""


def switch_average(argument):

    def test_a():
        return 97

    def test_b():
        return 87

    def test_c():
        return 75

    def test_d():
        return 68

    switch_dictionary = {
        'A': test_a,
        'B': test_b,
        'C': test_c,
        'D': test_d
    }

    function = switch_dictionary.get(argument, lambda: "Invalid key")
    return function()
