'''
Created on Aug 20, 2014

@author: valeriu
'''
import unittest
import random

from ActivityTracker import SystemMonitor, SystemMonitorException

class TestSystemMonitor(unittest.TestCase):    
     
        def provideTrue(self):
            
            return True
        
        
        def setUp(self):
            
            self.allowedFields = ["BootTime", "NetworkUpload", "NetworkDownload", "Memory", "CPU", "StartTime", "ActiveWindow", "Window"]          
            self.config = {label: True for label in self.allowedFields}
            self.providers = {label: self.provideTrue for label in self.allowedFields}
            self.monitor = SystemMonitor(self.providers)
            
        
        def tearDown(self):
            
            self.allowedFields = None
            self.config = None
            self.providers = None
            self.monitor = None
            
            
        def testProvidersSetup(self):
            
            self.assertDictEqual(self.providers, self.monitor._providers, "Assigned providers do not match")
        
        
        def testConfigAllDisabled(self):
            
            self.config = {label: None for label in self.allowedFields}
            
            self.assertDictEqual(self.monitor(self.config), self.config, "Some providers ignore provided configuration")
        
        
        def testConfigAllEnabled(self):
        
            self.assertDictEqual(self.monitor(self.config), self.config, "Some providers do not run")
            
        
        def testConfigMixed(self):
            """
            Enables all fields in configuration, after that disable a random one
            """
            self.config[random.choice(self.allowedFields)] = None
        
            self.assertDictEqual(self.monitor(self.config), self.config, "Some providers ignore configuration")
            
        
        def testConfigHasNoProvider(self):
            
            #Set a invalid configuration without a matching provider
            self.config["WrongConfigTest"] = True
        
            self.assertRaises(SystemMonitorException, self.monitor, self.config)
            
            
        def testProviderHasNoConfig(self):
            
            #Set a invalid provider without a matching configuration
            self.providers["WrongProviderTest"] = self.provideTrue
            
            self.monitor = SystemMonitor(self.providers)
        
            self.assertRaises(SystemMonitorException, self.monitor, self.config)

            
#TODO: Test each provider
#TODO: Test values of each provider
#TODO: System status: Unchanged, NewActivity, Idle
#TODO: Activity creation
#TODO: Activity to string
#TODO: Ncurses library for terminal display
#TODO: Configuration Manager
#TODO: Database backend

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()