#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  False
  None
  True
  and
  as
  assert
  break
  class
  continue
  def
  del
  elif
  else
  except
  finally
  for
  from
  global
  if
  import
  in
  is
  lambda
  nonlocal
  not
  or
  pass
  raise
  return
  try
  while
  with
  yield
"""

import os
import time

 
def kw_and():
    # if none are zero
    a, b = 10, 23
    a_and_b = a and b  # 23 (take the last of the two)
    print( a_and_b )

    # if any one is zero
    a, b = 0, 23
    a_and_b = a and b  # 0
    
    a, b = 23, 0
    a_and_b = a and b  # 0
    
    # if 0 and None, take the first
    a, b = None, 0
    a_and_b = a and b  # None

    a, b = 0, None
    a_and_b = a and b  # 0

    return
    
def kw_as():
    pass
    
def kw_assert():
    a = 3
    b = 4
    assert a==b, "%d != %d"%(a, b)
    """ Result:
    Traceback (most recent call last):
      File "<pyshell#34>", line 1, in <module>
        assert a == b, '%d != %d'%(a, b)
    AssertionError: 3 != 4
    """
    
    return

def kw_lambda():
    """
    A lambda function is an anonymous function, often used as arguments.
    """
    def adder(x):
        return lambda y: x+y    ## return anonymous function which takes argument 'y'
    
    add5 = adder(5)
    add100 = adder(100)
    
    add5(3) # 8
    add100(78) # 178
    
    # -------------------------------------------------------------------------
    multi = lambda num1, num2: num1 * num2
    result = multi(7, 8)
    result = multi(18, 56)
    
# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    """
    range()
    
    """

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()


"""
  Note: 
    - No ++ or --, use a+=1 or a-=1 
    - print ("Variable %d", %Val)
      print ("Variable %d %d", % (Val1, Val2))

  

"""


# -----------------------------------------------------------------------------
# Why (  if __name__ == "__main__":  )
# -----------------------------------------------------------------------------

##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""


'''
3 single quote string
'''
