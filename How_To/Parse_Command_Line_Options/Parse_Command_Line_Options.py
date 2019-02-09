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


# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Description of KeyPress program')
  
  # parser.add_argument('-f','--file', help='Description for file argument', required=True)
  # parser.add_argument('-w','--wait', help='Description for wait argument', required=True)
  # parser.add_argument('-s','--status', help='Description for status argument', required=True)
  parser.add_argument('-f','--file', help='Key Press Record file to playback' )
  parser.add_argument('-w','--wait', default=3, help='Wait for specified seconds before exit' )
  parser.add_argument('-s','--status', help='Check key press activity status' )

  #'args' will be a dictionary containing the arguments
  args = vars( parser.parse_args() )
  print( args )

  if args['file']:
    print( "Let's play record file" )

  if args['wait']:
    print( 'Wait before exit' )
  
  if args['status']:
    print( "Check Key Press Status" )
    
  exit(1);
  
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
