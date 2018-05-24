import unittest
from MaxFileCal import calc

class calcTest(unittest.TestCase):
    def Test_input(self):
        self.assertEqual(2, 2)
    
    def Test_print(self):   
        self.assertEqual(2, 2)

    def Test_add(self):
        self.assertEqual(2, 2)


    def Test_product(self):
        self.assertEqual(2, 2)

if __name__ == "__main__":
    unittest.main()
    #suite = unittest.TestLoader().loadTestsFromTestCase(EmployeeTest)
    #unittest.TextTestRunner(verbosity=2).run(suite)