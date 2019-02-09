#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/Python34

# -*- coding: utf-8 -*-

##-----------------------------------------------------------------------------
class Example():
    Value = 'Class Variable'

    def __init__( self, value="Hello" ):
        self.Value = value
        return;

    def increment_class_variable(self):
        Value += 1  ## UnboundLocalError: local variable 'Value' referenced before assignmen
#
c1 = Example('instance 1001')   # c1.Value == 'instance 1001'
c2 = Example('instance 2002')   # c2.Value == 'instance 2002'
Example.Value # 'Class Variable'


class classExample():
    var = 222   #<-- no 'self'

    def __init__( self, master=None ):
        self.varInit = 1 #<-- must have 'self'
        return;
    
    def incVar(self):
        self.var += 1
        return;

    def decVar(self):
        self.var -= 1
        return;


if __name__ == "__main__":
    class1 = classExample()

    print (class1.var)
    class1.incVar()
    print (class1.var)
    class1.incVar()
    print (class1.var)
    class1.incVar()

    print (class1.var)
    class1.decVar()
    print (class1.var)
    class1.decVar()
    print (class1.var)
    class1.decVar()
    print (class1.var)
    class1.decVar()

    print(class1.varInit)
    print(class1.var)
    
    print( "Class Example 02 output : ")
    class2 = classExample_02()
    print( class2.Value )

    class_2 = classExample_02(1234567)
    print( class_2.Value )


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
