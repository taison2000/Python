#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
## 
def printInfo( name, age, zip ):
    print( "You name is ", name)
    print( "You age is ", age)
    print( "You zip is ", zip)
    print()
    return

''' Dictionay argument unpacking '''
d = { 'name':"John", 'age':25, "zip":92029 }
printInfo( **d ) ## notice 2 stars( ** ) for dictionary unpack

## notice for keyword argument, the order of dictionary can be random
d1 = { 'age':25, 'name':"John", "zip":92029 } 
printInfo( **d1 )

''' list argument unpacking '''
l = ["John", 25, 92029 ]
printInfo( *l )     # list unpack only use one (*)



## ----------------------------------------------------------------------------
def addThreeNumbers( num1, num2, num3 ):
    total = num1+num2+num3
    print( "The total is ", total )
    return

def unpack_call():
    l = [23, 24, 1223]
    addThreeNumbers( *l )

    t = (34, 190, 973)
    addThreeNumbers( *t )

    ## TypeError: addThreeNumbers() takes 3 positional arguments but 4 were given
    #t1 = (34, 190, 973, 23)
    #addThreeNumbers( *t1 )

    ## TypeError: addThreeNumbers() missing 1 required positional argument: 'num3'
    #t2 = (190, 973)
    #addThreeNumbers( *t2 )


## ----------------------------------------------------------------------------
if __name__ == "__main__":
    unpack_call()

## ----------------------------------------------------------------------------
## Resource:
"""
 - http://stackoverflow.com/questions/7527849/how-to-extract-parameters-from-a-list-and-pass-them-to-a-function-call
 - http://stackoverflow.com/questions/2921847/what-does-the-star-operator-mean-in-python?lq=1
 - 
"""
