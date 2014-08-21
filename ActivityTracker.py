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

    def __init__(self, window_list):
        '''
        Saves all opened windows received by parameter and current system time
        
        :param windows: A list of dictionary, where each dictionary describe a opened window
        '''
        self._window_list = self.validateWindows(window_list)
        
        
    def validateWindows(self, windows_list):
        '''
        Validate if the parameter is a list of dictionaries which describes all current opened windows on the active
        desktop. Each dictionary must contain mandatory keys: Title, Application, Active.
        
        :param windows: A list of dictionary for validation. Empty list pass the validation.
        '''
        mandatory_key_list = ["Title", "Application", "Active"]
        
        if type(windows_list) is list:
            
            for window in windows_list:
                
                if type(window) is dict:
                    # Check for mandatory keys
                    for mandatory_key in mandatory_key_list:
                        if mandatory_key not in window.keys():
                            
                            raise MissingMandatoryKeyException(mandatory_key, 'ERROR: Mandatory key "{0}" expected for each dictionary in window list')
                                        
                else:
                    raise ParamaterDictionaryListException(0, "ERROR: A list of dictionaries was expected as parameter")
        
        else:
            raise ParamaterDictionaryListException(0, "ERROR: A list of dictionaries was expected as parameter")
        
        return windows_list
        
        
        
        
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
        
        Raises MissingProviderException if there is no provider to match the enabled configuration.
        Raises UnusedProviderException if one of the initiated provider do not match any configuration.
        
        :param config: A dictionary of parameters that must be retrieved from system. A false key disable the parameter.
        '''
        
        #Check for an unused provider
        for key in self._providers:
            if key not in config:                
                raise UnusedProviderException(key, 'WARNING: No configuration match provider "{0}"')
        
        
        result = {}
        for key in config:
            
            # For enabled key get values from providers
            if(config[key]):
                
                if(key in self._providers):
                    
                    result[key] = self._providers[key]()
                
                else:
                    raise MissingProviderException(key, 'ERROR: Missing provider for configuration "{0}"')
            else:
                
                result[key] = None
            
        return result
  
    

#=======================================================================
#                             EXCEPTIONS 
#=======================================================================

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


 
        
class MissingProviderException(ActivityException):
    '''
    There is no provider in SystemMonitor to match the configuration 
    '''
    
    
class UnusedProviderException(ActivityException):
    '''
    There is no configuration match for this provider
    '''


class MissingMandatoryKeyException(ActivityException):
    '''
    Dictionary must contain a mandatory key
    '''

    
class ParamaterDictionaryListException(ActivityException):
    '''
    Parameter must be of type list and contain only dictionaries
    '''
    