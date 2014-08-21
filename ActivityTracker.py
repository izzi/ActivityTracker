'''
Created on Aug 20, 2014

@author: valeriu
'''

class Activity(object):
    '''
    Describe current state of the active desktop: for each opened windows will store window title, parent application,
    system time where this state was detected and a recorded duration of this state. Any change of the active window
    title or a switch between active windows will mark a transition to a different state.
    '''

    def __init__(self, windows):
        '''
        Saves all opened windows received by parameter and current system time
        
        :param windows: A list of dictionary, where each dictionary describe a opened window
        '''
        self._windows = windows
        
        
class SystemMonitor(object):
    '''
    Used to store the current state of the operating system.
    '''
    
    def __init__(self, providers):
        '''
        Initialize the monitor with the available providers in the operating system.
        
        :param providers: A dictionary of callable providers with keys that must match a configuration parameter of __call__.
        '''
        
        self._providers = providers
    
    def __call__(self, config):
        '''
        For each enabled configuration call the respective provider to obtain the current system state.
        
        Raises MissingProvider if there is no provider to match the enabled configuration.
        Raises UnusedProvider if one of the initiated provider do not match any configuration.
        
        :param config: A dictionary of parameters that must be retrieved from system. A false key disable the parameter.
        '''
        
        #Check for an unused provider
        for key in self._providers:
            if key not in config:                
                raise UnusedProvider(key, 'WARNING: No configuration match provider "{0}"')
        
        
        result = {}
        for key in config:
            
            # For enabled key get values from providers
            if(config[key]):
                
                if(key in self._providers):
                    
                    result[key] = self._providers[key]()
                
                else:
                    raise MissingProvider(key, 'ERROR: Missing provider for configuration "{0}"')
            else:
                
                result[key] = None
            
        return result
    
    
class ActivityException(Exception):
    """
    Main class for Activity exceptions
    """
    
    def __init__(self, value, message):
        '''
        Store state of the exception
        
        :param value:    Value that generated the exception
        :param message:  Explanation message  
        '''
        self._value = value
        self._message = message
        
    
    def __str__(self):
        return self._message.format(self._value)
           
        
class MissingProvider(ActivityException):
    '''
    There is no provider in SystemMonitor to match the configuration 
    '''
    
    
class UnusedProvider(ActivityException):
    '''
    There is no configuration match for this provider
    '''
    