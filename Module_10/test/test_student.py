import unittest
from Student import Student


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = Student('Oliver', 'John', 'Media')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Oliver')
        self.assertEqual(self.student.first_name, 'John')
        self.assertEqual(self.student.major, 'Media')


if __name__ == '__main__':
    unittest.main()
