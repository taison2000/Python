#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - bytes
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  bytes( [source[, encoding[, errors]]] )
    - immutable

"""

import os
import time

##-----------------------------------------------------------------------------
def format_para():
    i = 123; 
    j=456
    s = '{0}:{1}\n'.format('%-15s'%i, '%02X'%j)
    # {0} - First parameter of format
    # {1} - Second parameter of format

    return s

##-----------------------------------------------------------------------------
def main():
    a = 123
    print ('%05s', a) # <- Leading empty spaces
    print ('%05s', a) # <- Leading empty spaces
    
    # with leading '0'
    format( 1234, '05X' )
    
    return
    
if __name__ == "__main__":
    main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
