#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

"""
 Function - print
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    print( something )


"""

import os
import time
import sys

"""
Fluent Python Page-691
https://github.com/fluentpython/example-code/blob/master/16-coroutine/taxi_sim.py
"""

"""
Chapter 3: Compare the bit patterns of hashes
"""
MAX_BITS = len(format(sys.maxsize, 'b'))
print('%s-bit Python build' % (MAX_BITS+1))

def hash_diff(o1, o2):
    h1 = '{:>0{}b}'.format(hash(o1), MAX_BITS)
    h2 = '{:>0{}b}'.format(hash(o2), MAX_BITS)
    diff = ''.join('!' if b1 != b2 else ' ' for b1, b2 in zip(h1, h2))
    count = '!={}'.format(diff.count('!'))
    width = max(len(repr(o1)), len(repr(o2)), 8)
    sep = '-' * (width * 2 + MAX_BITS)
    return '{!r:{width}} {}\n{:{width}} {} {}\n{!r:{width}} {}\n{}'.format(
        o1, h1, ' ' * width, diff, count, o2, h2, sep, width=width)
'''
    return '{!r:{width}} {}\n{:{width}} {} {}\n{!r:{width}} {}\n{}'.format(
            o1, h1, ' ' * width, diff, count, o2, h2, sep, width=width)
'''

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
    print(hash_diff(1, 1.0))
    print(hash_diff(1.0, 1.0001))
    print(hash_diff(1.0001, 1.0002))
    print(hash_diff(1.0002, 1.0003))


##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
