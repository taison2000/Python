# -----------------------------------------------------------------------------
# 			Hunter Industries
#
# updated       Description
# ---------------------------------------------
# 05/27/2015   	 Initial Release
#
# -----------------------------------------------------------------------------

##-----------------------------------------------------------------------------

from collections import OrderedDict


gbRetrieveResp = b'\xFF\xFF\x3C\xC3\x82\x00\xC1\x01\x00\x01\x00\x0B\xA5\xBD'
gbRetrieveCmd = b'\xFF\xFF\x3C\xC3\x82\x00\xA9\x01\x00\x03\x00\x0B\x01\x00\x70\x2D'

gdRetrieveSave = OrderedDict ([
  ('Preamble', b'\xFF\xFF\x3C\xC3'), # Byte[0:3]
  ('SystemId', b'\x82'),    # Byte[4]
  ('SiteId', b'\x00'),      # Byte[5]
  ('Fcb', b'\xA9'),         # Byte[6]
  ('DeviceId', b'\x01\x00'),# Byte[7:8]
  ('Len', b'\x03\x00'),     # Byte[9:10]- LEN (from Command ID to end of data not including CRC)
  ('CommandId' , b'\x0B'),  # Byte[11]
  ('RetFunc' , b'\x01'),    # Byte[12]
  ('RetNum' , b'\x00'),     # Byte[13]
  ('Checksum', b'\x70\x2D') # Byte[14:15]
])


##-----------------------------------------------------------------------------
## Multi-dimension dictionary array
##-----------------------------------------------------------------------------
odTuple = OrderedDict ([
  ('Preamble',  (b'\xFF\xFF\x3C\xC3', 4)),  # Byte[0:3]
  ('SystemId',  (b'\x82', 1)),              # Byte[4]
  ('SiteId',    (b'\x00', 1)),              # Byte[5]
  ('Fcb',       (b'\xA9', 1)),              # Byte[6]
  ('DeviceId',  (b'\x01\x00', 2)),          # Byte[7:8]
  ('Len',       (b'\x03\x00', 2)),          # Byte[9:10]
  ('CommandId', (b'\x0B', 1)),              # Byte[11]
  ('RetFunc',   (b'\x01', 1)),              # Byte[12]
  ('RetNum',    (b'\x00', 1)),              # Byte[13]
  ('Checksum',  (b'\x70\x2D', 2))           # Byte[14:15]
])

odList = OrderedDict ([
  ('Preamble',  [b'\xFF\xFF\x3C\xC3', 4]),  # Byte[0:3]
  ('SystemId',  [b'\x82', 1]),              # Byte[4]
  ('SiteId',    [b'\x00', 1]),              # Byte[5]
  ('Fcb',       [b'\xA9', 1]),              # Byte[6]
  ('DeviceId',  [b'\x01\x00', 2]),          # Byte[7:8]
  ('Len',       [b'\x03\x00', 2]),          # Byte[9:10]
  ('CommandId', [b'\x0B', 1]),              # Byte[11]
  ('RetFunc',   [b'\x01', 1]),              # Byte[12]
  ('RetNum',    [b'\x00', 1]),              # Byte[13]
  ('Checksum',  [b'\x70\x2D', 2])           # Byte[14:15]
])

## Note: 
#odTuple['Len'] = (b'\x13\x12\x33', 3) #==> OK
#odList['Len'] = [b'\x13\x12\x33', 3]  #==> OK

#odTuple['Len'][1] = 3 ##<= NOT OK (Can't change Tuple)
#odList['Len'][1] = 3##<= OK


def printDict (dictData):
  for k in dictData:
    print (k, ':', dictData[k])

def printByteArrayDict (dictData):
  for k in dictData:
    s=''
    for j in dictData[k]:
      s+=format(j, '02X')+' '
    print (k, ':', s)



def AnalysisOrderedDictEachFieldLength ():
  global odTuple
  
  ## print out the size of each field
  for k in odTuple:
    print ("Vaule:%s Size:%d" %(odTuple[k][0], odTuple[k][1]))
  return;


##-----------------------------------------------------------------------------
if __name__=="__main__":
  AnalysisOrderedDictEachFieldLength()
  

##-----------------------------------------------------------------------------
"""
Resources:
 - 

"""
