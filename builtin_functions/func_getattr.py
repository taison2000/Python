#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - getattr
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    getattr( object, name[, default] )


"""

import os
import time

##-----------------------------------------------------------------------------
def getattr_general():
    a = 'hello world'
    getattr(a, '__doc__')

    return

def demo_function():
    """ This is demo for getattr() __doc__"""
    pass
    return
    
##-----------------------------------------------------------------------------
def main():
    ret = getarrt( demo_function, '__doc__')
    print( ret ) # 'This is demo for getattr() __doc__'
    
    return
    
if __name__ == "__main__":
    main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
