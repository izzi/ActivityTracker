'''
Created on Aug 20, 2014

@author: valeriu
'''
import unittest
from ActivityTracker import Activity

class TestActivity(unittest.TestCase):


    def setUp(self):
        self.activity = Activity(1, 2)
        
        
    def tearDown(self):
        self.activity = None


    def testConfigSetup(self):
        self.assertEqual(1, self.activity._config, "Config is not stored properly")
        
    
    def testMonitorSetup(self):
        self.assertEqual(2, self.activity._monitor, "Monitor is not stored properly")
    
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()