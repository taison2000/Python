#!/usr/bin/python
# -*- coding: utf-8 -*-

"""

"""

import os
import time

def for_with_pass():
    """
    pass statement in Python is used when a statement is required syntactically
    but you do not want any command or code to execute
    pass statement is a null operation
    """
    print ('\nfor with pass')
    for letter in 'Python':
        if letter == 'h':
            pass
            print('This is a pass block')
        print('Current Letter :', letter)

    print('good bye!')

def for_with_else():
    print ('\nFor loop with else')
    for num in range (10, 20):
        for i in range(2, num):
            if num%i == 0:
                j=num/i
                print('%d equals %d * %d' %(num, i, j))
                break
        else:
            print(num, 'is a prime number')
"""
for ... else ...
if no "break" was encountered, "else" will be executed

    for something:
        if soemthing:
            break
    else:
        do soemthing
    
    
"""
def is_prime(num):
"""
use for ... else ...
"""
    for i in range(2, num):
        if num%i == 0:
            print("%d = %d * %d" % (num, i, num/i))
            break
    else:
        print(num, 'is a prime number')

def for_loop_basic():
    # range(start, stop[, step])
    print('\nfor loop basic')
    for i in range(0, 1000, 20):
        print("Current Num : %d" % i)
        time.sleep(0.1)

# ------------------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------------------ 
def main():
# This is the main function
    for_loop_basic()
    for_with_else()
    for_with_pass()

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------  
if __name__ == "__main__":
    main()
    #msg = main()
    #print(msg)
    #mainloop()

