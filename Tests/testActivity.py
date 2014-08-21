'''
Created on Aug 20, 2014

@author: valeriu
'''
import unittest
from ActivityTracker import Activity

class TestActivity(unittest.TestCase):


    def setUp(self):
        self.activity = Activity([])
        
        
    def tearDown(self):
        self.activity = None


    def testWindowParameter(self):
        self.assertEqual(self.activity._windows, [], "Constructor parameter windows is ignored")
        
    
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()