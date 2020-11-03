"""
Program: Customer.py
Author: Dylan Thomas
Last date modified: 11/2/2020
"""


class Customer:
    # Constructor
    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        # This statement in the constructor method raises an exception if the id is not an integer
        # display() can be commented out and the error will still be raised by init when creating the object
        if not isinstance(customer_id, int):
            raise AttributeError("'Customer' object has no attribute 'cid'")
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address

    def __str__(self):
        return 'Person(first_name={}, last_name={})'.format(self.first_name, self.last_name)

    def __repr__(self):
        return 'Person(first_name={}, last_name={})'.format(self.first_name, self.last_name)

    def display(self):
        return 'Customer ID: {}\n{} {}\n{}\n{}'.format(self.customer_id, self.first_name, self.last_name, self.phone_number, self.address)


# Driver

# Create a Customer object customer1 with no error
customer1 = Customer(1, 'Patel', 'Sasha', '111-222-3333', '123 Main Street\nUrban, Iowa')

# Call display on customer1
print(customer1.display())
del customer1


# Create a Customer object customer2 that raises an exception with non-numeric customer id
customer2 = Customer('hey', 'Thomas', 'Dylan', '444-555-6666', '456 Mountain Street\nDenver, Colorado')

# Call display on customer2
print(customer2.display())
del customer2
