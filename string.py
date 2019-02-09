#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-
"""
  Python String
  ~~~~~~~~~~~~~~~~~~~~~~


"""


## ----------------------------------------------------------------------------
## --- string methods ---
# -- String.method()
#   capitalize()  - Upper case first character
#   casefold()    - Lower case ?
#   center(width[, fillchar])
#   count('l')    - Count number of occurance
#   encode()
#   endswith()
#   expandtabs()
#   find()
#   format()
#   format_map()
#   index()
#   isalnum()
#   isalpha()
#   isdecimal()
#   isdigit()
#   isidentifier()
#   islower()
#   isnumeric()
#   isprintable()
#   isspace()
#   istitle()
#   isupper()
#   join()
#   ljust()
#   lower()
#   lstrip()
#   maketrans()
#   partition()
#   replace()
#   rfind()
#   rindex()
#   rjust()
#   rpartition()
#   rsplit()
#   rstrip()
#   split()
#   splitlines()
#   startswith()
#   strip()
#   swapcase()
#   title()
#   translate()
#   upper()
#   zfill()

# strDst = strSrc.upper() 


## ----------------------------------------------------------------------------
## Escape character
#   \'    Single quote
#   \"    Double quote
#   \t    Tab
#   \n    Newline (line break)
#   \\    Backslash

## ----------------------------------------------------------------------------
## Raw Strings - r in front of quotation mark, will ignore all escape chars
#  print( r'That is Carol\'s cat.' )
#

## ----------------------------------------------------------------------------
## Multiline String with Triple Quotes

#----- Triple Single Quotes -----
SingleQuoteString = '''Dear Alice,

Evs's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
'''

#----- Triple Double Quotes -----
DoubleQuoteString = """Dear Alice,

Evs's cat has been arrested for catnapping, cat burglary, and extortion.

Sincerely,
Bob
"""



## ----------------------------------------------------------------------------
import os
import time

def String_Summary():
    '123'.   isalnum()  # True
    '123ab'. isalnum()  # True
    '123_ab'.isalnum()  # False

    'abc'  .isalpha()   # True
    'abc  '.isalpha()   # False
    '12abc'.isalpha()   # False

    '123'.isdecimal()   # True

    '   '.isspace()     # True
    ' a '.isspace()     # False

    ## Title: First Character Is Upper Caseed. (Only First)
    'This Is Title'.istitle() # True
    'Yes Title 123'.istitle() # True
    'yes Title 123'.istitle() # False
    'YEs Title 123'.istitle() # False

    return


def str_center():
    src = 'Hello World';

    dst = src.center(60, '-')
    #=> dst == '------------------------Hello World-------------------------'

    return s

## --- find ---
def str_find():
    """
    - if found, return the starting string position
    - if not found, reutnr -1
    """

    s = b'\x00\x01\x02\xff\xff\xff\xff\xff\x3c\xc3'
    found = s.find( b'\xff\xff\x3c\xc3' ) #=> 6

    s = b'\x00\x01\x02\xff\xff\xff\xff\xff\x3c\xc3'
    found = s.find( b'\xaa\xdd\x3c\xc3' ) # found == -1

    return

def str_isdigit():
    """
    - '3 4 5'.isdigit() ==> False (There are spaces)
    - '345'.isdigit() ==> True
    """

    s1 = "this is a string"
    if s1.isdigit() == True:  # False
        print ("Yes, digit")
    else:
        print ("No, no digit")
    return

def str_strip():
    """
    strip() method will strip all leading spaces and trailing spaces
    """
    data = "    3 4 5   ".strip() #== "3 4 5"
    return

def str_in():
    ss = 'Hello World';
    'llo' in ss     #=> True
    'ddd' not in ss #=> True

    return



## --- String Index ---
def str_Indexing_01():
    ss = "Hello World"
    ss[0]   # 'H'
    ss[1]   # 'e'
    ss[2]   # 'l'
    ss[3]   # 'l'
    ss[4]   # 'o'
    ss[5]   # ' '
    ss[6]   # 'w'
    ss[7]   # 'o'
    ss[8]   # 'r'
    ss[9]   # 'l'
    ss[10]  # 'd'

    ss[11]  # Traceback (most recent call last):
            #   File "<pyshell#93>", line 1, in <module>
            #     ss[11]
            #   IndexError: string index out of range

    return

def str_Indexing_02():
    ss1 = "Hello World!"
    print( ss1 )       # Complete string
    print( ss1[0] )    # First character
    print( ss1[1:4] )  # char from 2nd to 4th (note: not include ss1[4])
    print( ss1[2:] )   # char from 3rd to end
    print( ss1*2 )     # 2 times (Repeat String) 'Hello World!Hello World!'

    print( ss1 + " I am John" )  # concatenated

    ## what about reverser string?
    # for example str[4:1], how?    [4:1] will just return empty
    return

def str_Indexing_Reverse():
    ss1 = "Hello World"
    ss1[-1] # Last character, 'd' in this case
    ss1[-4:-1]  # => 'orl'  ## Notice not including the last character
    ss1[-4:]    # => 'orld' ## Last 4 characters

    return


## ----------------------------------------------------------------------------
##
def how_to_get_rid_of_white_spaces():
    s = '\n\n\n\t\n\t\n\t\n\t\n\t\n\t\n\n\n\n\t\n\n\n\t\
\n\t\t\t\
\n\t\
\n\t\t\
\n\t\t\t\
\n 0 favorites\n\
\n\n\t\t\
\n\t\t\
∨\
\n\t\t\
∧\
\n\t\t\
\n \n\
\n\
\n\t \tCL wenatchee all personals casual encounters\n\
\n\
\n\t\t\
\n\t\
\n\
\n\n\t\t\
\n\t\t\t\
\n\t\n\t\t\n\t\n\n\n\nReply to: 59nv6-4031116628@pers.craigslist.org\n\
\n\n\n\t\
\n\t\tflag [?] :\n\t\t\tmiscategorized\n\t\n\t\tprohibited\n\t\n\t\tspam\n\t\t\tbest of\n\t\n\
\n\n\t\t\
\
Posted: 2013-08-28, 8:23AM PDT\
\n\
\n\n\
\n \n Well... - w4m - 22 (Wenatchee)\n'

    # split the string to list
    split_to_list = s.split()

    # join the list back to string
    join_to_string = ''.join( split_to_list )
    join_to_string = ' '.join( split_to_list )
    #join_to_string = '\n'.join( split_to_list )

    print( join_to_string )

    return

# -----------------------------------------------------------------------------
def string_percent_r_vs_s():
    # following have same output
    print("%r" % 12345) ## repr(12345)
    print("%s" % 12345) ## str(12345)
    
    ## Notice there is single quote with %r output
    print("%r" % "hello") ## 'hello'
    print("%s" % "hello") ## hello
    
## ----------------------------------------------------------------------------
def main():
    how_to_get_rid_of_white_spaces()

    #str_Indexing_01()
    #str_Indexing_02()

    ## what about reverser string?
    # for example str[4:1], how?

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()

## ----------------------------------------------------------------------------
