#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  hex() : built-in function
  ~~~~~~~~~~~
    hex(number) --> string
      Return the hexadecimal representation of an integer.

"""

import os
import time

def hex_01():
  # range(start, stop[, step])
  for i in range(0, 1000, 20):
    print("Current Num : 0x%x" % i)
    print("Current Num : 0x%X" % i)
    time.sleep(0.1)

def hex_02():
  # range(start, stop[, step])
  for i in range(0, 1000, 10):
    #print("hex Num : " + hex(i))
    print("hex Num : " , hex(i))
    time.sleep(0.1)



# ------------------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------------------
def main():
# This is the main function
  hex_01()
  hex_02()

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------      
if __name__ == "__main__":
	main()
  #msg = main()
  #print(msg)
  #mainloop()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""
