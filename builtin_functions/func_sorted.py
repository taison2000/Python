#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - sorted
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  sorted( iterable[, key] [, reverse] )


"""

import os
import time

##-----------------------------------------------------------------------------
def sorted_with_key():
    """
    Use the key as method to sort.
    """
    fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
    
    ## sorted by the length of list items
    s1 = sorted(fruits, key=len)
    # -> ['fig', 'apple', 'cherry', 'banana', 'raspberry', 'strawberry']
    
    ## sorted by uppercase
    fruits = ['strawberry', 'Fig', 'apple', 'Cherry', 'raspberry', 'banana']
    sorted_upper  = sorted(fruits, key=str.upper) # ['apple', 'banana', 'Cherry', 'Fig', 'raspberry', 'strawberry']
    sorted_normal = sorted(fruits) # ['Cherry', 'Fig', 'apple', 'banana', 'raspberry', 'strawberry']
    
    return

##-----------------------------------------------------------------------------
def main():
    a = 123
    print ('%05s', a) # <- Leading empty spaces
    print ('%05s', a) # <- Leading empty spaces

    # with leading '0'
    format( 1234, '05X' )

if __name__ == "__main__":
    main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
