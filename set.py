#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time


"""
  set
  ~~~~~~~~~~~

  Method: add, clear, copy, difference, difference_update, discard, 
    intersection, intersection_update, isdisjoint, issubset, issuperset, 
    pop, remove, symmetric_difference, symmetric_difference_update,
    union, update
  
"""

## ----------------------------------------------------------------------------
## --- set methods ---
"""
#------------------------------------------------------------------------------
  Methods
  - add()
  - clear()
  - copy()
  - difference() 
  - difference_update()
  - discard()
  - intersection()
  - intersection_update()
  - isdisjoint()
  - issubset()
  - issuperset()
  - pop()
  - remove()
  - symmetric_difference()
  - symmetric_difference_update()
  - union()
  - update()
#------------------------------------------------------------------------------
"""

##-----------------------------------------------------------------------------
def method_add():
  print("\n------ set add method ------\n")
  set_1 = {'physics', 'chemistry', 2001, 1997}
  print("Original set: ", set_1)
  set_1 = ['physics', 'chemistry', 2001, 1997]
  
  set_1.add('hello world')  # add an element to the end of the set
  print("after append 'hello world'", set_1)
  
  return

##-----------------------------------------------------------------------------
def method_clear():
  setA = ["one", 'two', 3, 'four']
  setA.clear() ## => setA == []
  return
  
##-----------------------------------------------------------------------------
def method_pop():
  print("\n------ set pop method ------\n")
  
  set_1 = ['physics', 'chemistry', 2001, 1997]
  print("Original set: ", set_1)
  
  ret = set_1.pop(2) # remove element with specified index, return the removed element
  print ("after pop(2)   ", set_1)
  print("returned value: ", ret)

  ## 
  set_1 = ['physics', 'chemistry', 2001, 1997]
  print("\nOriginal set: ", set_1)
  
  ret = set_1.pop() # remove last element when no index specified, return the removed element
  print ("after pop()    ", set_1)
  print("returned value: ", ret)
  
  return

##-----------------------------------------------------------------------------
def method_remove():
  """
  Remove the fist encountered element value
  """
  
  s = {'one', 'two', 'three'}
  s.remove('three') # => ['one', 'two']
  
  ## multipel same value, the first one will be removed
  s = ['one', 'two', 'three', 'four', 'three']
  s.remove('three') # => ['one', 'two', 'four', 'three']
  
  s = ['one', 'two', 3, 'four', 3]
  s.remove(3) #=> ['one', 'two', 'four', 3]
  s.remove(3) #=> ['one', 'two', 'four']
  
  return
  
##-----------------------------------------------------------------------------
def method_update():
  set1 = {'aa', 12, 'bb', 2014, '01', 31}
  
  set1.update() # => set1=={'aa', '01', 'bb', 12, 2014, 31}
  
  return
  

##-----------------------------------------------------------------------------
def convertListToTuple ():
  l = [0x35, 0xff, 'This is a set']
  t = tuple( l )
  print( t )

##-----------------------------------------------------------------------------
def convert_tuple_to_set( ):
  t = (0x35, 0xff, 'This is a set')
  s = set( t ) # {53, 'This is a set', 255}
  print( s )

##-----------------------------------------------------------------------------
def convert_TupleOfTuples_to_ListOfLists ():
  t1 = (
    ('00', '01', '02', '03'),
    ('10', '11', '12', '13'),
    ('20', '21', '22', '23'),
    ('30', '31', '32', '33'))
  
  l1 = [set(i) for i in t1]  # convert
  """" Result =>
  l1==[
    ['00', '01', '02', '03'], 
    ['10', '11', '12', '13'], 
    ['20', '21', '22', '23'], 
    ['30', '31', '32', '33']]
  """
  
  print("\n------ Tuple_of_tuples 2 List_of_sets ------\n")
  print ("Tuple of Tuples : ", t1)
  print ("List of Lists   : ", l1)

  
def convert_ListOfLists_to_TupleOfTuples ():
  l1 = [
    [1, 2, 1, 2],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]]
  
  t1 = [tuple(i) for i in l1]  # convert
  
  print("\n------ List_of_sets 2 Tuple_of_tuples ------\n")
  print ("List of Lists   : ", l1)
  print ("Tuple of Tuples : ", t1)
 
  
# ------------------------------------------------------------------------------
# Main - This is the main function
# ------------------------------------------------------------------------------
def main():
  convert_TupleOfTuples_to_ListOfLists()
  convert_ListOfLists_to_TupleOfTuples()
  method_pop()
  method_add()

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------
if __name__ == "__main__":
	main()
else:
    pass

"""
  Note: 
    - set has no order
    - element in a set can not be reference by index
    - set can not be nested (no set in a set), because a set is unhashable
    - no list in a set, set1 = {'aa', 12, 'bb', [2014, '01', 31]} => TypeError: unhashable type: 'list'
    - tuple in a set is ok => s = {'one', 'two', (1, 2)}
    - 

"""
