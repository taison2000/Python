#!c:/Python35/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  dictionary
  ~~~~~~~~~~~~~~~~~~~~~~
"""

## ----------------------------------------------------------------------------
## --- dictionary methods ---

"""
#------------------------------------------------------------------------------
Dictionary - dict:
  Methods
  - clear()
  - copy()
  - fromkeys()
  - get() - Get the value of a key, if key not exist, return None
  - items()
  - keys()
  - move_to_end() #<- This only available to OrderedDict
  - pop()
  - popitem()
  - setdefault()
  - update()
  - values()
#------------------------------------------------------------------------------
"""

import os
import time


FIRST = "First"
LAST = "Last"
## --- Dictionary in dictionary ---
Employee = {
  "Person_1":{FIRST:'John', LAST:'Doe'},
  "Person_2":{FIRST:'Sam',  LAST:'Kool'},
  "Person_3":{FIRST:'JUn',  LAST:'Otta'},
  "Person_4":{FIRST:'Jack', LAST:'Bowen'},
}
# Employee["Person_1"][FIRST] == 'John'
# Employee["Person_3"][LAST] == 'Otta'


## ----------------------------------------------------------------------------
def method_copy():
    """
    http://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression?rq=1
    """

    # z = x + y  -- z is x and y combined; x, y are not change
    x = {'a': 1, 'b': 2}
    y = {'b': 3, 'c': 4}

    z = x.copy()    # shallow copy?
    z.update(y)

    z = {**x}   ## this will also make a copy, Python v3.5+
    
    ## PEP 448 new syntax in Python 3.5
    z = {**x, **y}  # basically unpack both x and y, then combine {} them?

    ## Note: 
    #   Because both x and y have key 'b', when combine together, 
    #   the latest 'b' key value will override the older one
    
    return


## ----------------------------------------------------------------------------
def method_pop():
    ages = {"Sam":28, "John":18, "Tom":98, "Brian":33 }

    ## pop will remove the key from dictionay and return the value
    ret = ages.pop("John")
    # ret == 18
    # ages = {"Sam":28, "Tom":98, "Brian":33 }

    return

## ----------------------------------------------------------------------------
def how_to_find_if_a_key_exists_in_dictionary():
    methods = { 
        'F01': 'A',
        'F02': 'B',
        'F03': 'C',
        }
    if 'F01' in methods:
        print("yes, F01 exists")

def how_to_find_if_a_value_exists_in_dictionary():
    methods = { 
        'F01': 'A',
        'F02': 'B',
        'F03': 'C',
        }
    if 'A' in methods.values():
        print("yes, A exists")


## ----------------------------------------------------------------------------
def list_as_dictionary_values():
    holidays = { 
        'January':['New Years day', "Lee-jackson day", "MLK Day"], 
        'October':["Halloween", "Tchies Day", "Columbus"]
    }

    holidays["January"][2]  #-> 'MLK Day'

    return

## ----------------------------------------------------------------------------
## Any immutable object can be used as dictionary key
def Immutable_As_Dictionary_Key():
    key = (44.47, -73.21)
    location = {key: 'Home Coordinates'}
    # location[(44.47, -73.21)] ==> 'Home Coordinates'

    return

## ----------------------------------------------------------------------------
## --- nested dictionary ---
def nested_dictionary():
    ## ----- 
    area = {'Bottom Corner': {'x': 500, 'y': 200}, 'Top Corner': {'x': 300, 'y': 20}}

    ## ----- 
    Cord = { "lcd":{ 'top corner':{'x':115, 'y':30}, 'bottom corner':{'x':300, 'y':100} } }
    # Cord['lcd'] == {'bottom corner': {'x': 300, 'y': 100}, 'top corner': {'x': 115, 'y': 30}}
    # Cord['lcd']['bottom corner'] == {'x': 300, 'y': 100}
    # Cord['lcd']['bottom corner']['x'] == 300

    # This is same as above
    Cord = { 
        "lcd":{ 
        'top corner': {'x':115, 'y':30}, 
        'bottom corner':{'x':300, 'y':100} 
        } 
    }
    Cord.keys()                             # dict_keys(['lcd'])
    Cord['lcd'].keys()                      # dict_keys(['bottom corner', 'top corner'])
    Cord['lcd']['bottom corner'].keys()     # dict_keys(['x', 'y'])

    ## ----- 
    lcd = {}
    lcd['Top Left'] = {}
    lcd['Bottom Right'] = {}
    lcd['Top Left']['x'] = 100
    lcd['Top Left']['y'] = 150
    lcd['Bottom Right']['x'] = 330
    lcd['Bottom Right']['y'] = 430

    print( lcd )
    print( lcd['Top Left']['x'] )
    print( lcd['Bottom Right']['x'] )

    return


def nested_dictionary2():
    cl = {
        "name":"Sam", 
        "myInfo":{
            "Age":33, 
            "zip":92129, 
            "Street Number": 8707, 
            "Street": "Broadway"
        }
    }

    print( cl ) #=> {'name': 'Sam', 'myInfo': {'Age': 33, 'Street Number': 8707, 'Street': 'Broadway', 'zip': 92129}}

    print(cl['myInfo']['Street']) #=> Broadway

    return

def extract_subset_of_a_dictionary():
    """
     - Python Cookbook : page 29
    """
    prices = {  # stock price
        'ACME': 45.23,
        'AAPL': 612.78,
        'IBM': 205.55,
        'HPQ': 37.20,
        'FB': 10.75
    }
    
    ## extract stock price greater than 200
    p1 = {key:value for key, value in prices.items() if value > 200}
    # p1 == {'AAPL': 612.78, 'IBM': 205.55}
    
    ## Make a dictionary of tech stocks
    tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
    p2 = { key:value for key,value in prices.items() if key in tech_names }
    
    return

## ----------------------------------------------------------------------------
def main():
    # This is the main function
    tinydict = {'name':'john', 'code':6734, 'dept':'sales'}
    print( tinydict['name'] )  # Print value for 'name' key
    print( tinydict['code'] )  # Print value for 'code' key
    print( tinydict )          # complete dictionary
    print( tinydict.keys() )   # all the keys
    print( tinydict.values() ) # all the values
    

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    nested_dictionary2()
    #main()
    #msg = main()

