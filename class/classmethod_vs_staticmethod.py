#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# Comment start with #


import time, os

#------------------------------------------------------------------------------
# Basically @classmethod makes a method whose first argument is the class 
#  it's called from (rather than the class instance), 
#  @staticmethod does not have any implicit arguments
#
# Both @classmethod and @staticmethod can be called from class or instance.
#  @staticmethod knows nothing about the class nor the instance
#  @classmethond has the class object.
#
# @staticmethod put into the class simply it is logical tie to the class.
#


#------------------------------------------------------------------------------
"""
@staticmethod
    Neither self (the object instance) nor  cls (the class) is 
    implicitly passed as the first argument. 
    They behave like plain functions except that you can call them from 
    an instance or the class
    
  for example : 
    class : MyClass
    instance : myInstance
    staticmethod : foo
     OK : MyClass.foo()
     OK : myInstance.foo()
"""

##-----------------------------------------------------------------------------
class Kls( object ): ## must be exactly "object" 

    def foo( self, x ): # object instance is passed in as first argument
        print( "executing foo( %s, %s)"%(self, x) )
  
    @classmethod
    def class_foo( cls, x ): # class is passed in as first argument
        print("Executing class_foo( %s, %s )"%(cls, x) )
    
    @staticmethod
    def static_foo( x ): # no class nor object instance is implicitly passed in as first argument
        print( "executing static_foo( %s )"%x )
        
##-----------------------------------------------------------------------------
if __name__ == "__main__":

    a = Kls()
    
    a.static_foo(123)
    # executing static_foo( 123 )
    
    a.foo(123)
    # executing foo( <__main__.Kls object at 0x02F14490>, 123)
    
    a.class_foo(123)
    # Executing class_foo( <class '__main__.Kls'>, 123 )


## ----------------------------------------------------------------------------
## Resource:
"""
 - http://stackoverflow.com/questions/4015417/python-class-inherits-object 
 - https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html
 - http://stackoverflow.com/questions/54867/what-is-the-difference-between-old-style-and-new-style-classes-in-python
 - http://stackoverflow.com/questions/136097/what-is-the-difference-between-staticmethod-and-classmethod-in-python
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


