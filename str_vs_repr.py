#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python : str() vs repr() or %s vs %r
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    The %s specifier converts the object using str(), and %r converts it using repr().
"""

import os
import time

def str_vs_repr():
    """ http://stackoverflow.com/questions/6005159/when-to-use-r-instead-of-s-in-python
        For some objects such as integers, they yield the same result, 
        but repr() is special in that (for types where this is possible) 
        it conventionally returns a result that is valid Python syntax, 
        which could be used to unambiguously recreate the object it represents.
    """
    import datetime
    
    d = datetime.date.today()   # d == datetime.date(2016, 8, 19)
    
    print( str(d) ) # '2016-08-19'
    print( repr(d) )# 'datetime.date(2016, 8, 19)'
    
    print("%s"%d) # str(d)  2017-06-23
    print("%r"%d) # repr(d) datetime.date(2017, 6, 23)
    
    return
    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    - range()
    """
    pass

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
else:
    """
    Called by other module
    """
    pass


##-----------------------------------------------------------------------------
"""
Resources:
 - https://wiki.python.org/moin/Generators
 - 

"""

##-----------------------------------------------------------------------------
"""
Note: 
  - No ++ or --, use a+=1 or a-=1 
  - print ("Variable %d", %Val)
    print ("Variable %d %d", % (Val1, Val2))
  - Syntax Tip : line breaks are ignored inside pairs of [], {}, or ().
    So building multiline lists, liscomps, genexps, dictionaries and the like no need
    no need to use \ for line continuation escape
  - 
"""



'''
3 single quote string
'''
