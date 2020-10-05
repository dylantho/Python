"""
Program: inner_functions_assignment.py
Author: Dylan Thomas
Last date modified: 10/05/2020
"""



def measurements(a_list):
    length = a_list[0]
    width = a_list[1]


    def area(a_list):
        areaCalc = 0
        areaCalc = length * width

        return areaCalc

    def perimeter(a_list):
        perimeterCalc = 0
        perimeterCalc = (length * 2) + (width * 2)

        return perimeterCalc

    listPerimeter = str(perimeter(a_list))
    listArea = str(area(a_list))

    return "Perimeter = " + listPerimeter + " Area = " + listArea

