# -*- coding: utf-8 -*-
"""
    pyvisa.visa
    ~~~~~~~~~~~

    Module to provide an import shortcut for the most common VISA operations.

    This file is part of PyVISA.

    :copyright: 2014 by PyVISA Authors, see AUTHORS for more details.
    :license: MIT, see COPYING for more details.
"""

import os
import time
##-----------------------------------------------------------------------------
def setBits(number,msb,lsb,value):
	"""
	Change bits msb:lsb from teri original value in number to the new value
	"""
	mask=(2**(msb-lsb+1)-1)<<lsb
	number = number & ~mask
	number=number |(mask & (value<<lsb))
	return number

def main():
# This is the main function
  str = "hello world!"
  print (str)       # Complete string
  print (str[0])    # First character
  print (str[1:4])  # char from 2nd to 4th (note: not include str[4])
  print (str[2:])   # char from 3rd to end
  print (str*2)     # 2 times
  print (str+" I am John")  # concatenated
  
  ## what about reverser string?
  # for example str[4:1], how?
 
if __name__ == "__main__":
	main()
  #msg = main()
  #print(msg)
  #mainloop()

