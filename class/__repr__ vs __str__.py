#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# Comment start with #


import time, os


##-----------------------------------------------------------------------------
class ClassExample( object ): ## must be exactly "object" 
    var = 222   #<-- no 'self'

    def __init__( self, master=None ):
        self.varInit = 1 #<-- must have 'self'
        return

    def incVar(self):
        self.var += 1
        return

    def decVar(self):
        self.var -= 1
        return

    def __repr__(self):     ## repr(object)
        return "This is __repr__"
        
    def __str__(self):      ## str(object)
        return "This is __str__"
        
##-----------------------------------------------------------------------------
if __name__ == "__main__":

    c1 = ClassExample()

    c1 ## This is __repr__
    repr(c1)
    
    print(c1)   ## This is __str__
    str(c1)
    
    print (c1.var)

    # inc
    c1.incVar()
    print (c1.var)
    c1.incVar()
    print (c1.var)
    c1.incVar()
    print (c1.var)

    # dec
    c1.decVar()
    print (c1.var)
    c1.decVar()
    print (c1.var)
    c1.decVar()
    print (c1.var)
    c1.decVar()
    print(c1.var)

    print(c1.varInit)



## ----------------------------------------------------------------------------
## Resource:
"""
 - http://stackoverflow.com/questions/4015417/python-class-inherits-object 
 - https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
 - http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
"""

## ----------------------------------------------------------------------------
## Explanation:
"""
--- Python 3.x:
class MyClass(object): = new-style class
class MyClass: = new-style class (implicitly inherits from object)

--- Python 2.x:
class MyClass(object): = new-style class
class MyClass: = OLD-STYLE CLASS  <--- This is OLD-STYLE


 Python's original rendition of a class was broken in many serious ways. 
 By the time this fault was recognized it was already too late, 
 and they had to support it. 
 In order to fix the problem, they needed some "new class" style so that 
 the "old classes" would keep working 
 but you can use the new more correct version.
 
 They decided that they would use a word "object", lowercased, 
 to be the "class" that you inherit from to make a class. 
 It is confusing, but a class inherits from the class named "object" 
 to make a class but it's not an object really its a class, 
 but don't forget to inherit from object.

"""


##-----------------------------------------------------------------------------
## Terminology
##-----------------------------------------------------------------------------
"""
 - Attributes : These are the values an object has.
 - Methods : These are the functions attached to the object.
 - Instance : Whenever make a new object, it's called an "instance"
 - Class : The blueprint for an object.
 - Subclass : Base a new class off an existing class.
 
"""


