'''
Created on Aug 20, 2014

@author: valeriu
'''
import unittest
from ActivityTracker import Activity, ActivityException

class TestActivity(unittest.TestCase):


    def setUp(self):
        self.activity = Activity([])
        
        
    def tearDown(self):
        self.activity = None


    def testConstructorParameterStorage(self):
        self.assertEqual(self.activity._window_list, [], "Constructor parameter windows is ignored")
        
        
    def testConstructorParameterValidation(self):
        self.assertRaises(ActivityException, Activity, [{}])
        
      
    def testValidateListParameter(self):
        self.assertRaises(ActivityException, self.activity.validateWindows, 3)  
        
        
    def testValidateListDictionaryParameter(self):
        self.assertRaises(ActivityException, self.activity.validateWindows, [3]) 
        
        
    def testValidateListDictionaryKeys(self):
        self.assertRaises(ActivityException, self.activity.validateWindows, [{}]) 
    
    
    def testConstructorStartTime(self):
        pass
    
    
    def testConstructorDefaultDuration(self):
        pass
    
    
    def testIncrementDurationParam(self):
        pass
    
    
    def testIncrementDurationDefaultParam(self):
        pass
   

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()