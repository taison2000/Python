#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Module - argparse
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
"""

# from __future__ must be at the beginning of file
from __future__ import division, unicode_literals, print_function, absolute_import

import os, time
import argparse



##-----------------------------------------------------------------------------
def parse_required():
  parser = argparse.ArgumentParser(description='Description of your program')
  
  parser.add_argument('-f','--foo', help='Description for foo argument', required=True)
  parser.add_argument('-b','--bar', help='Description for bar argument', required=True)
  
  ## required
  parser.add_argument('-o','--output', help='Output result file', required=True)
  
  ## default
  parser.add_argument('-w','--wait', default=3, help='How long to wait for', required=True)

  #'args' will be a dictionary containing the arguments
  args = vars( parser.parse_args() )
  print( args )

  if args['foo'] == 'Hello':
    print( 'Hello option' )

  if args['bar'] == 'World':
    print( 'World option' )


# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Description of your program')

    parser.add_argument('-f','--foo', help='Description for foo argument')
    parser.add_argument('-b','--bar', help='Description for bar argument')

    
    parser.add_argument('-o','--output', help='Output result file')

    ## default
    parser.add_argument('-w','--wait', default=3, help='How long to wait for')

    #'args' will be a dictionary containing the arguments
    args = vars( parser.parse_args() )
    print( args )

    if args['foo'] == 'Hello':
        print( 'Hello option' )

    if args['bar'] == 'World':
        print( 'World option' )

# c:\Python35\Python.exe  module_argparse_keyPress.py -f FOO
# print( args ) => {'foo': 'FOO', 'output':None, 'bar':None, 'wait': 3}


##-----------------------------------------------------------------------------
"""
if __name__ == '__main__':
  
  parser = argparse.ArgumentParser(description='PyVISA command-line utilities')
  subparsers = parser.add_subparsers(title='command', dest='command')

  info_parser = subparsers.add_parser('info', help='print information to diagnose PyVISA')
  console_parser = subparsers.add_parser('shell', help='start the PyVISA console')

  args = parser.parse_args()
  if args.command == 'info':
    print( "info command" )
  elif args.command == 'shell':
    print( "shell command" )
"""
##-----------------------------------------------------------------------------
"""
Resources:
 - http://stackoverflow.com/questions/7427101/dead-simple-argparse-example-wanted-1-argument-3-results
 

"""
