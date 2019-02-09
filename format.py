# -*- coding: utf-8 -*-
"""
    Python 
    ~~~~~~~~~~~

    Module to provide an import shortcut for the most common VISA operations.

    This file is part of PyVISA.

    :copyright: 2014 by PyVISA Authors, see AUTHORS for more details.
    :license: MIT, see COPYING for more details.
"""

import os
import time

def by_position():
    '{0}, {1}, {2}'.format('a', 'b', 'c') # {0}<-'a' first parameter, {1}<-'b' second parameter
    # 'a, b, c,'
    '{}, {}, {}'.format('a', 'b', 'c')
    # 'a, b, c,'
    
    ## unpacking argument sequence
    '{2}, {1}, {0}'.format(*'abc')
    # 'c, b, a'
    
    ## arguments' indices can be repeated
    '{0} {1} {0}'.format('hello', 'world')
    #'hello world hello'
    
    
    return

def by_name():
    "{greeting!s:20}{name!s:15}".format(greeting="hello", name="John")
    # 'hello               John           '

    "{greeting!s:20}{name!s:15}{age:30}".format(greeting="hello", name="John", age=45)
    # 'hello               John                                       45'


## ----------------------------------------------------------------------------
def format_para():
    i = 123; 
    j = 456;
    s = '{0}:{1}\n'.format('%-15s'%i, '%02X'%j)
    # {0} - First parameter of format
    # {1} - Second parameter of format

    s1 = "{2} {1} {0} {3}".format( "going", "is", "what", 'on?' )
    # {2}=='what' {1}=='is' {0}=='going' {3}=='on'
    # => s1 == 'what is going on?'

    return s

def main():
    # format data type 'str'
    format( 1234, '5X' )  # '  4D2' Capital
    format( 1234, '5x' )  # '  4d2'

    # with leading '0'
    format( 1234, '05X' ) # '004D2'
    format( 1234, '05x' ) # '004d2'

    return;

## ----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    #msg = main()
    #print(msg)
    #mainloop()


##-----------------------------------------------------------------------------
"""
Resources:
 - https://docs.python.org/3.5/library/string.html#formatspec
 - 

"""
