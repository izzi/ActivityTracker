'''
Created on Aug 20, 2014

@author: valeriu
'''
import unittest
from ActivityTracker import ActivityError


class TestException(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testStringFormat(self):
        
        exception = ActivityError(2, '{0}')

        self.assertEqual('2', str(exception), "Incorect string formatting in exception")
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()