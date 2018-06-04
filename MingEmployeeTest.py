import unittest
from MingEmployee import *

class EmployeeTest(unittest.TestCase):
    def test_add_employee(self):
        company = EmployeeRepository()
        company += Employee(1, "Employee1")
        company += Employee(2, "Employee2")
        self.assertEqual(2, len(company._employees))

    def test_add_employee_with_duplicates(self):
        company = EmployeeRepository()
        company.add_employee(Employee(1, "Emp1"))
        self.assertEqual(1, len(company._employees))

        try:
            company.add_employee(Employee(1, "Emp1"))
        except ValueError:           
            self.assertEqual(1, len(company._employees))

    def test_remove_employee(self):
        company = EmployeeRepository()
        emp = Employee(1, "Employee1")
        company += emp
        company -= emp
        self.assertEqual(0, len(company._employees))

    def test_find_employees_by_name(self):
        company = EmployeeRepository()
        company += Employee(1, "John")
        company += Employee(2, "Mary")
        company += Employee(3, "Ming")

        #expect to find 2 employees whose name starts with 'm'
        found = [emp for emp in company.get_employees_by_name("m")]
        self.assertEqual(len(found), 2)

        #expect to find employee 'John'
        found = [emp for emp in company.get_employees_by_name("j")]
        self.assertEqual("John", found[0].name)

if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(EmployeeTest)
    unittest.TextTestRunner(verbosity=2).run(suite)