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
   - A function could have more than one decorator.
    

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
        return result + 2
    return new_function

def square_it( func ):
    def new_function( *args, **kwargs ):
        result = func( *args, **kwargs )
        return result * result
    return new_function


##-----------------------------------------------------------------------------
## automatically decorator
    

"""
Function to test decorator
"""
@document_it
@square_it
def add_ints( a, b ):
    return a + b

# reverse the order of decorators
@square_it
@document_it
def add_two( a, b ):
    return a + b

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    print()
    r1 = add_ints(12, 45)
    print('r1: ', r1)
    
    print()
    r2 = add_two(12, 45)
    print('r2: ', r2)
    
    pass
    
#------------------------------------------------------------------------------
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
