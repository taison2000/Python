#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python : Generator
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

def binary_join():
    a = b'\xff\xff\x3c\xc3'
    b = b'\x03\x02'
    
    # The following two statement have the same result
    c = b''.join( [a, b] )  # b'\xff\xff\x0c\xc3\x03\x02'
    d = b''.join( (a, b) )  # b'\xff\xff\x0c\xc3\x03\x02'
    
    return
    
def string_join():
    l = ['hello', 'world']
    
    s = '-'.join(l) # 'hello-world'
    ## l.join('-')
    
    return
    
def web_query_join():
    b'\x0a\x0a\x0a\x0a'.join(urllib.request.urlopen('http://data.stackexchange.com/users/7095'))    # join '\n'
    b'\x0d\x0d\x0d\x0d'.join(urllib.request.urlopen('http://data.stackexchange.com/users/7095'))    # join '\r'
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
##-----------------------------------------------------------------------------
"""
Resources:
 - https://wiki.python.org/moin/Generators
 - 

"""

##-----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Note: 
# -----------------------------------------------------------------------------
"""

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

