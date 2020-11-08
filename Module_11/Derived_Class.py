"""
Program: Derived_Class.py
Author: Dylan Thomas
Last date modified: 11/7/2020
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        self._last_name = lname
        self._first_name = fname
        self._address = addy

    def display(self):
        return self._last_name + ", " + self._first_name + ":" + self._address


class Student(Person):
    """Student class"""
    def __init__(self, student_id, lname, fname, major='Computer Science', gpa=0.0):
        super().__init__(lname, fname)
        self._student_id = student_id
        self._major = major
        self._gpa = gpa

    def display(self):
        return self._last_name + ", " + self._first_name + ":(" + str(self._student_id) + ") " + self._major + " gpa: " + str(self._gpa)

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)


# Driver
my_student = Student(900111111, 'Song', 'River')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering')
print(my_student.display())
my_student = Student(900111111, 'Song', 'River', 'Computer Engineering', 4.0)
print(my_student.display())
del my_student
