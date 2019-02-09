#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  List Comprehensions
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  

"""

import os
import time

## ----------------------------------------------------------------------------
def list_comprehensions_example_1():
    symbols = '$¢£¥€¤'
    codes = [ord(symbol) for symbol in symbols]
    print(codes)  # [36, 162, 163, 165, 8364, 164]

    """ Normal code
    symbols = '$¢£¥€¤'
    codes = []
    for symbol in symbols:
        codes.append(ord(symbol))
    """

    return

def list_comprehensions_example_2():
    """
    Fluent Python - page 22
    """
    x = 123
    dummy = [x for x in 'ABC'] # dummy == ['A', 'B', 'C']
    return

def list_comprehensions_example_3():
    items = ( 
        (2, (2, 5), 'First'), 
        (1, (2, ), 'second'), 
        (3, (6, 4, 5), 'Third'),
    )
    
    new_list = [ i[1] for i in items ]  # [(2, 5), (2,), (6, 4, 5)]
    
    new_tuple = ( i[1] for i in items ) # generator object (not tuple?)
    
    new_set = { i[1] for i in items }   # set : {(2,), (2, 5), (6, 4, 5)}
    
    return

def list_comprehensions_example_4():
    """
    nested list comprehension
    """
    iter_a = [1, 2, 3]
    iter_b = ['a', 'b', 'c', 'd']
    ll = [(a, b) for a in iter_a for b in iter_b]
    [(1, 'a'), (1, 'b'), (1, 'c'), (1, 'd'), 
     (2, 'a'), (2, 'b'), (2, 'c'), (2, 'd'), 
     (3, 'a'), (3, 'b'), (3, 'c'), (3, 'd')]

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    - range()
    """

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    #msg = main()
    #print(msg)


##-----------------------------------------------------------------------------
"""
Note: 
  - No ++ or --, use a+=1 or a-=1 
  - print ("Variable %d", %Val)
    print ("Variable %d %d", % (Val1, Val2))


"""


# -----------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# -----------------------------------------------------------------------------

##-----------------------------------------------------------------------------
"""
Resources:
 - https://docs.python.org/3/tutorial/datastructures.html#tut-listcomps
 - https://www.digitalocean.com/community/tutorials/understanding-list-comprehensions-in-python-3

"""


'''
3 single quote string
'''
