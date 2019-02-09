#!/usr/bin/python
# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Parse a script
  ~~~~~~~~~~~~~~~~~~~~~~

"""

import os
import time

"""
I am trying to parse a series of text files and save them as CSV files 
using Python. 
All text files have a 4 line long header which needs to be stripped out. 
The data lines have various delimiters including 
 quote("), dash(-), column(:), and blank space. 
 
I found it a pain to code it in C++ with all these different delimiters, 
so I decided to try it in Python, hearing it is relatively easier to do.

I wrote a piece of code to test it for a single line of data and it works, 
however, I could not manage to make it work for the actual file. 
For parsing a single line I was using the text object and "replace" method. 
It looks like my current implementation reads the text file as a list, 
and there is no replace method for the list object.

Any input would be appreciated!
"""

def Data_Parser( text, dic ):
  for i, j in dic.iteritems():
    text = text.replace( i, j )
  return text

"""
This is the original author's code.
"""
def Parser_Original():
  # open input/output files
  inputFile = open( 'test.dat' )
  outputFile = open( 'test01.csv' )
  
  # sample text string, just for demonstration to let you know how the data
  # looks like.
  # my_text = '"2012-06-23 03:09:13.23",4323584,-1.911224,-0.4657288,-0.1166382,-0.24823,0.256485,"NAN",-0.3489428,-0.130449,-0.2440527,-0.2942413,0.04944348,0.4337797,-1.105218,-1.201882,-0.5962594,-0.586636'

  # dictionary definition 0-, 1-, etc. 
  #  are there to parse the date block delimited with dashes, and make sure the negative numbers are not effected
  reps = {'"NAN"':'NAN', '"':'', '0-':'0,','1-':'1,','2-':'2,','3-':'3,','4-':'4,','5-':'5,','6-':'6,','7-':'7,','8-':'8,','9-':'9,', ' ':',', ':':',' }
  
  my_text = inputFile.readlines()[4:] # reads whole text file, skipping first 4 lines
  txt = Data_Parser( my_text, reps )
  outputFile.writelines( txt )
  
  inputFile.close()
  outputFile.close()
  return

"""
Read file one line at a time
"""
def Parser_Solution():
  # open input/output files
  inputFile = open( 'test.dat' )
  outputFile = open( 'test02.csv' )
  
  # sample text string, just for demonstration to let you know how the data
  # looks like.
  # my_text = '"2012-06-23 03:09:13.23",4323584,-1.911224,-0.4657288,-0.1166382,-0.24823,0.256485,"NAN",-0.3489428,-0.130449,-0.2440527,-0.2942413,0.04944348,0.4337797,-1.105218,-1.201882,-0.5962594,-0.586636'

  # dictionary definition 0-, 1-, etc. 
  #  are there to parse the date block delimited with dashes, and make sure the negative numbers are not effected
  reps = {'"NAN"':'NAN', '"':'', '0-':'0,','1-':'1,','2-':'2,','3-':'3,','4-':'4,','5-':'5,','6-':'6,','7-':'7,','8-':'8,','9-':'9,', ' ':',', ':':',' }

  for i in range(4) : inputFile.next()[4:] # skipping first 4 lines  
  for line in inputFile:
    outputFile.writeline( Data_Parser(line, reps) )
  
  inputFile.close()
  outputFile.close()
  return
  
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
  """
  """
  Parser_Original()
  Parser_Solution()
  
  return

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
	main()




# -----------------------------------------------------------------------------
# Resource : 
# - http://stackoverflow.com/questions/11936967/text-file-parsing-with-python
# -----------------------------------------------------------------------------
"""

"""

'''
3 single quote string
'''
