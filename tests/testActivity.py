'''
Created on Aug 20, 2014

@author: valeriu
'''

import unittest
from datetime import datetime, timedelta
from ActivityTracker import Activity, ActivityError

class TestActivity(unittest.TestCase):


    def setUp(self):
        self.activity = Activity([])
        
        
    def tearDown(self):
        self.activity = None


    def testConstructorParameterStorage(self):
        self.assertEqual(self.activity._window_list, [], "Constructor parameter windows is ignored")
        
        
    def testConstructorParameterValidation(self):
        self.assertRaises(ActivityError, Activity, [{}])
        
      
    def testValidateListParameter(self):
        self.assertRaises(ActivityError, self.activity.validateWindows, 3)  
        
        
    def testValidateListDictionaryParameter(self):
        self.assertRaises(ActivityError, self.activity.validateWindows, [3]) 
        
        
    def testValidateListDictionaryKeys(self):
        self.assertRaises(ActivityError, self.activity.validateWindows, [{}]) 
    
    
    def testConstructorStartTime(self):
        self.assertGreater (self.activity._startTime, datetime.now() - timedelta(seconds=1), "startTime in constructor not initialized wit current time")
        self.assertLess    (self.activity._startTime, datetime.now() + timedelta(seconds=1), "startTime in constructor not initialized wit current time")
    
    
    def testConstructorDefaultDuration(self):
        self.assertEqual(self.activity._duration, 0, "Default duration in constructor must be 0")
    
    
    def testIncrementDurationParam(self):
        self.activity.incrementDuration(2)
        self.assertEqual(self.activity._duration, 2, "Function ignore parameter value")
    
    
    def testIncrementDurationDefaultParam(self):
        self.activity.incrementDuration()
        self.assertEqual(self.activity._duration, 1, "Default increment must be 1")
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()