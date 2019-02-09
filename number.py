#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  Number
  ~~~~~~~~~~~

"""

import os
import time
import math
  # math.e  : 2.718281828459045
  # math.pi : 3.141592653589793

def bin_hex_oct():
  a = bin(1234) # '0b10011010010'; <class 'str'>
  b = hex(1234) # '0x4d2';  <class 'str'>
  c = oct(1234) # '0o2322'; <class 'str'>
  
  return
  
def function_int():
  a = int('0100')     # a==100
  b = int('0100', 8)  # b==64
  c = int('0100', 2)  # c==4
  d = int('0100', 4)  # d==16
  e = int('0100', 16) # d==256
  
  f = int('0x40', 16) # f==64
  
  return;
  
def number_represent():
  i=123   # integer
  
  ## octal
  # starts with 0o or 0O (zero follow with letter 'o' or 'O')
  # valid digits are from 0 to 7 ( 0o8 would "SyntaxError: invalid token")
  oct1 = 0o123 # octal
  oct2 = 0O123 # octal
  
  ## binary
  # 0b102110  -> SyntaxError: invalid syntax
  a = 0b101110 #-> a==46; type(a)==<class 'int'>
  
  ## hexadecimal
  b = 0xf3bd2 #-> type(b)==<class 'int'>
  
  return;
  
# ------------------------------------------------------------------------------
# Main program - This is the main function
# ------------------------------------------------------------------------------
def main():
  a = 5.7
  b = int(a)  #-> b==5
  c = float(100)  #-> c==100.0
  d = complex(4)  #-> d==(4+0j)
  e = complex(3, 4) #-> e==(3+4j)
  
  
# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------      
if __name__ == "__main__":
	main()
  #msg = main()
  #print(msg)
  #mainloop()
  

##-----------------------------------------------------------------------------
"""
Resources:
 - http://www.java2s.com/Tutorials/Python/Data_Types/How_to_create_integer_in_Python_octal_binary_hexadecimal_and_long_integer.htm
 - Convert string to bytearray:
  http://stackoverflow.com/questions/5649407/hexadecimal-string-to-byte-array-in-python
  

"""

  

"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""


# ------------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# ------------------------------------------------------------------------------      
"""
http://stackoverflow.com/questions/419163/what-does-if-name-main-do

  When the Python interpreter reads a source file, it executes all of the code
  found in it. Before executing the code, it will define a few special variables. 
  For example, if the python interpreter is running that module (the source file)
  as the main program, it sets the special __name__ variable to have a value
  "__main__". If this file is being imported from another module, 
  __name__ will be set to the module's name.

  In the case of your script, let's assume that it's executing as the main 
  function, e.g. you said something like python threading_example.py on the 
  command line. After setting up the special variables, 
  it will execute the import statement and load those modules. 
  It will then evaluate the def block, creating a function object and 
  creating a variable called myfunction that points to the function object.
  It will then read the if statement and see that __name__ does equal 
  "__main__", so it will execute the block shown there.

  One of the reasons for doing this is that sometimes you write a module 
  (a .py file) where it can be executed directly. Alternatively, it can also
  be imported and used in another module. By doing the main check, 
  you can have that code only execute when you want to run the module as 
  a program and not have it execute when someone just wants to import 
  your module and call your functions themselves.

"""