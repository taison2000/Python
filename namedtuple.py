#!/usr/bin/python
# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""


"""

import os
import time
from collections import namedtuple

def program_data():
    ProgramDataStruct = namedtuple('program_data', 'start_time run_time delay')
    
    p1 = ProgramDataStruct(720, 10, 30)
    # program_data(start_time=720, run_time=10, delay=30)
    
    print(p1.start_time)    # 720
    print(p1.run_time)      # 10
    print(p1.delay)         # 30
    
    return
    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    NewStruct = namedtuple('CustomStruct', 'f1 f2 f3')  
    # NewStruct => <class '__main__.CustomStruct'>
    
    ns = NewStruct('f1_data', 'f2_data', 'f3_data')
    # CustomStruct(f1='f1_data', f2='f2_data', f3='f3_data')
    
    print( ns )     #==> CustomStruct(f1='f1_data', f2='f2_data', f3='f3_data')
    print( ns.f1 )  #==> f1_data
    print( ns.f2 )  #==> f2_data
    print( ns.f3 )  #==> f3_data
    
    return
    
# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()


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

http://stackoverflow.com/questions/35988/c-like-structures-in-python



"""

'''
3 single quote string
'''
