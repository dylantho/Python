import unittest
from customer_exceptions import Customer, InvalidCustomerIdException, InvalidNameException, InvalidPhoneNumberFormat


class CustomerTest(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer(5000, 'Thomas', 'Dylan', '111-222-3333')

    def tearDown(self):
        del self.customer_1

    # Test 1: Valid customer id
    def test_valid_customer_id(self):
        self.customer_1.customer_id = 4500
        self.assertEqual(self.customer_1.customer_id, 4500)

    # Test 2: Invalid customer id
    def test_invalid_customer_id(self):
        # Under range
        with self.assertRaises(InvalidCustomerIdException):
            c = Customer(50, 'Thomas', 'Dylan', '111-222-3333')
            # Over range
        with self.assertRaises(InvalidCustomerIdException):
            c = Customer(50000, 'Thomas', 'Dylan', '111-222-3333')

    # Test 3: Valid last name
    def test_valid_last_name(self):
        self.customer_1.last_name = 'John'
        self.assertEqual(self.customer_1.last_name, 'John')

    # Test 4: Invalid last name
    def test_invalid_last_name(self):
        with self.assertRaises(InvalidNameException):
            c = Customer(5000, 'Thomas!!', 'Dylan', '111-222-3333')

    # Test 5: Valid first name
    def test_valid_last_name(self):
        self.customer_1.first_name = 'Matt'
        self.assertEqual(self.customer_1.first_name, 'Matt')

    # Test 6: Invalid first name
    def test_invalid_last_name(self):
        with self.assertRaises(InvalidNameException):
            c = Customer(5000, 'Thomas', 'Dyla234n', '111-222-3333')

    # Test 7: Valid phone number
    def test_valid_phone_number(self):
        self.customer_1.phone_number = '513-714-1456'
        self.assertEqual(self.customer_1.phone_number, '513-714-1456')

    # Test 8: Invalid phone number
    def test_invalid_phone_number(self):
        # Hyphens in extra places
        with self.assertRaises(InvalidPhoneNumberFormat):
            c = Customer(4500, 'Thomas', 'Dylan', '111-2-2-33-3')
        # Too many characters
        with self.assertRaises(InvalidPhoneNumberFormat):
            c = Customer(4500, 'Thomas', 'Dylan', '111-222-33334')
        # Alpha character
        with self.assertRaises(InvalidPhoneNumberFormat):
            c = Customer(4500, 'Thomas', 'Dylan', '111-2A2-3333')

    # Test 9: __str__
    def test_student_str(self):
        self.assertEqual(str(self.customer_1), 'Customer(first_name=Dylan, last_name=Thomas)')


if __name__ == '__main__':
    unittest.main()
