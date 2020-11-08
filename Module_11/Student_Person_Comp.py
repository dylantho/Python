"""
Program: Student_Person_Comp.py
Author: Dylan Thomas
Last date modified: 11/7/2020
"""
import datetime


class Person:
    def __init__(self, lname, fname):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname

    def display(self):
        return str(self.last_name) + ", " + str(self.first_name)


class Student:
    """Student class"""
    def __init__(self, major, start, gpa=0.0, name=' '):
        if not isinstance(gpa, float):
            raise AttributeError
        if (gpa < 0) or (gpa > 4):
            raise ValueError

        self.major = major
        self._start_date = start
        self.obj_person_name = name
        self.gpa = gpa

    def change_major(self, new_major):
        # Added '!' and ' ' to characters for the 'Being Awesome!' major
        word_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz! '-")
        if not (word_characters.issuperset(new_major)):
            raise ValueError
        # Changes major
        self.major = new_major

    def update_gpa(self, new_gpa):
        # Input validation
        if not isinstance(new_gpa, float):
            raise AttributeError
        if (new_gpa < 0) or (new_gpa > 4):
            raise ValueError
        # Changes gpa
        self.gpa = new_gpa

    def display(self):
        # Print the person made by the person class
        print(self.obj_person_name.display())
        start_date = 'Start date: {}-{}-{}'.format(self._start_date.month, self._start_date.day, self._start_date.year)

        # Return Student info string
        return 'Major: {}\n{}\nGPA: {}'.format(self.major, start_date, self.gpa)


# Driver

student_me = Person('Thomas', 'Dylan')
student_me_info = Student('Computer Science', datetime.datetime(2020, 6, 28), 4.0, student_me)
print(student_me_info.display())
print('------------')
student_me_info.change_major('Being Awesome!')
student_me_info.update_gpa(3.0)
print(student_me_info.display())

del student_me
del student_me_info
print('\n------------\n')

student_new = Person('Douglas', 'Jamie')
student_new_info = Student('Herbology', datetime.datetime(2015, 7, 11), 3.0, student_new)
print(student_new_info.display())
print('------------')
student_new_info.change_major('Horticulture')
student_new_info.update_gpa(3.9)
print(student_new_info.display())

del student_new
del student_new_info
