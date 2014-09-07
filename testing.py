#!/usr/bin/python

import unittest

class FirstTest(unittest.TestCase):
    """First go at writing python unit test cases."""
    
    def setUp(self):
        """Test env setup"""
        print ("Seting up the env")
        
    def tearDown(self):
        """Clean up after test"""
        print ("Tearing down the env.")
        
    def test_1(self):
        """Passing test routine to run..."""
        self.assertTrue(True, "This is a passing test")
        
    def test_2(self):
        """Failing test routine to run..."""
        self.assertTrue(False, "This is a failing test")



if __name__ == "__main__":
    fooSuite = unittest.TestLoader().loadTestsFromTestCase(FirstTest)
     
    fooRunner = unittest.TextTestRunner()
    fooRunner.run(fooSuite)
 
    
        