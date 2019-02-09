#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python : __all__
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

''' __all__ list of variable or functions that can be imported 
    by other Python files
'''
__all__ = ['yes_func', 'yes_variable' ]


yes_variable = "yes import variable"
no_variable = "no import variable"


def yes_func():
    print('yes func')
    
def no_func():
    print('no func')
    
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
Note: 
  - No ++ or --, use a+=1 or a-=1 
  - print ("Variable %d", %Val)
    print ("Variable %d %d", % (Val1, Val2))
  - Syntax Tip : line breaks are ignored inside pairs of [], {}, or ().
    So building multiline lists, liscomps, genexps, dictionaries and the like no need
    no need to use \ for line continuation escape
  - 
"""


# -----------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# -----------------------------------------------------------------------------

##-----------------------------------------------------------------------------
"""
Resources:
 - http://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
 - 

"""


'''
3 single quote string
'''
