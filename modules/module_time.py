#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  time module
  ~~~~~~~~~~~

"""

import os
import time

##-----------------------------------------------------------------------------
"""
# Properties:
#  - time.timezone  => difference in seconds between UTC and local standard time
#  - time.altzone   => difference in  seconds between UTC and local DST time
#  - time.daylight  => whether local time should reflect DST
#  - time.tzname    => tuple of (standard time zone name, DST time zone name)
#                       ('Pacific Standard Time', 'Pacific Daylight Time')
#  - 
#  - 
#
#
# Methods:
#  - time.altzone
#  - time.asctime()
#  - time.clock()
#  - time.ctime()
#  - time.gmtime()
#  - time.localtime()
#  - time.mktime(tupletime)
#  - time.sleep(secs)
#  - time.strftime(fmt[,tupletime])
#  - time.strptime(str, fmt='%a %b %d %H:%M:%S %Y')
#  - time.time()
#  - time.tzset()
#  
# Index Attributes Values
#  0 tm_year  2008
#  1 tm_mon   1 to 12
#  2 tm_mday  1 to 31
#  3 tm_hour  0 to 23
#  4 tm_min   0 to 59
#  5 tm_sec   0 to 61   (60 or 61 are leap-seconds)
#  6 tm_wday  0 to 6    (0 is Monday)
#  7 tm_yday  1 to 366  (Julian day)
#  8 tm_isdst -1, 0, 1, -1 means library determines DST

"""

##-----------------------------------------------------------------------------
def DateTimeString():
    t = time.localtime()
    s = format('%04d'%t.tm_year + '_%02d'%t.tm_mon + '_%02d'%t.tm_mday + '__%02d'%t.tm_hour + '_%02d'%t.tm_min + '_%02d'%t.tm_sec)
    s = format('%04d'%t.tm_year + '%02d'%t.tm_mon + '%02d'%t.tm_mday + '_%02d'%t.tm_hour + '%02d'%t.tm_min + '%02d'%t.tm_sec)
    return s
    
def method_asctime():
    # time.asctime( (year, month, day, hours, minutes, seconds, weekday(monday=0), Julian_day(day in the year, 1-366), DST)
    
    s = time.asctime()  # 'Fri Jul 15 16:37:00 2016'
    l = s.split()   # ['Fri', 'Jul', '15', '16:37:00', '2016']
    
    # takes a tuple (with 9 elements), convert it to time string
    t = time.asctime( (2016, 7, 15, 16, 47, 54, 4, 197, 1) )    # must exactly 9 items tuple
    # type(t) : <class 'str'>
    # t == 'Fri Jul 15 16:47:54 2016'
    
    return
    
def method_clock():
    """
    time.clock() return the current processor time as floating point number
        expressed in seconds on Unix.
    """
    t0 = time_clock()   # initial
    
    time.sleep(5)
    t1 = time_clock()   # t1 == 5.00

def method_ctime():
    """
    time.ctime() ==> 'Fri Jul 17 11:30:04 2015' ; # return a string
    """
    c = time.ctime()
    
    l = c.split()
    # ['Fri', 'Jul', '15', '12:14:16', '2016']
    
    # Take second as optional input
    s = time.ctime(1234567) # 'Wed Jan 14 22:56:07 1970'
    
    return
    
def method_gmtime ():
    """
    time.gmtime([secs]) : Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. 
                  Note :t.tm_isdst is always 0
      => time.struct_time(tm_year=2015, tm_mon=7, tm_mday=30, tm_hour=17, tm_min=8, tm_sec=28, tm_wday=3, tm_yday=211, tm_isdst=0)
    """
    
    t = time.gmtime( 0 )    # Epoch
    # time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)
    
    gm = time.gmtime()

    t = time.gmtime( 1456210303 )
    # t == time.struct_time(tm_year=2016, tm_mon=2, tm_mday=23, tm_hour=6, tm_min=51, tm_sec=43, tm_wday=1, tm_yday=54, tm_isdst=0)

    t = time.gmtime( 1456210303.3456789 )   # could take a float for fra
    
    return
    

# -----------------------------------------------------------------------------
def method_localtime():
    """
    lt = time.localtime(time.time()) # time.localtime() also work
    # time.struct_time(tm_year=2015, tm_mon=7, tm_mday=16, tm_hour=15, tm_min=9, tm_sec=52, tm_wday=3, tm_yday=197, tm_isdst=1)
    # to access individual: lt.tm_year, lt.tm_mon ...

    """
    
    t = time.localtime()  # <class 'time.struct_time'>
    #time.struct_time(tm_year=2016, tm_mon=7, tm_mday=15, tm_hour=12, tm_min=22, tm_sec=29, tm_wday=4, tm_yday=197, tm_isdst=1)
    """
    t.count()   # count occurance of a number;  ex.: t.count(2016)==1
    t.index()
    t.n_fields  # 9
    t.n_sequence_fields  #9
    t.n_unnamed_fields
    t.tm_hour
    t.tm_isdst  # is daylight saving time
    t.tm_mday   # day of month
    t.tm_min    # minute
    t.tm_mon    # month
    t.tm_sec    # seconds
    t.tm_wday   # day of week (0=Sun, .. 4=Fri, 5=Sat)
    t.tm_yday   # day of year
    t.tm_year   # year
    """
    
    return (t.tm_hour, t.tm_min, t.tm_sec)
    
def method_time():
    # assume time.time() => 1459445950.2023869
    d = format( '%d'%time.time() )    #=> 1459445950
    f = format( '%.4f'%time.time() )  #=> 1459445950.2024 (notice .0004 if round up)
    return

# -----------------------------------------------------------------------------
# Main program - This is the main function
# -----------------------------------------------------------------------------
def main():
    ticks = time.time() # Number of ticks since 12:00AM, January 1, 1970


# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()

## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 - http://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
 - http://geography.about.com/od/timeandtimezones/a/gmtutc.htm
 - http://stackoverflow.com/questions/11550994/convert-time-to-unix-time?lq=1
 - http://stackoverflow.com/questions/13260863/convert-a-unixtime-to-a-datetime-object-and-back-again-pair-of-time-conversion
 - http://stackoverflow.com/questions/12081310/python-module-to-change-system-date-and-time
  
"""


##-----------------------------------------------------------------------------
"""
Others:
# import calendar
#  - cal = calendar.month(2015, 1) => Jan 2015
#  - 
#  - 
"""

##-----------------------------------------------------------------------------
"""
Examples: 
  time.strftime("%D %H:%M",     time.localtime(int("1456210303")))
  time.strftime("%D %H:%M",     time.gmtime(int("1456210303")))
  time.strftime("%D %H:%M:%S",  time.gmtime(int("1456210303")))
  time.ctime(int("1456210303"))
  time.mktime( (2016, 2, 23, 6, 51, 43, 0, 0, 0) )
  
  d=datetime.datetime(2001, 10, 28, 1, 6, 40)
  d = datetime.datetime(2001, 10, 28, 1, 6, 40)
  d.timestamp() => 1004256400.0
  
  d = datetime.datetime(2016, 2, 23, 6, 51, 43)
  d.timestamp() => 1456239103.0
  d.timetuple()
   => time.struct_time(tm_year=2016, tm_mon=2, tm_mday=23, tm_hour=6, tm_min=51, tm_sec=43, tm_wday=1, tm_yday=54, tm_isdst=-1)
   
  datetime.datetime.utcfromtimestamp( 1456210303 )
   => datetime.datetime(2016, 2, 23, 6, 51, 43)
  d = datetime.datetime.utcfromtimestamp(1456210303)
   => datetime.datetime(2016, 2, 23, 6, 51, 43)
  d.utctimetuple() 
   => time.struct_time(tm_year=2016, tm_mon=2, tm_mday=23, tm_hour=6, tm_min=51, tm_sec=43, tm_wday=1, tm_yday=54, tm_isdst=0)
   
"""
