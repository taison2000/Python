#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# Comment start with #


import time, os


##-----------------------------------------------------------------------------
class A( object ): ## must be exactly "object" 

    def __init__( self ):
        self._internal = 'Internal for class A'
        self.__private = 'Private for class A'

    def _internal_method(self): ## 1 leading underscore, this hidden, but can be accessed by outside.
        self._internal = 'internal method modified'
        print("This is internal method with 1 underscore")

    def __private_method(self): ## 2 leading underscores, can not be directly accessed by object. 
        print("This is private method with 2 underscores")
        
    def public_method(self):
        print("This is public method")
        self.__private_method() ## access private functions
        print(self._internal)
        print(self.__private)
        
class B( A ):
    def __init__( self ):
        super().__init__()
        self._internal = 'internal for class B'
        self.__private = 'private for class B'  ## 2 underscore property can not be changed
        
        
##-----------------------------------------------------------------------------
if __name__ == "__main__":
    a = A()
    b = B()

    a._internal # OK, but '_internal' won't be auto complete in IDE
    # 'Internal for class A'
    b._internal
    # 'internal for class B'
    
    a.__private ## 2 underscores is private property can not be accessed outside
    '''
    Traceback (most recent call last):
      File "<pyshell#30>", line 1, in <module>
        a.__private
    AttributeError: 'A' object has no attribute '__private'
    '''

    a.public_method()
    """
        This is public method
        This is private method with 2 underscores
        Internal for class A
        Private for class A
    """
    
    b.public_method()
    """
        This is public method
        This is private method with 2 underscores
        internal for class B    ## <-- Notice only _internal can be changed from subclass
        Private for class A     ## <-- The __private can NOT be changed from subclass
    """



## ----------------------------------------------------------------------------
## Resource:
"""
 - Python Cookbook (8.5. Encapsulating Names in a Class)
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


