#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-


"""
 Module - json
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
"""

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - json.JSONDecodeError : class
 - json.JSONDecoder     : class
 - json.JSONEncoder     : class
 - json.dump()          : function dump (write) JSON data to file
 - json.dumps()         : function dump (write) JAON data to string
 - json.load()          : function load (read)  JSON file to Python dictionay
 - json.loadS()         : function load (read)  JSON String to Python dictionary
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
 usage : json.Attribute
 - .
 - .
"""

## ----------------------------------------------------------------------------
import os
import time
import json

## ----------------------------------------------------------------------------
def method_dump():
    """
    Put a module method here
    """
    pass
    return
    
## ----------------------------------------------------------------------------
def method_load():
    """
    json.load reads JSON data from JSON file, put it in Python format.
    """
    fp = open("json.txt", 'r')
    data = json.load(fp)
    print(type(data))
    print(data)
    for key, value in data.items():
        print(type(key))
        print(type(value))
    return
    
## ----------------------------------------------------------------------------
def method_loads():
    j = '["foo", {"bar":["baz", null, 1.0, 2]}]'    # JSON string, notice 'null' not 'None'
    l = json.loads(j)   # l is a list here

    js = '{"bar":["baz", null, 1.0, 2]}'    # JSON string, notice 'null' not 'None'
    pd = json.loads(j)   # pd is a Python dictionary here

    return

## ----------------------------------------------------------------------------
def dump_vs_dumps():
    """
    - https://stackoverflow.com/questions/36059194/what-is-the-difference-between-json-dump-and-json-dumps-in-python
    """
    pass
    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    jason.dump()
    jason.dumps()
    jason.load()
    jason.loads()
    """
    method_load()
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
 - https://docs.python.org/3/library/json.html
 -
  
"""

## ----------------------------------------------------------------------------
"""
  Note: 
    - JSON property name has to be in quotes, like {"age":32}, NOT  {age:32}
    - 



"""

