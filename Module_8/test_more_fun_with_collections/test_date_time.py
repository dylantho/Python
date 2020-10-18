import unittest
from date_time import half_birthday
from datetime import datetime


class MyTestCase(unittest.TestCase):

    def test_half_birthday(self):
        birthday = datetime(2020, 7, 8)
        self.assertEqual(half_birthday(birthday), '2021-01-06 00:00:00')


if __name__ == '__main__':
    unittest.main()
