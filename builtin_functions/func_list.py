#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time


"""
  list
  ~~~~~~~~~~~

  Method: append, clear, copy, count, extend, index, insert, pop, remove, reverse, sort
  
"""

## ----------------------------------------------------------------------------
## --- list methods ---
"""
#------------------------------------------------------------------------------
  Methods
  - append()
  - clear()
  - copy()
  - count() 
  - extend()
  - index()
  - insert()
  - pop()
  - remove()
  - reverse()
  - sort()
#------------------------------------------------------------------------------
"""

##-----------------------------------------------------------------------------
def method_append():
    print("\n------ list append method ------\n")
    list_1 = ['physics', 'chemistry', 2001, 1997]
    print("Original list: ", list_1)
    list_1 = ['physics', 'chemistry', 2001, 1997]
    
    list_1.append('hello world')  # add an element to the end of the list
    print("after append 'hello world'", list_1)

    return

##-----------------------------------------------------------------------------
def method_clear():
    listA = ["one", 'two', 3, 'four']
    listA.clear() ## => listA == []
    return

##-----------------------------------------------------------------------------
def method_copy():
    ## make a copy of the list
    
    listA = ["one", 'two', 3, 'four']
    
    ## if NOT copy
    a = listA
    a == listA  # True
    a is listA  # True
    
    ## make a copy
    listB = listA.copy()
    listB == listA  # True
    listB is listB  ## False <-- Notice
    
    return

##-----------------------------------------------------------------------------
def method_count():
    ## Count the number of occurances of a particular item
    list1 = [1, 3, 9, 5, 3, 3, 3, 4, 2, 9, 1]
    
    list1.count(9)  # 2
    list1.count(3)  # 4 (value 3 appear 4 times)
    list1.count(100)    # 0 (no value of 100 in the list)
    
    
##-----------------------------------------------------------------------------
def method_index():
    """
    - return the index of an element
    - cause exception if element is not in the list
    """
    lst = ['physics', 'chemistry', 2001, 1997, 'hello world']
    lst.index(2001)         # 2
    lst.index('chemistry')  # 1
    lst.index('hello world')    # 4

    lst.index('not_exist') # exception
    '''
    Traceback (most recent call last):
      File "<pyshell#236>", line 1, in <module>
        lst.index('not_exist')
    ValueError: 'not_exist' is not in list
    '''
    
    lst.index('hello world', 0, 4)  # does not include the end index (index 4 in this example)
    '''
    Traceback (most recent call last):
      File "<pyshell#30>", line 1, in <module>
        r = lst.index('hello world', 0, 4)
    ValueError: 'hello world' is not in list
    '''
    
    ## Note: only the first found index
    lst = ['a', 'b', 'c', 10, 'd', 10, 'e']
    lst.index(10) # 3, NOT 5 (only return the first encounter)
    lst.index(10, 4)    # 5, start search from index 4
    
    return

##-----------------------------------------------------------------------------
def method_insert():
    ## insert an object before an index
    
    lst = ['physics', 'chemistry', 2001, 1997, 'hello world']
    obj = ['one', 'two', 3, 'four']
    
    index = 3
    lst.insert(index, obj)
    # lst == ['physics', 'chemistry', 2001, ['one', 'two', 3, 'four'], 1997, 'hello world']
    
    
##-----------------------------------------------------------------------------
def method_pop():
    """
    ret = list.pop() #-> remove last item from the list, and return it, 
                     #   so 'ret' has the popped item.
                     
    ret = list.pop( index ) # remove the indexed item and return it.
    """
    print("\n------ list pop method ------\n")

    list_1 = ['physics', 'chemistry', 2001, 1997]
    print("Original list: ", list_1)

    ret = list_1.pop(2) # remove element with specified index, return the removed element
    print ("after pop(2)   ", list_1)   # ['physics', 'chemistry', 1997]
    print("returned value: ", ret)      # 2001

    ## 
    list_1 = ['physics', 'chemistry', 2001, 1997]
    print("\nOriginal list: ", list_1)

    ret = list_1.pop() # remove last element when no index specified, return the removed element
    print ("after pop()    ", list_1)
    print("returned value: ", ret)

    return

##-----------------------------------------------------------------------------
def method_remove():
    """
    Remove the fist encountered element value, won't return anything.
    """

    l = ['one', 'two', 'three']
    l.remove('three') # => ['one', 'two']

    ## multipel same value, ONLY the first one will be removed
    l = ['one', 'two', 'three', 'four', 'three']
    l.remove('three') # => ['one', 'two', 'four', 'three']

    l = ['one', 'two', 3, 'four', 3]
    l.remove(3) #=> ['one', 'two', 'four', 3]
    l.remove(3) #=> ['one', 'two', 'four']

    return

##-----------------------------------------------------------------------------
def method_reverse():
    ## mirror (or flip) the list, last item becomes the first one
    
    list1 = ['aa', 12, 'bb', [2014, '01', 31]]
    list1.reverse() # => list1==[[2014, '01', 31], 'bb', 12, 'aa']

    list1 = ['aa', 12, 'bb', [2014, '01', 31]]
    list1[3].reverse() # => list1==['aa', 12, 'bb', [31, '01', 2014]]

    return

##-----------------------------------------------------------------------------
def method_sort():
    list1 = [1, 3, 9, 5, 4, 2, 1]
    
    list1.sort()    # [1, 1, 2, 3, 4, 5, 9]
    
    list1.sort(reverse=True)    # [9, 5, 4, 3, 2, 1, 1]
    
    
##-----------------------------------------------------------------------------
def convertListToTuple ():
    l = [0x35, 0xff, 'This is a list']
    t = tuple( l )
    print( t )

##-----------------------------------------------------------------------------
def convertTupleToList ():
    t = (0x35, 0xff, 'This is a list')
    l = list( t )
    print( l )

##-----------------------------------------------------------------------------
def convert_TupleOfTuples_to_ListOfLists ():
    t1 = (
        ('00', '01', '02', '03'),
        ('10', '11', '12', '13'),
        ('20', '21', '22', '23'),
        ('30', '31', '32', '33'))

    l1 = [list(i) for i in t1]  # convert
    """" Result =>
    l1==[
        ['00', '01', '02', '03'], 
        ['10', '11', '12', '13'], 
        ['20', '21', '22', '23'], 
        ['30', '31', '32', '33']]
    """

    print("\n------ Tuple_of_tuples 2 List_of_lists ------\n")
    print ("Tuple of Tuples : ", t1)
    print ("List of Lists   : ", l1)


def convert_ListOfLists_to_TupleOfTuples ():
    l1 = [
        [1, 2, 1, 2],
        [2, 3, 4, 5],
        [3, 4, 5, 6],
        [4, 5, 6, 7]]

    t1 = [tuple(i) for i in l1]  # convert

    print("\n------ List_of_lists 2 Tuple_of_tuples ------\n")
    print ("List of Lists   : ", l1)
    print ("Tuple of Tuples : ", t1)


# ------------------------------------------------------------------------------
# Main - This is the main function
# ------------------------------------------------------------------------------
def main():
    convert_TupleOfTuples_to_ListOfLists()
    convert_ListOfLists_to_TupleOfTuples()
    method_pop()
    method_append()

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


"""
  Note: 
    - [1, 2] in [1, 2, 3, 4] => return False
    - 

"""
