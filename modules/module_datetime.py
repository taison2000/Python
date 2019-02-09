#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
 Module - datetime
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  - Includes in Python package
  - See also module_time and module_calendar
"""

import os
import time

##-----------------------------------------------------------------------------
"""
# Properties:
#  - MAXYEAR : 9999
#  - MINYEAR : 1
#  - datetime_CAPI
#  - 
#  - 
#  - 
#
#
# Methods:
#  - datetime.date()
#  - datetime.datetime()
#  - datetime.time()
#  - datetime.timedelta.days()
#  - datetime.timedelta.max()
#  - datetime.timedelta.microseconds()
#  - datetime.timedelta.min()
#  - datetime.timedelta.resolution()
#  - datetime.timedelta.seconds()
#  - datetime.timedelta.total_seconds()
#  - datetime.timezone.dst
#  - datetime.timezone.fromutc
#  - datetime.timezone.max
#  - datetime.timezone.min
#  - datetime.timezone.tzname
#  - datetime.timezone.utc
#  - datetime.timezone.utcoffset
#  - datetime.tzinfo.
#  - datetime.tzinfo.
#  - datetime.tzinfo.
#  - datetime.tzinfo.
#  - datetime.tzinfo.
#  - datetime.tzinfo.
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
    t = datetime.localtime()
    s = format('%04d'%t.tm_year + '_%02d'%t.tm_mon + '_%02d'%t.tm_mday + '__%02d'%t.tm_hour + '_%02d'%t.tm_min + '_%02d'%t.tm_sec)
    s = format('%04d'%t.tm_year + '%02d'%t.tm_mon + '%02d'%t.tm_mday + '_%02d'%t.tm_hour + '%02d'%t.tm_min + '%02d'%t.tm_sec)
    return s


def CTime():
    """
    datetime.ctime() ==> 'Fri Jul 17 11:30:04 2015' ; # return a string
    """
    c = datetime.ctime()
    #

def gmtime ():
    """
    datetime.gmtime([secs]) : Accepts an instant expressed in seconds since the epoch and returns a time-tuple t with the UTC time. 
                  Note :t.tm_isdst is always 0
      => datetime.struct_time(tm_year=2015, tm_mon=7, tm_mday=30, tm_hour=17, tm_min=8, tm_sec=28, tm_wday=3, tm_yday=211, tm_isdst=0)
    """
    gm = datetime.gmtime()

def LocalTime():
    lt = datetime.localtime(datetime.datetime()) # datetime.localtime() also work
    # datetime.struct_time(tm_year=2015, tm_mon=7, tm_mday=16, tm_hour=15, tm_min=9, tm_sec=52, tm_wday=3, tm_yday=197, tm_isdst=1)
    # to access individual: lt.tm_year, lt.tm_mon ...

def GetTime():
    t = datetime.localtime()
    return (t.tm_hour, t.tm_min, t.tm_sec)

# ------------------------------------------------------------------------------
# Main program - This is the main function
# ------------------------------------------------------------------------------
def main():
    ticks = datetime.datetime() # Number of ticks since 12:00AM, January 1, 1970


# ------------------------------------------------------------------------------
# Code entry
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


## ----------------------------------------------------------------------------
## Resource
## ----------------------------------------------------------------------------
"""
 - http://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
 - http://stackoverflow.com/questions/11550994/convert-time-to-unix-time?lq=1
 - http://stackoverflow.com/questions/13260863/convert-a-unixtime-to-a-datetime-object-and-back-again-pair-of-time-conversion
 - http://stackoverflow.com/questions/12081310/python-module-to-change-system-date-and-time

"""

##-----------------------------------------------------------------------------
"""
Examples: 
  time.strftime("%D %H:%M",     time.localtime(int("1456210303")))
  time.strftime("%D %H:%M",     time.gmtime(int("1456210303")))
  time.strftime("%D %H:%M:%S",  time.gmtime(int("1456210303")))
  time.ctime(int("1456210303"))     # 'Mon Feb 22 22:51:43 2016'
  time.mktime( (2016, 2, 23, 6, 51, 43, 0, 0, 0) )
  
  d = datetime.datetime(2001, 10, 28, 1, 6, 40)
  d.timestamp() => 1004256400.0
  d.timetuple() => time.struct_time(tm_year=2001, tm_mon=10, tm_mday=28, tm_hour=1, tm_min=6, tm_sec=40, tm_wday=6, tm_yday=301, tm_isdst=-1)

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


##-----------------------------------------------------------------------------
## The Difference Between GMT and UTC
"""
Greenwich Mean Time (GMT) is often interchanged or confused with 
Coordinated Universal Time (UTC). 
But GMT is a time zone and UTC is a time standard.


Although GMT and UTC share the same current time in practice, 
there is a basic difference between the two:

 - GMT is a time zone officially used in some European and African countries. 
   The time can be displayed using both the 24-hour format (0 - 24) or 
   the 12-hour format (1 - 12 am/pm).
 - UTC is not a time zone, but a time standard that is the basis for 
   civil time and time zones worldwide. This means that no country or 
   territory officially uses UTC as a local time. 

_______________________________________________________________________________
UTC, GMT and Daylight Saving Time

 Neither UTC nor GMT ever change for Daylight Saving Time (DST). 
 However, some of the countries that use GMT switch to different time zones 
 during their DST period.
 
- http://geography.about.com/od/timeandtimezones/a/gmtutc.htm
"""

##-----------------------------------------------------------------------------
"""
Others:
# import calendar
#  - cal = calendar.month(2015, 1) => Jan 2015
#  - 
#  - 
"""
