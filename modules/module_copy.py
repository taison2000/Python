#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - copy
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - copy.copy()
 - copy.deepcopy()
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : copy.Attribute
 - .Error
"""

## ----------------------------------------------------------------------------
import os
import time
import copy

## ----------------------------------------------------------------------------
class Bus:
	def __init__(self, passengers = None):
		if passengers is None:
			self.passengers = []
		else:
			self.passengers = list(passengers)
            
	def pick(self, name):
		self.passengers.append(name)
        
	def drop(self, name):
		self.passengers.remove(name)
        
def DeepCopy_vs_ShallowCcopy():
    """
    Put a module method here
    """
    
    bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
    bus2 = copy.copy(bus1)      ## Shallow copy
    bus3 = copy.deepcopy(bus1)  ## Deep copy
    
    id(bus1), id(bus2), id(bus3)    # They all have different IDs
    
    # because bus2 is shallow copy of bus1, the Attributes(property)
    # of those two are the same
    id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
    # 42689520, 42689520, 55268176
    
    bus1.drop('Bill')
    bus1.passengers     #-> ['Alice', 'Claire', 'David']
    bus2.passengers     #-> ['Alice', 'Claire', 'David']
    bus3.passengers     #-> ['Alice', 'Bill', 'Claire', 'David']
    
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

