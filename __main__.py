#!/usr/bin/python
# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~
  What is the execution order

"""

import os
import time

## ----------------------------------------------------------------------------
print("This is OUTSIDE of __main__ code ")

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    print ("Call by __main__")
    return

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("This is INSIDE block of __main__ code ")
    main()
    #msg = main()
    #print(msg)
    #mainloop()

## ----------------------------------------------------------------------------
print('This is AFTER ( if __name__ == "__main__" ) code ')


## ----------------------------------------------------------------------------


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""


# -----------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# -----------------------------------------------------------------------------
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

'''
3 single quote string
'''
