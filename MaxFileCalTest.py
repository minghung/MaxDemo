import unittest
from MaxFileCal import *

class calcTest(unittest.TestCase):
    def Test_load(self):
        """
        Use AAA pattern to test _load() - Arrange, Act, Assert
        """
        with open("test.txt", "w") as f:
            f.writelines(["1","2","3"])
        
        c = calc("test.txt")
        c._load()
        self.assertEquals(3, len(c.buffer))

    def Test_load_with_incorrect_filename(self):
        """
        TDD - Use Test-driven Development to highlight missing features
        """
        c = calc("unavailable.txt")
        c._load()
        self.assertRaises(FileNotFoundError)        

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