import unittest
from employee_salary import Employee


class TestCase(unittest.TestCase):
    def setUp(self):
        self.employee_salary = Employee('mohammed', 'mubarak', 100000)

    def test_give_default_salary(self):
        default_salary = 5000
        self.employee_salary.give_raise(default_salary)
        self.assertEqual(
            105000, self.employee_salary.annual_salary + default_salary)

    def test_give_custom_salary(self):
        custom_salary = 20000
        self.employee_salary.give_raise(custom_salary)
        self.assertEqual(
            120000, self.employee_salary.annual_salary + custom_salary)


if __name__ == '__main__':
    unittest.main()
