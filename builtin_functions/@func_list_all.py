#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 List all Built-in Functions (total:68)
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    abs()
    all()
    any()
    ascii()
    
    bin()
    bool()
    bytearray()
    bytes()
    
    callable()
    chr()
    classmethod()
    compile()
    complex()
    
    delattr()
    dict()
    dir()
    divmod()
    
    enumerate()
    eval()
    exec()
    
    filter()
    float()
    format()
    frozenset()
    
    getattr()
    globals()
    
    hasattr()
    hash()
    help()
    hex()
    
    id()
    input()
    in()
    isinstance()
    issubclass()
    iter()
    
    len()
    list()
    locals()
    
    map()
    max()
    memoryview()
    min()
    
    next()
    
    object()
    oct()
    open()
    ord()
    
    pow()
    print()
    property()
    
    range()
    repr()
    reversed()
    round()
    
    set()
    setattr()
    slice()
    sorted()
    staticmethod()
    str()
    sum()
    super()
    
    tuple()
    type()
    vars()
    
    zip()
    
    __import__()
"""

import os
import time

##-----------------------------------------------------------------------------
def abs_desc():
    """ abs() : absolute value
    """
    return 

##-----------------------------------------------------------------------------
def function_getattr():
    """
    getattr( object, name[, default] )
      Return the value of the named attribute of object.
      Name must be a string. 
      If the string is the name of one of the object's attributes, the result
      is the value of that attribute.
      For example, getattr(x, 'foobar') is equivalent to x.foobar.
      If the named attribute does not exist, default is returned if provided,
      otherwise 'AttributeError' is raised.
    """
    
    class Foo(object):
        def __init__():
            a, b = 'A', 'B'
            
        def bar():
            print("This is the bar method")
            

    result = getattr(Foo, 'bar')
    result()    # "This is the bar method"
    
    r = getattr(Foo, 'Not_implemented') # AttributeError (exception)
    r = getattr(Foo, 'Not_implemented', None)   # r == None
    r = getattr(Foo, 'Not_implemented', 'hello')   # r == 'hello'
    r = getattr(Foo, 'Not_implemented', sum)   # r == sum
    
    
##-----------------------------------------------------------------------------

##-----------------------------------------------------------------------------
def function_sum():
    s = sum( [1, 2, 3, 4] ) # 10 = 1+2+3+4
    s = sum( [3, 5, 6, 9, 1] ) # 24 = 3+5+6+9+1
    
##-----------------------------------------------------------------------------
def main():
    pass
    return
    
if __name__ == "__main__":
    main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
