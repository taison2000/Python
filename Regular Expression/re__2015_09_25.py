#!/usr/bin/python
# -*- coding: utf-8 -*-

##-----------------------------------------------------------------------------
"""
#------------------------------------------------------------------------------
Available Methods after a matched result:
  Methods
  - start()
  - end()
  - expand("string")
  - group() : matched group(s)
  - groupdict()
  - groups()
  - span()    : return matched span (tuple)
  - start()   : start position of matched
  - string()  : Source string
  
  Attributes
  - endpos : end position of source string
  - lastgroup
  - lastindex
  - pos
  - re  : recompile
  - regs
#------------------------------------------------------------------------------
"""


"""
#------------------------------------------------------------------------------
Available Methods after a matched result:
  mat = re.search("lo", "hello world") => Yes, match
   => mat == <_sre.SRE_Match object; span=(3, 5), match='lo'>
  Methods
  - mat.start()
  - get()
  - icursor(index)
  - index (index)
  - insert (index, s)
  - select_adjust(index)
  - select_clear()
  - select_from(index)
  - select_present()
  - select_range(start, end)
  - select_to (index)
  - xview(index)
  - xview_Scroll(number, what)
#------------------------------------------------------------------------------
"""
import os
import time
import re	# import the Regular Expression module

"""
-------------------------------------------------------------------------------
# escape
#   Escape all the characters in pattern except ASCII letters, numbers and '_'.
-------------------------------------------------------------------------------
""" 
def re_escape():
  line = "abcdef!@ghi#$jk456$%^lmn&*(op)rs_-uv_+w`xy~"
  m = re.escape(line)
  # m == abcdef\!\@ghi\#\$jk456\$\%\^lmn\&\*\(op\)rs_\-uv_\+w\`xy\~
  # 'line' is unchanged
  line = "a`b~c!d@e#f$g%h^i&j*k(l)m-n_o=p+q[r{s]t}u\v|w;x:y'z1,2<3.4>5/67?890"
  m = re.escape(line)
  # m == a\`b\~c\!d\@e\#f\$g\%h\^i\&j\*k\(l\)m\-n_o\=p\+q\[r\{s\]t\}u\\|w\;x\:y\'z1\,2\<3\.4\>5\/67\?890
  # Notice original string, there is '\v' in there. (it is already escape char)
  
  #line = "a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\u\v\w\x\y\z\1\2\3\4\5\6\7\8\9\0"
  line = "a\b\c\d\e\f\g\h\i\j\k\l\m\n\o\p\q\r\s\t\v\w\y\z\1\2\3\4\5\6\7\8\9\0"  # no \x or \u
  m = re.escape(line)
  # m == a\\\c\\d\\e\\\g\\h\\i\\j\\k\\l\\m\
  #    \\o\\p\\q\
  #   \\s\	\\\w\\y\\z\\\\\\\\\8\\9\000

""""
## ----------------------------------------------------------------------------
# split
# -----------------------------------------------------------------------------
"""
def re_split():
  m=re.split('cat', 'Cat are smart, cats are lazy, a lot of cats in the park, cat city')
   # m == ['Cat are smart, ', 's are lazy, a lot of ', 's in the park, ', ' city']    # <-- Notice 'Cat' (capital 'C') is not part of split
  m=re.split(' ', 'Cat are smart, cats are lazy, a lot of cats in the park, cat city') # split with space
   # m == ['Cat', 'are', 'smart,', 'cats', 'are', 'lazy,', 'a', 'lot', 'of', 'cats', 'in', 'the', 'park,', 'cat', 'city']

  line='a lot  of two  spaces to  split  the  sentence are you   ready yet?'
  m=re.split('  ', line)  # Use two spaces to split
   # m == ['a lot', 'of two', 'spaces to', 'split', 'the', 'sentence are you', ' ready yet?']
   #                                                                            ^
   #                                                                            | extra space here, because or 3 spaces original

""""
# -----------------------------------------------------------------------------
# search
# -----------------------------------------------------------------------------
"""   
def re_search():
	m = re.search('cat', 'There is a cat in the house') 
  # m == <_sre.SRE_Match object; span=(11, 14), match='cat'>
  
  m = re.search('\W', 'AB12_8~53&7')
  # m == <_sre.SRE_Match object; span=(6, 7), match='~'>


""""
# -----------------------------------------------------------------------------
# Example
# -----------------------------------------------------------------------------
"""
def re_examples():
  m = re.match('cat', 'There is a cat in the house') 
  # m == None; no match. match only search begining of string
  
	m=re.findall('cat', 'Cat are smart, cats are lazy, a lot of cats in the park, cat city')
    # m == ['cat', 'cat', 'cat']

# ------------------------------------------------------------------------------
# Main program
# ------------------------------------------------------------------------------
def main():
# This is the main function

  line = "Cats are smarter than dogs";
  
  # ^ From begining of line
  matchObj = re.match( r'^cats', line, re.M|re.I)
  
  if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    #print ("matchObj.group(1) : ", matchObj.group(1))
    #print ("matchObj.group(2) : ", matchObj.group(2))
  else:
    print("No match!!")

  

  
# ------------------------------------------------------------------------------
# Case Sensitive
#   re.I flag is for case-insensitive
# ------------------------------------------------------------------------------
  print("\n")
  print("Case senitive search")
  print("Search for 'cats' in 'Cats are smarter than dogs'")
  
  line = "Cats are smarter than dogs";
  
  # ^ From begining of line
  matchObj = re.match( r'^cats', line, re.M)
  #matchObj = re.match( r'^cats', line, re.M|re.I)  # <- re.I : case insenstive
  
  if matchObj:
    print ("matchObj.group() : ", matchObj.group())
    #print ("matchObj.group(1) : ", matchObj.group(1))
    #print ("matchObj.group(2) : ", matchObj.group(2))
  else:
    print("No match!!")

# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------
if __name__ == "__main__":
	main()
  #msg = main()

"""
re.match (pattern, string, flags=0)
  Pattern : This is the regular expression to be matched
  String  : This is the string, which would be searched to match the pattern at the begining of string
  Flags   : Specify different flags using bitwise OR(|). These are modifiers, which are listed in the table below

    Modifier Description
    -----------------------------------------------------------------------------------------------
      re.I    Performs case-insensitive matching.
      re.L    Interprets words according to the current locale. 
                This interpretation affects the alphabetic group (\w and \W), 
                as well as word boundary behavior (\b and \B).
      re.M    Makes $ match the end of a line (not just the end of the string) and makes ^ match the
                start of any line (not just the start of the string).
      re.S    Makes a period (dot) match any character, including a newline.
      re.U    Interprets letters according to the Unicode character set. 
                This flag affects the behavior of \w, \W, \b, \B.
      re.X    Permits "cuter" regular expression syntax. It ignores whitespace (except inside a set []
                or when escaped by a backslash) and treats unescaped # as a comment marker.  
"""

"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""
