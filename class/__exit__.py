#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# Comment start with #


import time, os


##-----------------------------------------------------------------------------
class Class__exit__( object ): ## must be exactly "object" 
    def __init__(self, greeting):
        print( greeting )
        self.value = greeting
        
    def __del__(self):
        del self
        print("__del__")
        
    def __enter__(self):
        print("This is the __enter__ code")
        return self # must have return statement, otherwise methods (for example: display) would not work.
        
    def __exit__(self, exception_type, exception_value, traceback):
        print("This is the __exit__ code")
        
    def display(self):
        print("Print something")

"""
In order for __exit__ to work properly it must have exactly three arguments: 
  exception_type
  exception_value
  traceback
The formal argument names in the method definition do not need to correspond directly to these names, 
but they must appear in this order. 
If any exceptions occur while attempting to execute the block of code nested after the with statement, 
Python will pass information about the exception into the __exit__ method. 
You can then modify the definition of __exit__ to gracefully handle each type of exception.
"""

# when this function is called, the variable 'c' 
def destructor__del__():
    c = Class__exit__("hi")

##-----------------------------------------------------------------------------
if __name__ == "__main__":

    c1 = Class__exit__('hello')

    with Class__exit__("hello world") as c:
        c.display()



## ----------------------------------------------------------------------------
## Resource:
"""
 - https://docs.quantifiedcode.com/python-anti-patterns/correctness/exit_must_accept_three_arguments.html
 - 
 - 
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


