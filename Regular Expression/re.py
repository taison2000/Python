#!/usr/bin/python
# -*- coding: utf-8 -*-

##-----------------------------------------------------------------------------
"""
re module
#------------------------------------------------------------------------------

  Methods       Description
  - compile()   Compile a pattern into a RegexObject.
  - error()
  - escape()    Backslash all non-alphanumerics in a string.
  - findall()   Find all occurrences of a pattern in a string.
  - finditer()  Return an iterator yielding a match object for each match.
  - fullmatch() Match a regular expression pattern to all of a string.
  - match()     Match a regular expression pattern to the beginning of a string.
  - purge()     Clear the regular expression cache.
  - search()    Search a string for the presence of a pattern.
  - split()     Split a string by the occurrences of a pattern.
  - sub()       Substitute occurrences of a pattern found in a string.
  - subn()      Same as sub, but also return the number of substitutions made.
  - template()  Compile a template pattern, returning a pattern object
  
  Attributes
  - 
  - 
#------------------------------------------------------------------------------
"""

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
  - mat.end()
  - mat.endpos()
  - mat.expand()
  - mat.group()
  - mat.groupdict()
  - mat.groups()
  - mat.lastgroup()
  - mat.lastindex()
  - mat.pos()
  - mat.re()
  - mat.regs()
  - mat.span()
  - mat.start()
  - mat.string()
#------------------------------------------------------------------------------
"""
import os
import time
import re   # import the Regular Expression module

"""
https://docs.python.org/3/library/re.html#re.compile
"""
def re_compile():
    s = '  \t    foo   \t   bar   \t  '
    pat = re.compile(r'\s+')  # whitespace, equivalent to [\t\n\r\f]
    ss = pat.sub('', s) #=> ss=='foobar'  all whitespace gone

    s = " hello world of abc, will be match the following patternBeginaBcPatternEnd  "
    pat = re.compile('aBc')
    result = pat.search(s)  #-> result = <_sre.SRE_Match object; span=(61, 64), match='aBc'>
    # result.span() == (61,64)

    
    line = 'This is hello from Fred'
    pattern = "Fred"
    regexp = re.compile(pattern)
    m = regexp.search(line)
    # m == <_sre.SRE_Match object; span=(19, 23), match='Fred'>
    
    return

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

    ## \W match a nonword character:[A-Za-z0-9_]
    # all alphanumerics and underscore
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

    m = re.findall('cat', 'Cat are smart, cats are lazy, a lot of cats in the park, cat city')
    # m == ['cat', 'cat', 'cat']

def re_examples_digits():
    phoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumberRegex.search('My number is 415-555-4242.')
    print('phone number found: ' + mo.group())  # phone number found: 415-555-4242
    
    d = re.search("[0-5]", "hello 5world")  # string contains either 0, 1, 2, 3, 4, 5
    print(d)    # <_sre.SRE_Match object; span=(6, 7), match='5'>
    
def any_one_char():
    m = re.search("[aeiou]", 'hello world')
    print(m)    # <_sre.SRE_Match object; span=(1, 2), match='e'>
    
    m = re.search("[aeiou]", 'are you serious?')
    print(m)    # <_sre.SRE_Match object; span=(0, 1), match='a'>
    
    ## NOT (^)
    m = re.search("[^aeiou]", 'are you serious?')
    print(m)    # <_sre.SRE_Match object; span=(1, 2), match='r'>


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

## ----------------------------------------------------------------------------
"""
- See if string *STARTS* with any of this characters
  result = re.match( '[ 123odAB]', string ) # Notice also looking for a space

- See if string *CONTAINS* with any of this characters
  result = re.search( '[123odAB]', string )

"""

