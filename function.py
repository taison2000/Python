
import os

## ----------------------------------------------------------------------------
def VariableArguments_and_default_argument( *arg, delay=50 ):
    """
    - VariableArguments_and_default_argument( 1, 2, 3, 4, 5, 6 )
    - VariableArguments_and_default_argument( 1, 2, 3, 4, 5, 6, 7, 8, 9, delay=222 )
    - VariableArguments_and_default_argument( )
    """

    # How many arguments in arg
    print( len(arg) )

    print( arg )
    print( delay )

    return

## ----------------------------------------------------------------------------
def DefaultParameter(value=30):
    """
    Function parameter with default value
    """
    return (value*3)



## ----------------------------------------------------------------------------
## Beware: Mutable Types as Parameter Defaults
#  When call this function, if no argument is provided for 'passengers'
#  The default list will be used, different function calls will refer to same
#  referenced list.
def add_name( name, passengers=[] ):
	passengers.append(name)
	return passengers

# the following function calls will return a same reference list 
# because using the default mutable list
name_list1 = add_name('John')
name_list2 = add_name('Joe')
## name_list1 is name_list2 -> ['John', 'Joe']




## ----------------------------------------------------------------------------
if __name__=='__main__':

    # 
    a = DefaultParameter(13)
    print(a)

    # Function call by using default value
    b = DefaultParameter()
    print(b)


## ----------------------------------------------------------------------------
## Resource:
"""
 - 
 
"""
