#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - zip
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  zip( something )


"""

import os
import time


##-----------------------------------------------------------------------------
def function_zip():
    x = [1, 2, 3]
    y = [4, 5, 6]

    zipped = zip(x, y)  # zipped == <zip object at 0x02E45580>

    type (zipped)   #-> <class 'zip'>

    list( zipped )  #-> [(1, 4), (2, 5), (3, 6)]

    x2, y2 = zip(*zip(x, y))
    # x2==(1, 2, 3) -> tuple
    # y2==(4, 5, 6) -> tuple

    x==list(x2) #-> True
    y==list(y2) #-> True

    return s

def zip_two_different_length_list():
    """ If zip two different length lists, 
    iterator stops at the shortest input.
    """
    
    x = [1, 2, 3]
    y = ['one', 'two', 'three', 'four', 'five']

    xy = zip(x, y)  # xy == <zip object at 0x02E45580>
    yx = zip(y, x)  # yx == <zip object at 0x02F38170>

    type (xy)   #-> <class 'zip'>

    list( xy )  #-> [(1, 'one'), (2, 'two'), (3, 'three')]
    list( yx )  #-> [('one', 1), ('two', 2), ('three', 3)]
    
    x2, y2 = zip(*zip(x, y))
    # x2==(1, 2, 3) -> tuple
    # y2==('one', 'two', 'three') -> tuple - notice the length cut down

    x==list(x2) #-> True
    y==list(y2) #-> False - length cut down

    return s

def zip_more_iterables():
    x = [1, 2, 3]
    y = ['one', 'two', 'three', 'four', 'five']
    z = (111, 222, 333, 444, 555, 666, 777, 888)
    xyz = zip(x, y, z)  # <zip object at 0x03180CD8>
    lxyz = list(xyz)    # [(1, 'one', 111), (2, 'two', 222), (3, 'three', 333)]
    
##-----------------------------------------------------------------------------
def main():
    function_zip()

if __name__ == "__main__":
    main()


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
