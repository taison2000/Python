#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - format
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  format( value[, format_spec] )


"""

import os
import time

##-----------------------------------------------------------------------------
"""
NOTE:
 - '%03.2f' => '{:03.2f}'
"""

##-----------------------------------------------------------------------------
def format_align():
"""
  < : left-aligned
  > : right-aligned
  = : center-aligned
  ^ : Forces the field to be centered within the available space
"""
    pass
# 
#

def format_sign():
"""
  '+' : indicates that a sign should be used for both positive as well as negative numbers.
  '-' : indicates that a sign should be used only for negative numbers (this is the default behavior).
  ' ' : indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.
"""
    pass
    

##-----------------------------------------------------------------------------
def format_arguments_by_position():
    arg1 = 123
    arg2 = 456
    s = '{0}:{1}\n'.format('%-15s' % arg1, '%05X' % arg2)
    # {0} - First parameter of format
    # {1} - Second parameter of format

    '{0}, {1}, {2}'.format('a', 'b', 'c')   # 'a, b, c'
    '{2}, {1}, {0}'.format('a', 'b', 'c')   # 'c, b, a'
    '{2}, {2}, {2}'.format('a', 'b', 'c')   # 'c, c, c'
    '{}, {}, {}'.format('a', 'b', 'c')      # 'a, b, c'
    '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
    
    '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
    
    return s


def format_arguments_by_name():
    'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
    # 'Coordinates: 37.24N, -115.81W'
    
    coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
    'Coordinates: {latitude}, {longitude}'.format(**coord)
    # 'Coordinates: 37.24N, -115.81W'

    return


def format_arguments_by_item(): # by array indexing
    t1 = (31, 61)
    t2 = ('t2_0', 't2_1', 't2_2')
    'item_00:{0[0]}  item_01:{0[1]} item_11:{1[0]}  item_11:{1[1]} item_12:{1[2]}'.format(t1, t2)
    return

def format_with_fill_char():
    # use '*' as a fill char
    f = '{:*^30}'.format('centered')
    # '***********centered***********'

    return


def format_left_align():
    # 30 avaiable spots
    s = '{:*<30}'.format('left align')    #Fill right empty spaces with * (can only be 1 char)
    # s == 'left align********************'

    return
    
##-----------------------------------------------------------------------------
def format_right_align():
    # 30 avaiable spots
    s = '{:*>30}'.format('right align')
    # s == '*******************right align'

    return
    
##-----------------------------------------------------------------------------
def format_center_align():
    # 30 avaiable spots
    s = '{:^30}'.format('center')
    # s == '            center            '

    s1 = '---- {:^30} ----'.format('hello')
    # s1 == '----             hello              ----'

    # center align with fill character
    f = '{:*^30}'.format('centered')
    # '***********centered***********'

    return

##-----------------------------------------------------------------------------
def main():
    a = 123
    print ('%05s', a) # <- Leading empty spaces
    print ('%05s', a) # <- Leading empty spaces

    # with leading '0'
    format( 1234, '05X' )

    # 'Introducing Python' page 155
    s = '{name:s} {age:d}         {decimal:f} '.format(age=42, decimal=7.03, name='John Doe')
    # 'John Doe 42         7.030000 '

    for align, text in zip('<^>', ['left', 'center', 'right']):
        '{0:{fill}{align}16}'.format(text, fill=align, align=align)

    # format using keyword
    sf = '{0:{fill}{align}26}'.format('data', fill='-', align='^')

    return

if __name__ == "__main__":
    main()


##-----------------------------------------------------------------------------
"""
Resources:
 - See 'Format Specification Mini-Language' in Python document
 - https://docs.python.org/3/library/string.html#formatspec

"""
