#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# Comment start with #

import time, os

##-----------------------------------------------------------------------------
class Example( object ):
    Value = 'Class Variable'
    
    def __init__(self, val='instance variable'):
        self.instValue = val
#end class Example
inst_1 = Example( 'instance #1')
inst_2 = Example( 'instance #2')

# to access class variable
# followin all have same id.
Example.Value
inst_1.Value
inst_2.Value
inst_1.Value is Example.Value is inst_2.Value   # True

## Note: the following does not change the class variable 'Value'
##       it create a different variable belongs to 'inst_1'
inst_1.Value = 1  

# Now Example.Value and inst_2.Value still have the same id. 
Example.Value is inst_2.Value   # True

# But inst_1 is completely different.
inst_1.Value is Example.Value is inst_2.Value   # False
inst_1.Value is Example.Value       # False
inst_1.Value is inst_2.Value        # False

# to recover original class value of inst_1.Value, run 'del inst_1.Value'
inst_1.Value is Example.Value is inst_2.Value   # True again


##-----------------------------------------------------------------------------
class ClassExample( object ): ## must be exactly "object"
    # This is class variable
    # no 'self'
    # access by class, not by a particular object instance
    value = 'Class value'
    
    def __init__(self, value='Object value'):
        #<-- Object instance variable must have 'self'
        self.value = value
        
    def get_object_value(self):
        return self.value
        
    def set_object_value(self, v):
        self.value = v
        
    def get_class_value(self):
        return ClassExample.value
        
    def set_class_value(self, v):
        ClassExample.value = v
        
# end class ClassExample

##-----------------------------------------------------------------------------
if __name__ == "__main__":

    obj1 = ClassExample()
    obj2 = ClassExample()
    
    ## Note: 
    # - Class value will be same 
    # - Object value will be different
    obj1.get_class_value() == obj2.get_class_value()    # Alway True
    
    obj1.get_object_value() == obj2.get_object_value()  # False, they could set to different values.
    

    obj1.value
    # 'Object value'
    
    ClassExample.value
    # 'Class value'

    obj1.get_class_value()
    # 'Class value'

    # 

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


