#!C:\Python34\python.exe
#!/Python34/python
#!/usr/bin/python

# -*- coding: utf-8 -*-

## ----------------------------------------------------------------------------
"""
  Python
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  There is a basket of eggs, 
  if take 2 at a time, there will be 1 left in the end,
  if take 3 at a time, there will be 1 left in the end,
  if take 4 at a time, there will be 1 left in the end,
  if take 5 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 7 at a time, there will be NO eggs left in the end,
  how many eggs in the basket?

"""

import os
import time

## ----------------------------------------------------------------------------
def how_many_eggs_31():
    """ 39594522567601  """
    j=0
    #for i in range(2248776129601, 10000000000000, 310): ## 140 minutes, not found
    #for i in range(9995182984081, 20000000000000, 310): ## 3 hours
    #for i in range(19997398582561, 30000000000000, 310): ## 3 hours
    #for i in range(29989521077041, 40000000000000, 310): ## 3 hours
    #for i in range(39476937906001, 40000000000000, 310): ## <== will find 39594522567601 (2+ minutes)
    #for i in range(39998246727601, 50000000000000, 310): ## 3 hours
    #for i in range(49990369222081, 60000000000000, 310): ## 3 hours
    for i in range(51807077476561, 960000000000000, 310): ## 3 hours

    if i%16==1 and i%17==1 and i%18==1 and i%19==1 and i%20==1 and i%21==1 :
        j+=1
        if j%1000==0 : print(i);
        if i%22==1 and i%23==1 and i%24==1 and i%25==1 and i%26==1 and i%27==1 and i%28==1 and i%29==1 and i%30==1:
            print( "Found Result" )
            print( i )
            return i

    return None

## ---------------------------------------------------------------------------- 
def how_many_eggs_29_by_290():
    """
    2248776129601 
    27868761320401
    """
    j=0
    for i in range( 28188000000841, 899000000841, -290):
        if i%14==1 and i%15==1 and i%16==1 and i%17==1 and i%18==1 and i%19==1:
            j+=1
            if j%100==0:
                print(i)
            if i%20==1 and i%21==1 and i%22==1 and i%23==1 and i%24==1 and i%25==1 \
              and i%26==1 and i%27==1and i%28==1 and i%29==0:
                print( "Found Result" )
                return i

    return None

def how_many_eggs_29():
    """ 
    2248776129601
    27868761320401
    """
    for i in range(29000000000000, 2900000000000, -29):
        if i%1000000000==0:
            print(i)
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
        i%8==1 and i%9==1 and i%10==1 and i%11==1 and i%12==1 and i%13==1 and \
        i%14==1 and i%15==1 and i%16==1 and i%17==1 and i%18==1 and i%19==1 and \
        i%20==1 and i%21==1 and i%22==1 and i%23==1 and i%24==1 and i%25==1 \
        and i%26==1 and i%27==1and i%28==1 and i%29==0:
            return i

    return None

## ----------------------------------------------------------------------------
def how_many_eggs_29():
    """ 
    2248776129601  
    27868761320401
    """
    for i in range(2900000000, 10000000000000, 29):
        if i%1000000000==0:
            print(i)
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
        i%8==1 and i%9==1 and i%10==1 and i%11==1 and i%12==1 and i%13==1 and \
        i%14==1 and i%15==1 and i%16==1 and i%17==1 and i%18==1 and i%19==1 and \
        i%20==1 and i%21==1 and i%22==1 and i%23==1 and i%24==1 and i%25==1 \
        and i%26==1 and i%27==1and i%28==1 and i%29==0:
            return i

    return None

## ----------------------------------------------------------------------------
def how_many_eggs_23():
    """ 698377681  """
    for i in range(23, 1000000000, 23):
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
        i%8==1 and i%9==1 and i%10==1 and i%11==1 and i%12==1 and i%13==1 and \
        i%14==1 and i%15==1 and i%16==1 and i%17==1 and i%18==1 and i%19==1 and \
        i%20==1 and i%21==1 and i%22==1 and i%23==0:
            return i

    return None

def how_many_eggs_23_new():
    """ 698377681  """
    for i in range(23, 10000000000, 23):
        if i%22==1 and i%21==1 and i%20==1:
            if i%19==1 and i%16==1 and i%17==1 and i%18==1:
                if i%14==1 and i%15==1 and i%13==1:
                    if i%10==1 and i%11==1 and i%12==1:
                        if i%8==1 and i%9==1 :
                        #i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
                            return i

    return None

## ----------------------------------------------------------------------------
def how_many_eggs_19():
    """ 49008961  """
    for i in range(19, 100000000, 19):
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
        i%8==1 and i%9==1 and i%10==1 and i%11==1 and i%12==1 and i%13==1 and \
        i%14==1 and i%15==1 and i%16==1 and i%17==1 and i%18==1 and i%19==0 :
            return i

    return None

def how_many_eggs_19_new():
    """ 49008961  """
    for i in range(19, 100000000, 19):
        if i%16==1 and i%17==1 and i%18==1:
            if i%14==1 and i%15==1 and i%13==1:
                if i%10==1 and i%11==1 and i%12==1:
                    if i%8==1 and i%9==1 :
                        return i

    return None

## ----------------------------------------------------------------------------
"""
  There is a basket of eggs, 
  if take 2 at a time, there will be 1 left in the end,
  if take 3 at a time, there will be 1 left in the end,
  if take 4 at a time, there will be 1 left in the end,
  if take 5 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 7 at a time, there will be 1 left in the end,
  if take 8 at a time, there will be 1 left in the end,
  if take 9 at a time, there will be 1 left in the end,
  if take 10 at a time, there will be 1 left in the end,
  if take 11 at a time, there will be 1 left in the end,
  if take 12 at a time, there will be 1 left in the end,
  if take 13 at a time, there will be NO eggs left in the end,
  how many eggs in the basket? (7207201)
"""
def how_many_eggs_17():

    for i in range(100000000):
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
            i%8==1 and i%9==1 and i%10==1 and i%11==1 and i%12==1 and i%13==1 and \
                i%14==1 and i%15==1 and i%16==1 and i%17==0 :
                    return i

    return None


## ----------------------------------------------------------------------------
"""
  There is a basket of eggs, 
  if take 2 at a time, there will be 1 left in the end,
  if take 3 at a time, there will be 1 left in the end,
  if take 4 at a time, there will be 1 left in the end,
  if take 5 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 7 at a time, there will be 1 left in the end,
  if take 8 at a time, there will be 1 left in the end,
  if take 9 at a time, there will be 1 left in the end,
  if take 10 at a time, there will be 1 left in the end,
  if take 11 at a time, there will be 1 left in the end,
  if take 12 at a time, there will be 1 left in the end,
  if take 13 at a time, there will be NO eggs left in the end,
  how many eggs in the basket? (83161)
"""
## ----------------------------------------------------------------------------
def how_many_eggs_13():

    for i in range(25201, 1000000, 10):
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
            i%8==1 and i%9==1 and i%10==1 and i%11==1 and i%12==1 and i%13==0 :
                return i

    return None

"""
  There is a basket of eggs, 
  if take 2 at a time, there will be 1 left in the end,
  if take 3 at a time, there will be 1 left in the end,
  if take 4 at a time, there will be 1 left in the end,
  if take 5 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 7 at a time, there will be 1 left in the end,
  if take 8 at a time, there will be 1 left in the end,
  if take 9 at a time, there will be 1 left in the end,
  if take 10 at a time, there will be 1 left in the end,
  if take 11 at a time, there will be NO eggs left in the end,
  how many eggs in the basket? (25201)
"""
## ----------------------------------------------------------------------------
def how_many_eggs_11():

    for i in range(10001, 100001, 10):
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==1 and \
          i%8==1 and i%9==1 and i%10==1 and i%11==0 :
            return i

    return None


## ----------------------------------------------------------------------------
"""
  There is a basket of eggs, 
  if take 2 at a time, there will be 1 left in the end,
  if take 3 at a time, there will be 1 left in the end,
  if take 4 at a time, there will be 1 left in the end,
  if take 5 at a time, there will be 1 left in the end,
  if take 6 at a time, there will be 1 left in the end,
  if take 7 at a time, there will be NO eggs left in the end,
  how many eggs in the basket?
"""
def how_many_eggs():

    for i in range(1000):
        if i%2==1 and i%3==1 and i%4==1 and i%5==1 and i%6==1 and i%7==0 :
            return i

    return None

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


