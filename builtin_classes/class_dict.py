#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
    pyvisa.visa
    ~~~~~~~~~~~

    Module to provide an import shortcut for the most common VISA operations.

    This file is part of PyVISA.

    :copyright: 2014 by PyVISA Authors, see AUTHORS for more details.
    :license: MIT, see COPYING for more details.
"""

import os
import time

def New_vs_Copy_of_Class():
    dictOrg = {'name':'john', 'code':6734, 'dept':'sales'}
    dictNew = dict(dictOrg) # New dictionay
    dictCopy= dictOrg       # Point to same copy of 'dictOrg', dictCopy === dictOrg

def for_loop_to_access_dictionary():
    dictOrg = {'name':'john', 'code':6734, 'dept':'sales'}
    
    # get individual 'key'
    for k in dictOrg:
        print (k, ':', dictOrg[k])
    
    # get individual 'value'
    for v in dictOrg.values():
        print (v)
    
    # both key and value
    for k, v in dictOrg.items():
        print (k, v)

def main():
    # This is the main function
    tinydict = {'name':'john', 'code':6734, 'dept':'sales'}
    print (tinydict['name'])  # Print value for 'name' key
    print (tinydict['code'])  # Print value for 'code' key
    print (tinydict)          # complete dictionary
    print (tinydict.keys())   # all the keys
    print (tinydict.values()) # all the values


# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------   
if __name__ == "__main__":
    main()
    #msg = main()
    #print(msg)
    #mainloop()

