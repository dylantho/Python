"""
Program: Multiple_Inherit.py
Author: Dylan Thomas
Last date modified: 11/8/2020
"""
import datetime


class Person:
    """Person class"""
    def __init__(self, lastname, firstname, address=''):
        self.lastname = lastname
        self.firstname = firstname
        self.address = address

    def display(self):
        return self.last_name + ", " + self.first_name + ":" + self.address


class Employee:
    """Employee class"""
    def __init__(self, salary, start_date, employee_last_name, employee_first_name):
        self.employee_first_name = employee_first_name
        self.employee_last_name = employee_last_name
        self.salary = salary
        self.start_date = start_date
        self.start_date = '{}-{}-{}'.format(self.start_date.month, self.start_date.day, self.start_date.year)

    def give_raise(self, new_salary):
        self.salary = new_salary

    def full_name(self):
        return self.employee_last_name + ", " + self.employee_first_name


class Manager(Person, Employee):
    """Manager class"""
    def __init__(self, lastname, firstname, address, salary, start_date, department, direct_reports=None, employee_first_name="", employee_last_name=""):
        Person.__init__(self, lastname, firstname, address)
        Employee.__init__(self, salary, start_date, employee_first_name, employee_last_name)
        self.department = department
        self.direct_reports = direct_reports
        if direct_reports is None:
            self.direct_reports = []
        else:
            self.direct_reports = direct_reports

    def add_employee(self, employee):
        self.direct_reports.append(employee)

    def print_employees(self):
        print("Employees that report to manager - " + self.firstname + " " + self.lastname)
        for emp in self.direct_reports:
            print("------> " + emp.full_name())

    def display(self):
        return 'Manager: {}, {}\nAddress: {}\nSalary: {}\nStart Date: {}\nDepartment: {}'.format(self.lastname, self.firstname, self.address, str(self.salary), str(self.start_date), self.department)


# Driver

# Creates a Manager  object with my name, start date today, starting salary $40,000
my_manager = Manager('Thomas', 'Dylan', '456 Mountain Street Denver, Colorado', 40000, datetime.datetime(2020, 11, 7), 'IT')

# Displays the Manager object  # the display() that was used was in the Manager class
print(my_manager.display(), "\n")

# 1. Creates objects of type Employee
emp1 = Employee(35000, datetime.datetime(2020, 11, 7), "Butler", "Jimmy")
emp2 = Employee(30000, datetime.datetime(2020, 12, 3), "Carter", "Bailey")
# 2. Adds to Manager's direct reports
my_manager.add_employee(emp1)
my_manager.add_employee(emp2)
# 3. Displays Manager's direct reports
my_manager.print_employees()
print()

# Change salary to $42,000
my_manager.give_raise(42000)

# Displays the Manager object  # the display() that was used was in the Manager class
print(my_manager.display(), "\n")

# Performs garbage collection
del emp1, emp2
del my_manager
