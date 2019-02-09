#!usr/bin/env python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  The ctypes library includes datatypes for passing data to DLLs
  For instance, c_int to pass integer pointers

"""

## ----------------------------------------------------------------------------
## simpledll.dll
"""
simpledll.dll is created by LabWindows/CVI that exports a single function 
called addNumbers. This function uses the cdecl calling convention and 
has the following four parameters and return value:

int addNumbers (int x, int y, int* sum, char *string)
{
  *sum = x+y;
  strcpy (string, "Hello World");
  return 0;
}
"""

import os
import time

''' Here is the ctypes import '''
from ctypes import *


# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  ## Load the DLL
  dll = cdll.LoadLibrary( "SimpleDLL.dll")

  x = 254
  y = 365

  # Create sum as a c style integer
  sum = c_int(0)
  #string = create_string_buffer( "", 20 )
  string = create_string_buffer( 20 )

  # Function prototype: int addNumbers( int x, int y, int *sum, char *string)

  # Call the function
  # Pass pointers using the byref keyword
  returnValue = dll.addNumbers( x, y, byref(sum), byref(string) )

  # Print Results
  print( "Sum:", sum, '\n')
  print( "String: ", repr(string.raw), '\n')
  print( "ReturnValue: ", returnValue, '\n')


# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	main()


## ----------------------------------------------------------------------------
"""
Source:
  http://www.ni.com/white-paper/8911/en/

"""

'''
3 single quote string
'''

## ----------------------------------------------------------------------------
## create_string_buffer
## ----------------------------------------------------------------------------
"""

from ctypes import *
p = create_string_buffer(3)            # create a 3 byte buffer, initialized to NUL bytes
print(sizeof(p), repr(p.raw))
#--> 3 b'\x00\x00\x00'

p = create_string_buffer(b"Hello")     # create a buffer containing a NUL terminated string
print(sizeof(p), repr(p.raw))
#--> 6 b'Hello\x00'
print(repr(p.value))
#--> b'Hello'

p = create_string_buffer(b"Hello", 10) # create a 10 byte buffer
print(sizeof(p), repr(p.raw))
#--> 10 b'Hello\x00\x00\x00\x00\x00'
p.value = b"Hi"
print(sizeof(p), repr(p.raw))
#--> 10 b'Hi\x00lo\x00\x00\x00\x00\x00'

"""