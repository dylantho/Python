"""
Program: Invoice.py
Author: Dylan Thomas
Last date modified: 11/2/2020
"""


class Invoice:
    # Constructor
    def __init__(self, invoice_id, customer_id, last_name, first_name, phone_number, address, items_with_price={}):
        self.invoice_id = invoice_id
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number
        self.address = address
        self.items_with_price = items_with_price

    def __str__(self):
        return 'Person(first_name={}, last_name={})'.format(self.first_name, self.last_name)

    def __repr__(self):
        return 'Person(first_name={}, last_name={})'.format(self.first_name, self.last_name)

    # Adds a key value pair to the instance's dictionary
    def add_item(self, pair):
        self.items_with_price.update(pair)

    def create_invoice(self):
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


# Driver code
invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
invoice.add_item({'iPad': 799.99})
invoice.add_item({'Surface': 999.99})
invoice.create_invoice()
