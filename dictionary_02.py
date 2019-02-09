#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
  dictionary
  ~~~~~~~~~~~~~~~~~~~~~~
"""
import os
import time

"""
noStrKeyDict = {
bPreamble : b'\xFF\xff\x3C\xC3',\
bSystemId : b'\x88',\
bSiteId : b'\x00',\
bFcb : b'\x00',\
bDeviceId : b'\x01\x00',\
bLen : b'\x14\x00',\
bCommandId : b'\x01',\
bFwVer : b'\x00',\
bEngRev : b'\x00',\
bSize : b'\x06\x00',\
bHours : b'\x00',\
bMinutes : b'\x00',\
bSeconds : b'\x00',\
bMonth : b'\x00',\
bDay : b'\x00',\
bYear : b'\xDF\x07',\
bSysDcHour : b'\x00',\
bFcpDcHour : b'\x00',\
bOptions : b'\x00',\
bCurEtap : b'\x00',\
bMaxEtap : b'\x00',\
bResponse : b'\x00',\
bReportInterval : b'\x00',\
bOptStatus : b'\x00',\
bOffStatus : b'\x00',\
bGblSeasAdj : b'\x00\x00',\
bStackMode : b'\x00',\
bSsPrgThold : b'\x00',\
bSsgSsPrgThold : b'\x00',\
bRotaryKnob : b'\x00'
}
"""
## Note: when print out a dictionary, items might NOT be in same order as list below
bCurGlobal = {
  'Preamble' : b'\xFF\xff\x3C\xC3',
  'SystemId' : b'\x88',
  'SiteId' : b'\x00',
  'Fcb' : b'\x00',
  'DeviceId' : b'\x01\x00',
  'Len' : b'\x14\x00',
  'CommandId' : b'\x01',
  'FwVer' : b'\x00',
  'EngRev' : b'\x00',
  'Size' : b'\x06\x00',
  'Hours' : b'\x00',
  'Minutes' : b'\x00',
  'Seconds' : b'\x00',
  'Month' : b'\x00',
  'Day' : b'\x00',
  'Year' : b'\xDF\x07',
  'SysDcHour' : b'\x00',
  'FcpDcHour' : b'\x00',
  'Options' : b'\x00',
  'CurEtap' : b'\x00',
  'MaxEtap' : b'\x00',
  'Response' : b'\x00',
  'ReportInterval' : b'\x00',
  'OptStatus' : b'\x00',
  'OffStatus' : b'\x00',
  'GblSeasAdj' : b'\x00\x00',
  'StackMode' : b'\x00',
  'SsPrgThold' : b'\x00',
  'SsgSsPrgThold' : b'\x00',
  'RotaryKnob' : b'\x00'
}

def isKeyExist( key, dictData ):
    if key in dictData.keys():
        return True
    else:
        return False

def manual_iterate_dictionary( dictionary ):
    it = iter( dictionary )
    
    #for item in next(it): print(item)
    
    try:
        while True:
            item = next( it )
            print( item )
    except StopIteration:
        print( "***** Exception StopIteration catched *****")

    return

def try_this():
    manual_iterate_dictionary( bCurGlobal )

    return


def main():

    try_this()

    print( bCurGlobal )  # Print entire dictionary, Notice the output is not the same order

    # access using items
    print( '\nfor loop access using ITEMS method' )
    for k, v in bCurGlobal.items():
        print ('%-15s' % k, ':', v) ## left-aligned if when minus(-) sign
        #print ('%15s' % k, ':', v) ## right-aligned if NO minus(-) sign

    print ('\nfor loop access using KEYS method')
    for k in bCurGlobal:
        print ('%-15s' % k, ':', bCurGlobal[k])
    
    print ('\nfor loop access using VALUES method')
    for v in bCurGlobal.values():
        print (v)

# -----------------------------------------------------------------------------
# Code entry
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
    #msg = main()
    #print(msg)
    #mainloop()

