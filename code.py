'''
Filename: code.py
Author: Tyler Phillips

This is an inspect-based module with resources for working with one's own code 
and accessing object metadata.
'''

# Import modules
import DBC
import inspect
import types
###############################################################################

# Global variables
CALLABLE = (types.FunctionType, types.BuiltinFunctionType, types.MethodType, 
            types.BuiltinMethodType)
###############################################################################

# Exceptions

###############################################################################

# Classes

###############################################################################

# Functions
def get_methods(target_class):
    
    '''
    Purpose:          This function finds all of the methods of a class and 
                      organizes them into a dictionary with method names as 
                      keys and the methods themselves as values.
    Parameters:
        target_class: Any class
    Returns:          A dictionary.
    '''
    
    # Test input
    DBC.check_arg_type(target_class, 'target_class', type)
    
    # Define variables
    method_list = inspect.getmembers(target_class)
    dictionary = {}
    
    # Construct dictionary
    for item in method_list:
        name = item[0]
        function = item[1]
        dictionary[name] = function
    
    # Test output
    DBC.check_output_type(dictionary, dict)
    
    # Return
    return dictionary

def get_function(level: int = 1) -> CALLABLE:
    
    '''
    Purpose:   Returns the callable function object from the specified level in
               the stack.  If no level is specified, returns the function that 
               called this one.
    Parameters:
        level: Indicates the level (index in the stack) to check.  0 will check 
               the check_all_argument_types function itself.  1 (the default 
               value) will check the function that called the 
               check_all_argument_types function.  2 will check the function 
               that called that one, and so on.
    Returns:   A callable object.
    '''
    
    DBC.check_all_argument_types()
    if not level >= 0:
        raise ValueError('level must be >= 0.')
    function = inspect.stack()[level][3]
    DBC.check_output_type()