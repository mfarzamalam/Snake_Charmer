import unittest
from employee import *

class TestEmployeeClass(unittest.TestCase):

    def setUp(self):
        self.employee = Employee('first','last',5000)


    def test_give_default_raise(self):

        value = self.employee.give_raise()      # default value of this function is 5000
        self.assertEqual(value,10000)       # 5000(employee-salary) + 5000(default-raise-value) = 10000(total)


    def test_give_custom_raise(self):

        value = self.employee.give_raise(1000)  # We give the raise of 1000
        self.assertEqual(value,6000)            # 5000(employee-salary) + 1000(raise-value) = 6000(total)

unittest.main()