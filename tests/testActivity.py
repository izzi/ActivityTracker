'''
Created on Aug 20, 2014

@author: valeriu
'''

import unittest
from datetime import datetime, timedelta
from activitytracker import Activity, ActivityError

class TestActivity(unittest.TestCase):


    def setUp(self):
        self.activity = Activity([])
        
        
    def tearDown(self):
        self.activity = None


    def test_constructor_parameter_storage(self):
        self.assertEqual(self.activity._window_list, [], "Constructor parameter windows is ignored")
        
        
    def test_constructor_parameter_validation(self):
        self.assertRaises(ActivityError, Activity, [{}])
        
      
    def test_validate_windows_empty_list_parameter(self):
        self.assertRaises(ActivityError, self.activity.validate_windows, 3)  
        
        
    def test_validate_windows_list_of_dictionary_parameter(self):
        self.assertRaises(ActivityError, self.activity.validate_windows, [3]) 
        
        
    def test_validate_windows_list_dictionary_keys(self):
        self.assertRaises(ActivityError, self.activity.validate_windows, [{}]) 
    
    
    def test_constructor_default_start_time(self):
        self.assertGreater (self.activity._start_time, datetime.now() - timedelta(seconds=1), "startTime in constructor not initialized wit current time")
        self.assertLess    (self.activity._start_time, datetime.now() + timedelta(seconds=1), "startTime in constructor not initialized wit current time")
    
    
    def test_constructor_default_duration(self):
        self.assertEqual(self.activity._duration, 0, "Default duration in constructor must be 0")
    
    
    def test_increment_duration_param(self):
        self.activity.increment_duration(2)
        self.assertEqual(self.activity._duration, 2, "Function ignore parameter value")
    
    
    def test_increment_duration_default_param(self):
        self.activity.increment_duration()
        self.assertEqual(self.activity._duration, 1, "Default increment must be 1")
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()