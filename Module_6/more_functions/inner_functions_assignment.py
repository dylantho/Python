"""
Program: inner_functions_assignment.py
Author: Dylan Thomas
Last date modified: 10/05/2020
"""



def measurements(a_list):
    width = 0
    length = a_list[0]
    if len(a_list) == 2:
        width = a_list[1]


    def area(a_list):
        areaCalc = 0
        if len(a_list) == 1:
            areaCalc = length * length
        elif len(a_list) == 2:
            areaCalc = length * width
        else:
            print("There should only be one or two values.")
        return areaCalc

    def perimeter(a_list):
        perimeterCalc = 0
        if len(a_list) == 1:
            perimeterCalc = length * 4
        elif len(a_list) == 2:
            perimeterCalc = (length * 2) + (width * 2)
        else:
            print("There should only be one or two values.")
        return perimeterCalc

    listPerimeter = str(perimeter(a_list))
    listArea = str(area(a_list))

    return "Perimeter = " + listPerimeter + " Area = " + listArea

