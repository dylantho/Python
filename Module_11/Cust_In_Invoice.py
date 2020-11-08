"""
Program: Cust_In_Invoice.py
Author: Dylan Thomas
Last date modified: 11/7/2020
"""


class Customer:
    # Constructor
    def __init__(self, customer_id, last_name, first_name, phone_number, address):
        # This statement in the constructor method raises an exception if the id is not an integer
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
        return 'Customer #{}: {}, {}\nPhone: {}\n{}'.format(self.customer_id, self.last_name, self.first_name, self.phone_number, self.address)


class Invoice:
    # Constructor
    def __init__(self, invoice_id, customer=' ', items_with_price={}):
        self.invoice_id = invoice_id
        self.items_with_price = items_with_price
        self.obj_customer = customer

    # Adds a key value pair to the instance's dictionary
    def add_item(self, pair):
        self.items_with_price.update(pair)

    def create_invoice(self):
        print(self.obj_customer.display())
        total = 0
        tax = 0.06
        # Prints the items and cost
        for key, value in self.items_with_price.items():
            print('{}.....${}'.format(key, value))
        # Calculates the total cost before tax
        for key, value in self.items_with_price.items():
            total += value

        # Calculates the cost of tax, total cost and prints both rounded with two decimal places
        tax_cost = total * tax
        tax_cost = round(tax_cost, 2)
        print('Tax.....{:0.2f}'.format(tax_cost))
        total += tax_cost
        total = round(total, 2)

        print('Total.....{:0.2f}'.format(total))


# Driver
captain_mal = Customer(1, 'Reynolds', 'Mel', 'No phones in the verse', 'Firefly, somewhere in the verse')
invoice = Invoice(1, captain_mal)
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()

del captain_mal
del invoice
print('\n-----------------------\n')

its_me = Customer(2, 'Thomas', 'Dylan', '111-222-3333', '123 Main Street\nUrban, Iowa')
invoice2 = Invoice(2, its_me, {'iPhone': 699.99})
invoice2.add_item({'Xbox Series X': 499.99})
invoice2.add_item({'Headphones': 39.99})
invoice2.create_invoice()

del its_me
del invoice2
