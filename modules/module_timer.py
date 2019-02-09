#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - timer
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - error()
 - kill_timer()
 - set_timer()
 - 
 - 
 - 
 - 
 - 
 - 
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : timer.Attribute
 - .
 - .
 - .
"""
 
## ----------------------------------------------------------------------------
import os
import time
import timer

def call_back(*args):
	print("length : ", len(args))   
	for i in range(len(args)):
		print(args[i])
    return
    
## ----------------------------------------------------------------------------
def method_set_timer():
    """
    set_timer( miliseconds, call_back_function )
        - the call back function will be passed in 2 positional arguments.
           First is timer id, the second is the processor time?
    """
    timer_id = timer.set_timer( 7000, call_back )   # run 'call_back' every 7 seconds
    
    return;
    
def method_kill_timer():
    """
    kill_timer( timer_id )
    """
    status = kill_timer( timer_id )
    # - if kill success, return True, else return False
    # - if timer_id is not valid, will have exception <KeyError: timer_id>
    
    return

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    method_Name()
    return;

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()



## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 -
 -
  
"""

## ----------------------------------------------------------------------------
"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))



"""

