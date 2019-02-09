#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Generator
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Note: 
   - Generators are a special type of iterator, and that containers like 
     'list' and 'set' are also iterable.

"""

import os
import time

# Function build and return a list ( not using generator )
# sum_of_first_n = sum( firstn(1000000) )
# The problem with following function is : it builds a full list in memory
def firstn( n ):
    num, nums = 0, []
    while num < n:
        nums.append( num )
        num += 1
    
    return nums;


# Using the generator pattern ( an iterable )
# This method is somewhat convoluted.
class Firstn( object ):
    def __init__( self, n ):
        self.n = n
        self.num, self.nums = 0, []
    
    def __iter__( self ):
        return self
    
    def __next__( self ):
        return self.next()
    
    def next( self ):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
        return cur
        else:
            raise StopIteration()
      
# sum_of_first_n = sum( Firstn(1000000) )


##-----------------------------------------------------------------------------
## Method using generator
def firstn_gen( n ):
    num = 0
    while num < n:
        yield num
        num += 1
#sume_of_first_n = sum( firstn_gen(1000000) )


# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    range()
    
    """

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
