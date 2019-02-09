#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - map
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    map( function, iterable, ... )

    equivalent of map implementation
    def map( func, iterable ):
        for i in iterable:
            yield func(i)

"""

import os
import time

##-----------------------------------------------------------------------------
def map_lambda():
    list_numbers = [4, 1, 9, 11]
    result = map(lambda x: x**2, list_numbers)
    # result == <map object at 0x02D53CD0>
    print(list(result)) # [16, 1, 81, 121]
    
    return

def map_lambda():
    list_numbers1 = [4, 1, 9, 11]
    list_numbers2 = [3, 23, 5, 4]
    ## Note: if two lists have different length, map will stop at the shortest one.
    
    ## Note: since lambda here takes 2 arguments, so provide 'list_numbers1' and 'list_numbers2'
    result = map(lambda x, y: x+y, list_numbers1, list_numbers2)    
    # result == <map object at 0x02D53CD0>
    
    print(list(result)) # [7, 24, 14, 15], number member added individually of the two list numbers. Not append two lists.
    
    return


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
