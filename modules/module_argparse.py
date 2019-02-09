#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Module - argparse
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
"""

# three choices: getopt, optparse, argparse
# use argparse, it is newer

from __future__ import division, unicode_literals, print_function, absolute_import

## --- Methods ---
"""
#------------------------------------------------------------------------------
 - argparse.Action()
 - argparse.ArgumentDefaultsHelpFormatter()
 - argparse.ArgumentError()
 - argparse.ArgumentParser()
 - argparse.ArgumentTypeError
 - argparse.FileType()
 - argparse.HelpFormatter()
 - argparse.MetavarTypeHelpFormatter()
 - argparse.Namespace()
 - argparse.RawDescriptionHelpFormatter()
 - argparse.RawTextHelpFormatter
#------------------------------------------------------------------------------
"""

## --- Attribute ---
"""
Note : 
 usage : argparse.Attribute
 - .ONE_OR_MORE
 - .OPTIONAL
 - .PARSER
 - .REMAINDER
 - .SUPPRESS
 - .ZERO_OR_MORE
"""


##-----------------------------------------------------------------------------
def add_argument():
    # https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
    """
    ArgumentParser.add_argument( name_or_flags...[,action] [,nargs] [,const] [,default] 
                                [,type] [,choice] [,required] [,help] [,metavar] [,dest] )
    
    name_or_flags - Either a name or a list of option strings, e.g. foo or -f, --foo.
    action   - The basic type of action to be taken when this argument is encountered at the command line.
    nargs    - The number of command-line arguments that should be consumed.
    const    - A constant value required by some action and nargs selections.
    default  - The value produced if the argument is absent from the command line.
    type     - The type to which the command-line argument should be converted.
    choices  - A container of the allowable values for the argument.
    required - Whether or not the command-line option may be omitted (optionals only).
    help     - A brief description of what the argument does.
    metavar  - A name for the argument in usage messages.
    dest     - The name of the attribute to be added to the object returned by parse_args().
    """
    
    return
    
def argparse_1():
    import argparse
    
    ## Creating a parser (an ArgumentParser object)
    parser = argparse.ArgumentParser( description="Process some integers" )
    # run parser.print_help() at Pyton prompt
    
    ## Adding arguments
    # https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_argument
    parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
                    
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')
                        
    ## Parsing arguments
    parser.parse_args(['--sum', '7', '-1', '42'])
    #Namespace(accumulate=<built-in function sum>, integers=[7, -1, 42])

    return
    
def argparse_2():
    import argparse
    
    ## Creating a parser (an ArgumentParser object)
    parser = argparse.ArgumentParser( 
        description='A foo that bars', 
        epilog="And that's how you'd foo a bar")
    
    ## run parser.print_help() at Pyton prompt
    """
    usage: argparse.py [-h]

    A foo that bars

    optional arguments:
     -h, --help  show this help message and exit

    And that's how you'd foo a bar
    """
    
    return
    
# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='command-line utilities')

    subparsers = parser.add_subparsers(title='command', dest='command')

    info_parser = subparsers.add_parser('info', help='print information to diagnose')

    console_parser = subparsers.add_parser('shell', help='start the console')

    args = parser.parse_args()
    print("args type ", type(args)) # <class 'argparse.Namespace'>
    print(args)

    if args.command == 'info':
        print( "info command" )
    elif args.command == 'shell':
        print( "shell command" )

else:
    pass

##-----------------------------------------------------------------------------
"""
Resources:
 - https://docs.python.org/3/library/argparse.html#module-argparse
 - https://docs.python.org/3/library/argparse.html
 - https://docs.python.org/3/howto/argparse.html#id1
 

"""
