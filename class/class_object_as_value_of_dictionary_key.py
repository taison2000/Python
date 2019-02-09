#!/Python34/python
#!/usr/bin/Python34


##-----------------------------------------------------------------------------

class TestField( object ):
    def __init__( self, value ):
        self.clsValue = value

    def printValue( self ):
        print( self.clsValue )

if __name__ == "__main__":

    # Creat a class object named "field"
    # Initial the class attribute of "clsValue" to 345
    field = TestField( 345 )

    ''' Use the class object "field" as value of dictionary key '''
    myDict = {"One" : field }

    # Access the attribute of class using dictionary key 
    print( myDict["One"].clsValue )

    myDict["One"].printValue()

    # 
    isinstance( myDict["One"], TestField )  # True

## ----------------------------------------------------------------------------
## Resource:
"""
 - http://www.elvenware.com/charlie/development/web/Python/PythonSyntax.html#defaultParameters
 
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
