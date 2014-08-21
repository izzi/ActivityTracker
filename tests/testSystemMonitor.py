'''
Created on Aug 20, 2014

@author: valeriu
'''
import unittest
import random

from activitytracker import SystemMonitor, SystemMonitorError

class TestSystemMonitor(unittest.TestCase):    
     
        def provide_true(self):
            
            return True
        
        
        def setUp(self):
            
            self.allowedFields = ["BootTime", "NetworkUpload", "NetworkDownload", "Memory", "CPU", "StartTime", "ActiveWindow", "Window"]          
            self.config = {label: True for label in self.allowedFields}
            self.providers = {label: self.provide_true for label in self.allowedFields}
            self.monitor = SystemMonitor(self.providers)
            
        
        def tearDown(self):
            
            self.allowedFields = None
            self.config = None
            self.providers = None
            self.monitor = None
            
            
        def test_providers_setup(self):
            
            self.assertDictEqual(self.providers, self.monitor._providers, "Assigned providers do not match")
        
        
        def test_config_all_disabled(self):
            
            self.config = {label: None for label in self.allowedFields}
            
            self.assertDictEqual(self.monitor(self.config), self.config, "Some providers ignore provided configuration")
        
        
        def test_config_all_enabled(self):
        
            self.assertDictEqual(self.monitor(self.config), self.config, "Some providers do not run")
            
        
        def test_config_mixed(self):
            """
            Enables all fields in configuration, after that disable a random one
            """
            self.config[random.choice(self.allowedFields)] = None
        
            self.assertDictEqual(self.monitor(self.config), self.config, "Some providers ignore configuration")
            
        
        def test_config_has_no_provider(self):
            
            #Set a invalid configuration without a matching provider
            self.config["WrongConfigTest"] = True
        
            self.assertRaises(SystemMonitorError, self.monitor, self.config)
            
            
        def test_provider_has_no_config(self):
            
            #Set a invalid provider without a matching configuration
            self.providers["WrongProviderTest"] = self.provide_true
            
            self.monitor = SystemMonitor(self.providers)
        
            self.assertRaises(SystemMonitorError, self.monitor, self.config)

            
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