#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python : bitwise operation
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

def bitwise_on_bytes():
    """
    - No bitwise operations on 'bytes' (immutable)
    - http://stackoverflow.com/questions/22593822/doing-a-bitwise-operation-on-bytes
    """
    a, b = b'\x12', b'\x34'
    a_and_b1 = bytes( [ a[0]&b[0] ] ) # b'\x10'
    a_and_b2 = bytes(   a[0]&b[0]   ) # b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

    a, b = b'\x02', b'\x04'
    a_or_b1 = bytes( [ a[0]|b[0] ] ) # b'\x06'
    a_or_b2 = bytes(   a[0]|b[0]   ) # b'\x00\x00\x00\x00\x00\x00'

    return

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    range()
    
    """

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    #msg = main()
    #print(msg)


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""


# -----------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# -----------------------------------------------------------------------------

##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""


'''
3 single quote string
'''
