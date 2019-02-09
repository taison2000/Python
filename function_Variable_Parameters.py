
## ----------------------------------------------------------------------------
## One(*) : This function will not take keyword argument
## Two(**): This function can take keyword argument
def nonKeywordFunc(arg1, arg2, *args): ## nonKeywordFunc(arg1=1, arg2=2, arg3=3, arg4=4)  ''' NO -> arg3 and arg4'''
    pass
def KeywordFunc(arg1, arg2, **args):   ## KeywordFunc(arg1=1, arg2=2, arg3=3, arg4=4)  ''' YES '''
    pass


## ----------------------------------------------------------------------------
# Mix non keyword arguments with keyword arguments
# The non keyword arguments must be declare first
def mix( *args, **kwargs ):
    print( len(args) )
    print( args )
    print( len(kwargs) )
    print( kwargs )

    return


## ----------------------------------------------------------------------------
"""
An asterisk(*) is placed before the variable name that will hold the 
values of all nonkeyword arguments (Tuple).
"""
def PrintInfo( arg1, *varTuple ):
    """ varTuple == Tuple """
    
    "This prints a variable passed arguments"
    print( "arg1 is : ", arg1 )

    for var in varTuple: ## Tuple
        print( var )
    print( 'Variable:', varTuple )
    return
    
def PrintInfo_Test():
    print( "\nParameter List : 10" )
    PrintInfo( 10 );
    print( "\nParameter List : 34, 38, 29, 0, 34, 1" )
    PrintInfo( 34, 38, 29, 0, 34, 1 );
    print( "\nParameter List : 34, 38, 29, 0, 'hello world', 34, 1" )
    PrintInfo( 34, 38, 29, 0, 'hello world', 34, 1 );

    
def multiple(one, *more): # more == Tuple
    print("argument one : ")
    print('\t', one)
    print("\ttype one: %s" % type(one))
    
    print("Argument *more : ")
    print('\t', more)
    print("\ttype more: ", type(more)) # <class 'tuple'> : always.
    for element in more:
        print('\telement value: %s telement type: %s' % ( str(element), type(element) ))

multiple(2, 34, 'third', 3.14, (1, 2, 3))

## ----------------------------------------------------------------------------
# myFunc(1, 2, arg3=3, arg4=4, arg5=5, arg6=6, arg7=7)
# myFunc(arg1=1, arg2=2, arg3=3, arg4=4, arg5=5, arg6=6, arg7=7)
#  => arg1==1, arg2==2, args=={'arg3'=3, 'arg4'=4, 'arg5'=5, 'arg6'=6, 'arg7'=7}
def myFunc(arg1, arg2, **kwargs): ## args : dict
    """
    Two asterisks(**) are placed before the variable name that will
     hold the values of all KEYWORD arguments(Dictionary).
    """
    print( arg1 )
    print( arg2 )
    print( kwargs ) ## dictionary (not an ordered dictionary)
    return

## ----------------------------------------------------------------------------
# NonKeywordFunc(1, 2, arg3=3, arg4=4, arg5=5, arg6=6, arg7=7)
# NonKeywordFunc(arg1=1, arg2=2, arg3=3, arg4=4, arg5=5, arg6=6, arg7=7)
#  => arg1==1, arg2==2, args=={'arg3'=3, 'arg4'=4, 'arg5'=5, 'arg6'=6, 'arg7'=7}
def NonKeywordFunc(arg1, arg2, *args):
    """
    One asterisk(*) is placed before the variable name that will
     hold the values of all NON-KEYWORD arguments.
    """
    print( arg1 )
    print( arg2 )
    print( args )   ## Tuple
    return

## ----------------------------------------------------------------------------
def unpackArgs():
    """
    Pass a list into a function with '*' in front of list.
    Number of items in the list must match number of arguments in the function
    """

    # 
    listOfArgs = ['hello', 1, 2]
    NonKeywordFunc( *listOfArgs )

    ## Note: since function 'NonKeywordFunc' can take variable number of arguments,
    ##        so the argument list pass in here could have any number of items in it.
    listOfArgs = ['hello', 1, 2, 'more', 'items']
    NonKeywordFunc( *listOfArgs ) ''' Fucntion call use list for unpack arguments '''

    return

if __name__=="__main__":
    PrintInfo_Test()
    
## ----------------------------------------------------------------------------
