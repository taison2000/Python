#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-
import os
import time


## ----------------------------------------------------------------------------
"""
  Python : copyreg, copy, pickle
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import copyreg, copy, pickle

## ----------------------------------------------------------------------------
class C(object):
	def __init__(self, a):
		self.a = a
        
def pickle_c( c ):
	print('pickling a C instance ...')
	return C, (c.a,)
    


# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    
    """
    
    copyreg.pickle(C, pickle_c)
    
    c = C(12)
    
    d = copy.copy(c)    # pickling a C instance ...
    
    p = pickle.dumps(c) # pickling a C instance ...
    
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
 - https://docs.python.org/3/library/copyreg.html
 - https://docs.python.org/3/library/pickle.html#module-pickle
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
