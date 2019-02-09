#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Decorator
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    A decorator is a function that takes one function as input and returns
    another function.
    
  Note: 
   - 
    

"""

import os
import time


##-----------------------------------------------------------------------------
'''
decorator function
'''
def document_it( func ):
    def new_function( *args, **kwargs ):
        print('Running function: ', func.__name__)
        print('Positional arguments: ', args)
        print('Keyword arguments: ', kwargs)
        result = func( *args, **kwargs )
        print('Result: ', result)
        return result
    return new_function

#------------------------------------------------------------------------------
"""
Function to test decorator
"""
def add_ints( a, b ):
    return a + b


##-----------------------------------------------------------------------------
## automatically decorator
@document_it
def add_two( a, b ):
    return a + b

@document_it
def add_two_kw( first=8, second=11):
    return first + second
    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    ## manual decorator assignment
    cooler_add_ints = document_it( add_ints )
    
    # Call the new function
    print("Manual decorator ")
    cooler_add_ints(12, 45)
    
    print("Automatic decorator")
    add_two(34, 78)
    
    pass

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()



##-----------------------------------------------------------------------------
"""
Resources:
 - https://wiki.python.org/moin/Generators

"""

##-----------------------------------------------------------------------------
"""
Note: 
  - No ++ or --, use a+=1 or a-=1 
  - print ("Variable %d", %Val)
    print ("Variable %d %d", % (Val1, Val2))

  

"""

'''
3 single quote string
'''
