#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - random
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - random.Random()
 - random.SystemRandom()
 - random.betavariate()
 - random.choice()
 - random.expovariate()
 - random.gammavariate()
 - random.gauss()
 - random.getrandbits()
 - random.getstate()
 - random.lognormvariate()
 - random.normalvariate()
 - random.paretovariate()
 - random.randint()
 - random.random()
 - random.randrange()
 - random.sample()
 - random.seed()
 - random.setstate()
 - random.shuffle()
 - random.triangular()
 - random.uniform()
 - random.vonmisesvariate()
 - random.weibullvariate()
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : random.Attribute
 - .
 - .
 - .
 - .
"""
 
## ----------------------------------------------------------------------------
import os
import time
import random

## ----------------------------------------------------------------------------
def method_choice():
    l = ['apple', 'cherry', 'banana', 'orange', 'pear']
    c = random.choice(l)
    print(c)
    
def method_getrandbits():
    """
    Put a module method here
    """
    for i in range(100):
        b = random.getrandbits(5) # 0<='b'<32 [5-bit value]
        #b = random.getrandbits(8) # 0<='b'<255 [8-bit value]
        print(b)
    return


    
def method_SystemRandom():
    """
    http://nullege.com/codes/search/random.SystemRandom
    """
    
    sys_ran = random.SystemRandom()
    
    ran_num = sys_ran.choice( [1, 2, 3, 4, 5] )
    ran_num = sys_ran.choice( range(0, 100) )

    return
    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    method_Name()
    return

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

