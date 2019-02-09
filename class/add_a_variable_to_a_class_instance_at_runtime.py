#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# Comment start with #


import time, os

## https://rosettacode.org/wiki/Add_a_variable_to_a_class_instance_at_runtime#Python

##-----------------------------------------------------------------------------
class Empty( object ): # must be exactly "object" 
    pass
#end class Empty

e = Empty()

# If the variable (attribute) name is known at "compile" time (hard-coded
e.foo = 1

#If the variable name is determined at runtime
setattr(e, name, value)
setattr(e, 'foo', 1)


##-----------------------------------------------------------------------------
class empty_02(object):
    def __init__(this):
        this.foo = "whatever"
 
def patch_empty(obj):
    def fn(self=obj):
        print self.foo
    obj.print_output = fn
 
e = empty_02()
patch_empty(e)
e.print_output()
# >>> whatever

##-----------------------------------------------------------------------------
if __name__ == "__main__":




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


