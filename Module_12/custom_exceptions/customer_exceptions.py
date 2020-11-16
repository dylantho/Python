"""
Program: customer_exceptions.py
Author: Dylan Thomas
Last date modified: 11/15/2020
"""


class Customer:
    # Constructor
    def __init__(self, customer_id, last_name, first_name, phone_number):
        # Leftover exception from module 10
        if not isinstance(customer_id, int):
            raise AttributeError("'Customer' object has no attribute 'cid'")

        # Custom constructor exception 1 for Id outside of range
        if customer_id < 1000 or customer_id > 9999:
            raise InvalidCustomerIdException

        # Custom constructor exception 2 (last) for non alpha characters (' and - are included in acceptable characters ie: O'Malley, Mary-Louise
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(last_name)):
            raise InvalidNameException

        # Custom constructor exception 2 (first) for non alpha characters (' and - are included in acceptable characters ie: O'Malley, Mary-Louise
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(first_name)):
            raise InvalidNameException

        # Custom constructor exception 3 for phone number with invalid format (Not 12 char, no hyphens in the right spots, not numeric char)
        numeric_characters = set("0123456789-")
        if len(phone_number) != 12:
            raise InvalidPhoneNumberFormat
        for i in range(12):
            if not numeric_characters.issuperset(phone_number):
                raise InvalidPhoneNumberFormat
            if i in [3, 7]:
                if phone_number[i] != '-':
                    raise InvalidPhoneNumberFormat
            if i in [0, 1, 2, 4, 5, 6, 8, 9, 10, 11, 12]:
                if phone_number[i] == '-':
                    raise InvalidPhoneNumberFormat

        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

    def __str__(self):
        return 'Customer(first_name={}, last_name={})'.format(self.first_name, self.last_name)

    def __repr__(self):
        return 'Customer(first_name={}, last_name={})'.format(self.first_name, self.last_name)

    def display(self):
        return 'Customer ID: {}\n{} {}\n{}'.format(self.customer_id, self.first_name, self.last_name, self.phone_number)


# Create first exception class
class InvalidCustomerIdException(Exception):
    pass


# Create second exception class
class InvalidNameException(Exception):
    pass


# Create third exception class
class InvalidPhoneNumberFormat(Exception):
    pass


# Driver

# Call constructor with invalid customer_id
my_id = 999
try:
    customer = Customer(my_id, 'Patel', 'Sasha', '111-222-3333')
except InvalidCustomerIdException:
    print("Invalid Customer ID '", my_id, "' must be between 1000-9999")

# Call constructor with invalid last_name
my_last = 'Thomas1'
try:
    customer = Customer(1234, my_last, 'Dylan', '444-555-6666')
except InvalidNameException:
    print("Invalid last name '", my_last, "' must include only alpha characters (includes - and ')")

# Call constructor with invalid first_name
my_first = 'Dylan!'
try:
    customer = Customer(1234, 'Thomas', my_first, '444-555-6666')
except InvalidNameException:
    print("Invalid first name '", my_first, "' must include only alpha characters (includes - and ')")

# Call constructor with invalid phone_number
my_phone = '4d4-5546-666'
try:
    customer = Customer(1234, 'Thomas', 'Dylan', my_phone)
except InvalidPhoneNumberFormat:
    print("Invalid number format '", my_phone, " 'must be 12 char, xxx-xxx-xxxx format, only numeric char")

# Call str()
customer = Customer(1234, 'Thomas', 'Dylan', '444-555-6666')
print(str(customer))

