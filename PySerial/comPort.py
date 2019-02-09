# 			CIS1021 internal ONLY
# updated power-up seq  5/27/2010
# 12/7/10   	Added loop test
# 12/9/10	changed to 282Mhz setFreq
# 12/10/10	#adding swrbbits and srdb
# 12/12/3/10  	updated mode hgt/lgt for main output --revserse
# 12/15/10    	corrected typo lgb/hgb
#		added more mif files
# 01/20/10  	updated to similar for enmap2001 
#			2 pipeline delay and GS no prescan based
#			adding setcam1021gbasef for integration with lines l--lap
# 2/17		Corrected to use setroi1length1021 for setting ROI1 default is zero!!!!
#		Corrected to use Lines instead of VROI1!!!
#2/17/11	Added setprescanlength1021(Lines) for integration time adding additional prescan lines; def is 16
#2/27/11	added 4 more reg read for readall()
#2/28/11	tx1 goes from 3 to 20 to 3 to 46 to get 1us-- bad lines in middle of frame but defects are OK
#3/1/11		changed setfavlwave address from 3/4 to 0/1
#3/8/11		took /commented out swr and swrbits
#		replace j by s in jwrsensorbitsb 3 spots
#4/13/11   Added more wait time in init1021 and moved final READ rise to after all powerups (sm)
#
# 4/18/11 added Tx2 added for bot cut int by 1/2
# 4/19/11 changed init1021global to correct FVAL to DATA_SEL timing (Data_sel comes 2 LVAL's before FVAL)

import sys
import time
import SystemConfig1021
import pywin.debugger



def opencom(COMPort):
	"""
	Open the serial port with 4800 bps
	"""
	import serial
	global ser
	ser=serial.Serial(COMPort-1,4800,timeout=1)

def closecom():
	"""
	Close serial port
	"""
	global ser
	ser.close()

def getGlobal():
    ser.write(b'\xFF\xFF\xFF\x3C\xC3\x88\x00\xA9\x01\x00\x01\x00\x02\xF7\xB2') 
    data = ser.read(50)  # Read 50 bytes

def write(Address,Data): #write to CIS2051 test camera
	"""
	Write a list of values to the camera
	the format is write(Address,[Data0,Data1,...])
	"""
	import serial
	global ser
	#print "Write to address: ",Address
	OutString = chr(0x80 + (len(Data) & 0x7f))
	OutString = OutString + chr((Address & 0xff000000) >> 24)
	OutString = OutString + chr((Address & 0x00ff0000) >> 16)
	OutString = OutString + chr((Address & 0x0000ff00) >> 8)
	OutString = OutString + chr(Address & 0x000000ff)
	for i in range(0,len(Data)):
		#print "Data[",i,"]=",Data[i]
		OutString = OutString + chr((Data[i] & 0xff000000) >> 24)
		OutString = OutString + chr((Data[i] & 0x00ff0000) >> 16)
		OutString = OutString + chr((Data[i] & 0x0000ff00) >> 8)
		OutString = OutString + chr(Data[i] & 0x000000ff)
	#print "Output string: " ,OutString
	ser.write(OutString)

def read(Address,Size): #read from CIS2051 test camera
	"""
	Read a list of values from the camera
	the format is read(Address,Size) the returned value is
	a list from the type [Data0,Data1,...Datan]
	"""
	#global ser
	#print "Read from address: ",Address
	OutString = chr(0x00 + (Size & 0x7f))
	OutString = OutString + chr((Address & 0xff000000) >> 24)
	OutString = OutString + chr((Address & 0x00ff0000) >> 16)
	OutString = OutString + chr((Address & 0x0000ff00) >> 8)
	OutString = OutString + chr(Address & 0x000000ff)
	#print OutString
	ser.write(OutString)
	InString=ser.read((Size*4))
	if len(InString)<>Size*4:
			print ()
			print ("---------------------------------------------------")
			print ("| Serial port timeout!!!                          |")
			print ("| ======================                          |")
			print ("| Please check serial cable connections           |")
			print ("| or recycle power to the board                   |")
			print ("---------------------------------------------------")
			print ()
			print ()
			sys.exit(1)
	#print "reading from serial port"
	#InString=ser.read(512)
	#print InString
	Data=[]
	for i in range (0,Size*4-1,4):
		ThisData = (ord(InString[i])<<24)|(ord(InString[i+1])<<16)|(ord(InString[i+2])<<8)|ord(InString[i+3])
		Data.append(ThisData)
	#for i in range (0,len(Data)):
	    #print hex(Data[i])
	#if len(Data)==0 : print "Serial RX timeout!!!"
	return Data

def rd(Address):
	a=read(Address,1)[0]
	print a," (",hex(a),")"
	
def wr(Address,Data):
	write(Address,[Data])

#def swr(Address,Data):
#	"""
#	Write to the sensor regsiter (offset 0x0e000080)
#	The format is swr(Address,Data) where Address is 0-47
#	and Data is 32 bit value
#	"""
#	write(0x0f000080+Address,[Data])


	
##def swrbits(Address,MSB,LSB,Value):
#	"""
#	sensor write bits
#	Change bits msb:lsb from the original value read from the sensor address
#	to the new value
#	
#	The format is swrbits(Address,msb,lsb,value) 
#	"""
#	number=read(0x0f000080+Address,1)[0]
#	print "Original:", number," (",hex(number),")"
#	number=setbits(number,MSB,LSB,Value)
#	print "New value:", number," (",hex(number),")"
#	swr(Address,number)	

#bot ONLy
def swrb(Address,Data):
	"""
	Write to the sensor regsiter (offset 0x0f000080)
	The format is swr(Address,Data) where Address is 0-47
	and Data is 32 bit value
	"""
	write(0x0f000080+Address,[Data])
	
def swrbbits(Address,MSB,LSB,Value):
	"""
	sensor write bits
	Change bits msb:lsb from the original value read from the sensor address
	to the new value
	
	The format is swrbbits(Address,msb,lsb,value) 
	"""
	number=read(0x0f000080+Address,1)[0]
	print "Original:", number," (",hex(number),")"
	number=setbits(number,MSB,LSB,Value)
	print "New value:", number," (",hex(number),")"
	swrb(Address,number)
	
def srdb(Address):
	"""
	sensor read
	The format is srd(Address) where Address is 0-47
	"""
	a=read(0x0f000080+Address,1)[0]
	print a," (",hex(a),")"	
#	
	
	
	
	
	
	
def srd(Address):
	"""
	sensor read
	The format is srd(Address) where Address is 0-47
	"""
	a=read(0x0e000080+Address,1)[0]
	print a," (",hex(a),")"


def lbwrite(string): #loopback write to CIS2051 test camera
	"""
	Serial port loopback test write
	lbwrite("Hello")
	"""

	global ser
	ser.write(string)

def lbread(): #loopback read from CIS2051 test camera
	"""
	Serial port loopback test read
	lbread()
	"""
	global ser
	string = ser.read(100)
	return(string)


def init1021():
	"""
	Initialize com port and test camera registers for CIS2051 sensor
	"""
	import time
	
	try:
		opencom(SystemConfig1021.ComPort)
	except:
		print "COM port is open"
	else:
		print "COM port is open"

	#flush serial port
	read(4,4)

	#Enable power 1st dvddio
	write(2,[0x4])
	time.sleep(0.1)

	#Enable power dvddio+ DVDD
	write(0x00000002,[0x5])
	time.sleep(0.1)

	#orig write(2,[0xf85]) 		#Enable ONLY DVDD and DVDDIO
	#orig time.sleep(0.1)

	#Board Soft Reset - same as pushbutton
	write(0,[4])
	time.sleep(0.1)

	#Check board revision number
	print 'FPGA rev = ',read(4,1)[0],'.',read(5,1)[0],'.',read(6,1)[0]
	# was orig                    write(2,[0xfff])  #Power supplies to sensor enabled

	#Set clock divider of the sensor SPI controller 
	#write(0xe000000,[1]) # 1 - 22MHz; 2 - 15MHz 	  
	#write(0xe000001,[1]) # 1 - 22MHz; 2 - 15MHz 	  
	write(0xf000000,[1]) # 1 - 22MHz; 2 - 15MHz 	
	write(0xf000001,[1]) # 1 - 22MHz; 2 - 15MHz 	


	#Setup CLController for mode 0
	#write(0x3000000,[0])

	#Set clock frequency
	setfreq(SystemConfig1021.SensorFreq)

	#Set JTAG controller
	#write(0x14000000,[0x7F])#0x7F=5.31MHz ,0x4F=21.25MHz(works) ,0x4B=28.33MHz ,0x47=42.5MHz  'CLK must be inverted (bit 6 on)
	#write(0x15000000,[0x7F])#0x7F=5.31MHz ,0x4F=21.25MHz(works) ,0x4B=28.33MHz ,0x47=42.5MHz  'CLK must be inverted (bit 6 on)

	#Set top/bot to sync mode
	#write(0x06000000,[0x2000])
	write(0x07000000,[0x2000])

	#Release sensor reset
	#write(0x6000000,[0x2001])
	#write(0x7000000,[0x2001])

	#???????????????
	time.sleep(0.1)

	#Release sensor reset
	#write(0x6000000,[0x2001])
	write(0x7000000,[0x2001])
	
	time.sleep(0.1)

	#Set READ to high
	#write(0x06000000,[0x2041])
	#write(0x07000000,[0x2041])

	WriteWaveTables1021()
	
	#Enable power to AVDD+DVDD+DVDD_IO
	write(2,[0xd])
	time.sleep(0.1)

	#enable the rest of power
	write(2,[0xfff]) 		#enable all power supplies
	time.sleep(0.1)

	#Enable data path
	#Enable data path
	write(0x0,[0]) 		#leds off
	write(0x0,[0xA]) 	#data path enable and camera link tx enable
	write(0x1,[0xFF]) #clear error flags

	write(0x07000000,[0x2041])

	

def init1021NP():
	"""
	Initialize com port and test camera registers for CIS2051 sensor
	"""
	import time
	
	try:
		opencom(SystemConfig1021.ComPort)
	except:
		print ("COM port is open")
	else:
		print ("COM port is open")

	#flush serial port
	read(4,4)

	#Enable power
	#Enable power
	#write(2,[0xf85]) 		#Enable ONLY DVDD and DVDDIO
	write(2,[0x0])
	time.sleep(0.1)

	#Board Soft Reset - same as pushbutton
	write(0,[4])
	time.sleep(0.1)

	#Check board revision number
	print 'FPGA rev = ',read(4,1)[0],'.',read(5,1)[0],'.',read(6,1)[0]
	#write(2,[0xfff])  #Power supplies to sensor enabled

	#Set clock divider of the sensor SPI controller 
	write(0xe000000,[1]) # 1 - 22MHz; 2 - 15MHz 	  
	write(0xe000001,[1]) # 1 - 22MHz; 2 - 15MHz 	  
	write(0xf000000,[1]) # 1 - 22MHz; 2 - 15MHz 	
	write(0xf000001,[1]) # 1 - 22MHz; 2 - 15MHz 	


	#Setup CLController for mode 0
	write(0x3000000,[0])

	#Set clock frequency
	setfreq(SystemConfig1021.SensorFreq)

	#Set JTAG controller
	write(0x14000000,[0x7F])#0x7F=5.31MHz ,0x4F=21.25MHz(works) ,0x4B=28.33MHz ,0x47=42.5MHz  'CLK must be inverted (bit 6 on)
	write(0x15000000,[0x7F])#0x7F=5.31MHz ,0x4F=21.25MHz(works) ,0x4B=28.33MHz ,0x47=42.5MHz  'CLK must be inverted (bit 6 on)

	#Set top/bot to sync mode
	write(0x06000000,[0x2000])
	write(0x07000000,[0x2000])

	#Release sensor reset
	write(0x6000000,[0x2001])
	write(0x7000000,[0x2001])

	#???????????????
	time.sleep(0.1)

	#Release sensor reset
	write(0x6000000,[0x2001])
	write(0x7000000,[0x2001])

	#Set READ to high
	write(0x06000000,[0x2041])
	write(0x07000000,[0x2041])

	#WriteWaveTables2051()
	
	#Enable power to AVDD
	#write(2,[0xfff]) 		#enable all power supplies

	#Enable data path
	#Enable data path
	write(0x0,[0]) 		#leds off
	write(0x0,[0xA]) 	#data path enable and camera link tx enable
	write(0x1,[0xFF]) #clear error flags

def WriteWaveTables1021():

	SavedDataPath	=read(0x0000000,1)
	SavedSensorCtlB	=read(0x7000000,1)
	SavedModeReg2B 	=read(0xf000082,1)


	#first, READ needs to be high before changing reg2 bit 21
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFFF) | 0x0041])

	#set read as read so dont disturb GS
	write(0xF000082,[(SavedModeReg2B[0] & 0x035FFFFF) | 0x00000000])

	#now pause/reset it
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFBF) | 0x0001])

	#now datasel direct and set read to 0 
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFDBF) | 0x0001])

	#now datasel high
	write(0x7000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x1001])

	#Write Wavetable A
	#f=open('X:\\cameras\\projects\\CIS2051\\electrical\\test_software\\PythonScripts\\WaveTable.csv','r')
	f=open(SystemConfig1021.WaveTableFileName,'r')
	a=f.read()
	print "WaveTable A"
	for i in range (0,32):
		b='0x'+a[i*9:i*9+8]
		print 31-i,"->",b
		write(0x0F000090+31-i,[int(b,0)])

	
	time.sleep(.1)
	# now datasel low
	write(0x7000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x0001])

	#Wavetable B
	print "WaveTable B"
	for i in range (32,64):
		b='0x'+a[i*9:i*9+8]
		print 63-i,"->",b
		write(0x0F000090+63-i,[int(b,0)])

	# now datasel direct or auto as before
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFBF) | 0x0001]) 	#+resetb -read

	#READ high
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFFF) | 0x0041]) 	#+resetb +read

	#restore conditions...
	write(0xF000082,SavedModeReg2B)
	write(0x7000000,SavedSensorCtlB)

	write(0x0,[SavedDataPath[0] & 0xFFFD]) 	#clear datapath fifo
	write(0x0,SavedDataPath) 			#let it go again


def WriteWaveTables2051():
	SavedDataPath	=read(0x0000000,1)
	SavedSensorCtlT	=read(0x6000000,1)
	SavedSensorCtlB	=read(0x7000000,1)
	SavedModeReg2T 	=read(0x1000042,1)
	SavedModeReg2B 	=read(0x2000042,1)


	#first, READ needs to be high before changing reg2 bit 21
	write(0x6000000,[(SavedSensorCtlT[0] & 0xFFFF) | 0x0041])
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFFF) | 0x0041])

	#set read as read so dont disturb GS
	write(0x1000042,[(SavedModeReg2T[0] & 0x035FFFFF) | 0x00000000])
	write(0x2000042,[(SavedModeReg2B[0] & 0x035FFFFF) | 0x00000000])

	#now pause/reset it
	write(0x6000000,[(SavedSensorCtlT[0] & 0xFFBF) | 0x0001])
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFBF) | 0x0001])

	#now datasel direct
	write(0x6000000,[(SavedSensorCtlT[0] & 0xFDBF) | 0x0001])
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFDBF) | 0x0001])

	#now datasel high
	write(0x6000000,[(SavedSensorCtlT[0] & 0xEDBF) | 0x1001])
	write(0x7000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x1001])

	#Write Wavetable A for top    
	write(0x0100006F,[0x07FC008C])
	write(0x0100006E,[0x0410048C])
	write(0x0100006D,[0x13FD049D])
	write(0x0100006C,[0x15098C1D])
	write(0x0100006B,[0x00548C1D])
	write(0x0100006A,[0x065C9C1D])
	write(0x01000069,[0x0D508C1D])
	write(0x01000068,[0x1698841D])
	write(0x01000067,[0x1FE4E41D])
	write(0x01000066,[0x1FE4441D])
	write(0x01000065,[0x13DC041D])
	write(0x01000064,[0x0510001D])
	write(0x01000063,[0x070C001F])
	write(0x01000062,[0x01A4001E])
	write(0x01000061,[0x0A2C030E])
	write(0x01000060,[0x0CFC0302])
	write(0x0100005F,[0x07FC0342])
	write(0x0100005E,[0x0A2C0302])
	write(0x0100005D,[0x13FC0322])
	write(0x0100005C,[0x0CFC032E])
	write(0x0100005B,[0x08E8038E])
	write(0x0100005A,[0x08E8018E])
	write(0x01000059,[0x07FC008C])
	write(0x01000058,[0x07FC008C])
	write(0x01000057,[0x07FC008C])
	write(0x01000056,[0x07FC008C])
	write(0x01000055,[0x07FC008C])
	write(0x01000054,[0x07FC008C])
	write(0x01000053,[0x07FC008C])
	write(0x01000052,[0x07FC008C])
	write(0x01000051,[0x07FC008C])
	write(0x01000050,[0x1080008C])
	                              
	#Write Wavetable A for bottom 
	write(0x0200006F,[0x1080008C])
	write(0x0200006E,[0x13FC009D])
	write(0x0200006D,[0x0270001D])
	write(0x0200006C,[0x1474041D])
	write(0x0200006B,[0x01518C1D])
	write(0x0200006A,[0x01508C1D])
	write(0x02000069,[0x19949C1D])
	write(0x02000068,[0x0D508C1D])
	write(0x02000067,[0x1698841D])
	write(0x02000066,[0x1FE4E41D])
	write(0x02000065,[0x1FE4441D])
	write(0x02000064,[0x13FC041D])
	write(0x02000063,[0x070C041F])
	write(0x02000062,[0x1BE8041E])
	write(0x02000061,[0x14B4001E])
	write(0x02000060,[0x0A2C030E])
	write(0x0200005F,[0x0CFC0302])
	write(0x0200005E,[0x07FC0342])
	write(0x0200005D,[0x0A2C0302])
	write(0x0200005C,[0x13FC0322])
	write(0x0200005B,[0x0CFC032E])
	write(0x0200005A,[0x08E8038E])
	write(0x02000059,[0x08E8018E])
	write(0x02000058,[0x07FC008C])
	write(0x02000057,[0x07FC008C])
	write(0x02000056,[0x07FC008C])
	write(0x02000055,[0x07FC008C])
	write(0x02000054,[0x07FC008C])
	write(0x02000053,[0x07FC008C])
	write(0x02000052,[0x07FC008C])
	write(0x02000051,[0x07FC008C])
	write(0x02000050,[0x0A10008C])
	                              
	                              
	# now datasel low             
	write(0x6000000,[(SavedSensorCtlT[0] & 0xEDBF) | 0x0001])
	write(0x7000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x0001])
	                              
	#Wavetable B for top          
	write(0x0100006F,[0x07FC008C])
	write(0x0100006E,[0x0410048C])
	write(0x0100006D,[0x13FD049D])
	write(0x0100006C,[0x15090C1D])
	write(0x0100006B,[0x00540C1D])
	write(0x0100006A,[0x065C1C1D])
	write(0x01000069,[0x0D500C1D])
	write(0x01000068,[0x1698041D])
	write(0x01000067,[0x1FE4A41D])
	write(0x01000066,[0x054C841D])
	write(0x01000065,[0x12D0801D])
	write(0x01000064,[0x150C001D])
	write(0x01000063,[0x070C001F])
	write(0x01000062,[0x01A4001E])
	write(0x01000061,[0x0A2C030E])
	write(0x01000060,[0x0CFC0302])
	write(0x0100005F,[0x07FC0342])
	write(0x0100005E,[0x0A2C0302])
	write(0x0100005D,[0x13FC0322])
	write(0x0100005C,[0x0CFC032E])
	write(0x0100005B,[0x08E8038E])
	write(0x0100005A,[0x08E8018E])
	write(0x01000059,[0x07FC008C])
	write(0x01000058,[0x07FC008C])
	write(0x01000057,[0x07FC008C])
	write(0x01000056,[0x07FC008C])
	write(0x01000055,[0x07FC008C])
	write(0x01000054,[0x07FC008C])
	write(0x01000053,[0x07FC008C])
	write(0x01000052,[0x07FC008C])
	write(0x01000051,[0x07FC008C])
	write(0x01000050,[0x1080008C])
	                              
	#Wavetable B for bottom       
	write(0x0200006F,[0x1080008C])
	write(0x0200006E,[0x13FC009D])
	write(0x0200006D,[0x0270001D])
	write(0x0200006C,[0x1474041D])
	write(0x0200006B,[0x01518C1D])
	write(0x0200006A,[0x01508C1D])
	write(0x02000069,[0x19949C1D])
	write(0x02000068,[0x0D508C1D])
	write(0x02000067,[0x1698841D])
	write(0x02000066,[0x1FE4E41D])
	write(0x02000065,[0x1FE4441D])
	write(0x02000064,[0x13FC041D])
	write(0x02000063,[0x070C041F])
	write(0x02000062,[0x1BE8041E])
	write(0x02000061,[0x14B4001E])
	write(0x02000060,[0x0A2C030E])
	write(0x0200005F,[0x0CFC0302])
	write(0x0200005E,[0x07FC0342])
	write(0x0200005D,[0x0A2C0302])
	write(0x0200005C,[0x13FC0322])
	write(0x0200005B,[0x0CFC032E])
	write(0x0200005A,[0x08E8038E])
	write(0x02000059,[0x08E8018E])
	write(0x02000058,[0x07FC008C])
	write(0x02000057,[0x07FC008C])
	write(0x02000056,[0x07FC008C])
	write(0x02000055,[0x07FC008C])
	write(0x02000054,[0x07FC008C])
	write(0x02000053,[0x07FC008C])
	write(0x02000052,[0x07FC008C])
	write(0x02000051,[0x07FC008C])
	write(0x02000050,[0x0A10008C])
	
	# now datasel direct or auto as before
	write(0x6000000,[(SavedSensorCtlT[0] & 0xFFBF) | 0x0001]) 	#+resetb -read
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFBF) | 0x0001]) 	#+resetb -read

	#READ high
	write(0x6000000,[(SavedSensorCtlT[0] & 0xFFFF) | 0x0041]) 	#+resetb +read
	write(0x7000000,[(SavedSensorCtlB[0] & 0xFFFF) | 0x0041]) 	#+resetb +read

	#restore conditions...
	write(0x1000042,SavedModeReg2T)
	write(0x2000042,SavedModeReg2B)
	write(0x6000000,SavedSensorCtlT)
	write(0x7000000,SavedSensorCtlB)

	write(0x0,[SavedDataPath[0] & 0xFFFD]) 	#clear datapath fifo
	write(0x0,SavedDataPath) 			#let it go again


def WriteWaveTables2051LoadFile():
	#pywin.debugger.set_trace()
	SavedDataPath	=read(0x0000000,1)
	SavedSensorCtlT	=read(0x6000000,1)
	SavedSensorCtlB	=read(0x7000000,1)
	SavedModeReg2T 	=read(0x1000042,1)
	SavedModeReg2B 	=read(0x2000042,1)


	#first, READ needs to be high before changing reg2 bit 21
	write(0x06000000,[(SavedSensorCtlT[0] & 0xFFFF) | 0x0041])
	write(0x07000000,[(SavedSensorCtlB[0] & 0xFFFF) | 0x0041])

	#set read as read so dont disturb GS
	write(0x01000042,[(SavedModeReg2T[0] & 0x035FFFFF) | 0x00000000])
	write(0x02000042,[(SavedModeReg2B[0] & 0x035FFFFF) | 0x00000000])

	#now pause/reset it
	write(0x06000000,[(SavedSensorCtlT[0] & 0xFFBF) | 0x0001])
	write(0x07000000,[(SavedSensorCtlB[0] & 0xFFBF) | 0x0001])

	#now datasel direct
	write(0x06000000,[(SavedSensorCtlT[0] & 0xFDBF) | 0x0001])
	write(0x07000000,[(SavedSensorCtlB[0] & 0xFDBF) | 0x0001])

	#now datasel high
	write(0x06000000,[(SavedSensorCtlT[0] & 0xEDBF) | 0x1001])
	write(0x07000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x1001])

	#Write Wavetable A for top
	f=open(SystemConfig1021.WaveTableFileName,'r')
	a=f.read()
	print "WaveTable A top"
	for i in range (0,32):
		b='0x'+a[i*9:i*9+8]
		print 31-i,"->",b
		write(0x01000050+31-i,[int(b,0)])

	
	time.sleep(.1)
	
	#Wavetable A for bot
	print "WaveTable A bot"
	for i in range (64,96):
		b='0x'+a[i*9:i*9+8]
		print 95-i,"->",b
		write(0x02000050+95-i,[int(b,0)])



	## now datasel low
	write(0x06000000,[(SavedSensorCtlT[0] & 0xEDBF) | 0x0001])
	write(0x07000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x0001])

	#Wavetable B for top
	print "WaveTable B top"
	for i in range (32,64):
		b='0x'+a[i*9:i*9+8]
		print 63-i,"->",b
		write(0x02000050+63-i,[int(b,0)])

	
	time.sleep(.1)
	
	#Wavetable B for bot
	print "WaveTable B bot"
	for i in range (96,128):
		b='0x'+a[i*9:i*9+8]
		print 127-i,"->",b
		write(0x02000050+127-i,[int(b,0)])
	

	# now datasel direct or auto as before
	write(0x06000000,[(SavedSensorCtlT[0] & 0xFFBF) | 0x0001]) 	#+resetb -read
	write(0x07000000,[(SavedSensorCtlB[0] & 0xFFBF) | 0x0001]) 	#+resetb -read

	#READ high
	write(0x06000000,[(SavedSensorCtlT[0] & 0xFFFF) | 0x0041]) 	#+resetb +read
	write(0x07000000,[(SavedSensorCtlB[0] & 0xFFFF) | 0x0041]) 	#+resetb +read

	#restore conditions...
	write(0x01000042,SavedModeReg2T)
	write(0x02000042,SavedModeReg2B)
	write(0x06000000,SavedSensorCtlT)
	write(0x07000000,SavedSensorCtlB)

	write(0x0,[SavedDataPath[0] & 0xFFFD]) 	#clear datapath fifo
	write(0x0,SavedDataPath) 			#let it go again








def ReadWaveTables2051():
	"""
	Read and display top and bottom wavetables for CIS2051 sensor
	"""
	SavedSensorCtlT=read(0x06000000,1)[0]
	SavedSensorCtlB=read(0x07000000,1)[0]
	SavedModeReg2T =read(0x01000042,1)[0]
	SavedModeReg2B =read(0x02000042,1)[0]

	# Top sensor
	#------------
	DataSel=0x0000  #doesn't really matter, as read reset forces A read internally
	write(0x01000042,[(SavedModeReg2T & 0x037FFFFF)| 0x00200000])     #b23=0 b21=1 Set READ as reset
	write(0x02000042,[(SavedModeReg2B & 0x037FFFFF) | 0x00200000])    #b23=0 b21=1 Set READ as reset
	write(0x06000000,[DataSel | 1]) 	#resetb highbut read low gets to known point
	write(0x07000000,[DataSel | 1]) 	#resetb high
	write(0x01000042,[(SavedModeReg2T & 0x5FFFFF)])     #b23=0 b21=0 Set READ as pause
	write(0x02000042,[(SavedModeReg2B & 0x5FFFFF)])     #b23=0 b21=0 Set READ as pause
	write(0x06000000,[DataSel | 0x8001]) 	#ReadPauseMode (undocumented as of 0.7 top icd doc)
	write(0x07000000,[DataSel | 0x8001]) 	#ReadPauseMode (undocumented as of 0.7 top icd doc)
	
	#Table A
	WavetableR=[]
	for Reg in range(0,32):
		if Reg<11:
			DataSel=0x0000
		else :
			DataSel=0x1000
			
		Value=read(0x0100004e,1)[0] & 0x1FFFFFFF
		WavetableR.append(Value)
		lfsr = (Value / 0x40000) & 0x7FF
		Length = lfsr2lin(lfsr)
		write(0x06000013,[Length-1]) #set READ pulse length
		write(0x07000013,[Length-1]) #set READ pulse length
		write(0x06000000,[DataSel | 0x8041])   #pulse it
		write(0x07000000,[DataSel | 0x8041])   #pulse it

	print "WaveTable A top: ";
	for Reg in range(0,32):
		print hex(WavetableR[Reg]);" ";

	#Table B
	WavetableR=[]
	for Reg in range(0,32):
		if Reg<11:
			DataSel=0x0000
		else :
			DataSel=0x1000
			
		Value=read(0x0100004e,1)[0] & 0x1FFFFFFF
		WavetableR.append(Value)
		lfsr = (Value / 0x40000) & 0x7FF
		Length = lfsr2lin(lfsr)
		write(0x06000013,[Length-1]) #set READ pulse length
		write(0x07000013,[Length-1]) #set READ pulse length
		write(0x06000000,[DataSel | 0x8041])   #pulse it
		write(0x07000000,[DataSel | 0x8041])   #pulse it

	print "WaveTable B top: ";
	for Reg in range(0,32):
		print hex(WavetableR[Reg]);" ";


	# Bottom sensor
	#---------------
	DataSel=0x0000  #doesn't really matter, as read reset forces A read internally
	write(0x01000042,[(SavedModeReg2T & 0x037FFFFF)| 0x00200000])     #b23=0 b21=1 Set READ as reset
	write(0x02000042,[(SavedModeReg2B & 0x037FFFFF) | 0x00200000])    #b23=0 b21=1 Set READ as reset
	write(0x06000000,[DataSel | 1]) 	#resetb highbut read low gets to known point
	write(0x07000000,[DataSel | 1]) 	#resetb high
	write(0x01000042,[(SavedModeReg2T & 0x5FFFFF)])     #b23=0 b21=0 Set READ as pause
	write(0x02000042,[(SavedModeReg2B & 0x5FFFFF)])     #b23=0 b21=0 Set READ as pause
	write(0x06000000,[DataSel | 0x8001]) 	#ReadPauseMode (undocumented as of 0.7 top icd doc)
	write(0x07000000,[DataSel | 0x8001]) 	#ReadPauseMode (undocumented as of 0.7 top icd doc)
	
	#Table A
	WavetableR=[]
	for Reg in range(0,32):
		if Reg<11:
			DataSel=0x0000
		else :
			DataSel=0x1000
			
		Value=read(0x0200004e,1)[0] & 0x1FFFFFFF
		WavetableR.append(Value)
		lfsr = (Value / 0x40000) & 0x7FF
		Length = lfsr2lin(lfsr)
		write(0x06000013,[Length-1]) #set READ pulse length
		write(0x07000013,[Length-1]) #set READ pulse length
		write(0x06000000,[DataSel | 0x8041])   #pulse it
		write(0x07000000,[DataSel | 0x8041])   #pulse it

	print "WaveTable A bottom: ";
	for Reg in range(0,32):
		print hex(WavetableR[Reg]);" ";

	#Table B
	WavetableR=[]
	for Reg in range(0,32):
		if Reg<11:
			DataSel=0x0000
		else :
			DataSel=0x1000
			
		Value=read(0x0200004e,1)[0] & 0x1FFFFFFF
		WavetableR.append(Value)
		lfsr = (Value / 0x40000) & 0x7FF
		Length = lfsr2lin(lfsr)
		write(0x06000013,[Length-1]) #set READ pulse length
		write(0x07000013,[Length-1]) #set READ pulse length
		write(0x06000000,[DataSel | 0x8041])   #pulse it
		write(0x07000000,[DataSel | 0x8041])   #pulse it

	print "WaveTable B bottom: ";
	for Reg in range(0,32):
		print hex(WavetableR[Reg]);" ";




	#Restore values
	write(0x6000000,[SavedSensorCtlT])
	write(0x7000000,[SavedSensorCtlB])
	write(0x1000042,[SavedModeReg2T])  #restore
	write(0x2000042,[SavedModeReg2B])  #restore



def readall2051():
	for i in range(0,48):
		print hex(i),"-",hex(read(0x01000040+i,1)[0])
	for i in range(0,48):
		print hex(i),"-",hex(read(0x02000040+i,1)[0])
				


	
def cofcal(Mode):
	"""
	calibrate column offset correction block by calculating the column vectoe for a sequence of dark images
	The format is cofcal(Mode) where the mode can be one of the following:
	blg (bottom low gain)
	bhg (bottom high gain)
	tlg (top low gain)
	thg (top high gain)
	"""
	import Image 
	import numpy

	Mode=Mode.lower()
	if Mode == 'blg':
		print 'Bot LG'
		Address = 0x40001000
	elif Mode == 'tlg':
		print 'Top LG'
		Address = 0x20001000
	elif Mode == 'bhg':
		print 'Bot HG'
		Address = 0x41001000
	elif Mode == 'thg':
		print 'Top HG'
		Address = 0x21001000
	else:
		print 'unsupported mode'
		return

	mean=0
	im = Image.open("c:\\temp\\testimage.tif")
	im.seek(0) # skip to the second frame
	[w,h]=im.size
	while 1:
		#im.seek(im.tell()+1)
		#convert image file to numpy array
		im_ar = numpy.array(im.getdata()).reshape([h,w])

		#Calculate the mean vector
		im_mean=im_ar.mean(0)
		mean=mean+im_mean

		#Get the next image from the sequence
		try:
			im.seek(im.tell()+1)	
		except EOFError:
			break
	mean=mean/(im.tell()+1)
	mean=mean*(2**7)
	mean=mean/16
	mean=numpy.array(mean,dtype=int)

	#Reshape for easier writing to the memory
	mean=mean.reshape(32,81)
	for i in range(0,31):
		mean_li=mean[i].tolist()
		write(Address+i*81,mean_li)
		
def setfreq(Freq):
	"""
	Set PLL frequency
		Currently supports following frequencies (In MHZ):
		300 - 100 (10MZ intervals),82, 75, 60, 50, 42.85, 37.5
	"""
	#Path = r"C:\\CPP_Camera\\Python\\"
	#Path = r"X:\\cameras\\projects\\CIS2051\\electrical\\test_software\\PythonScripts\\"
	Path = SystemConfig1021.MIFFilesPath
	


	if Freq == 282:
		FileName = "1021_282MHZ.mif"
	elif Freq == 280:
		FileName = "1021_280MHZ.mif"
	elif Freq == 270:
		FileName = "1021_270MHZ.mif"
	elif Freq == 260:
		FileName = "1021_260MHZ.mif"
	elif Freq == 141:
		FileName = "1021_141MHz.mif"
	elif Freq == 210:
		FileName = "1021_210MHZ.mif"
	elif Freq == 200:
		FileName = "1021_200MHZ.mif"
	elif Freq == 190:
		FileName = "1021_190MHZ.mif"
	elif Freq == 220:
		FileName = "1021_220MHZ.mif"
	elif Freq == 230:
		FileName = "1021_230MHZ.mif"
	elif Freq == 240:
		FileName = "1021_240MHZ.mif"
	elif Freq == 250:
		FileName = "1021_250MHZ.mif"	
	elif Freq == 272:
		FileName = "1021_272MHZ.mif"
	elif Freq == 274:
		FileName = "1021_274MHZ.mif"
	elif Freq == 276:
		FileName = "1021_276MHZ.mif"
	elif Freq == 278:
		FileName = "1021_278MHZ.mif"
	elif Freq == 38:
		FileName = "1021_38MHZ.mif"
		
	else:
		print Freq, " is not a supported frequency. Use help testcam1 for supported frequencies"
		return

	ReadFile = Path + FileName
	try:
		f = open(ReadFile)
	except:
		print "File ", FileName," was not found!"
	else:
		print "Load timing file: ", FileName
		line = f.readline()
		while line != 'CONTENT BEGIN\n':
			line = f.readline()

		i=0
		line = f.readline()

		ScanReg=[0,0,0,0,0,0]
		for j in range(0,6):
			ScanReg[j]=0
			for i in range(0,32):
				if (j<5) |((j==5) & (i<14)):
					bit = line.split()[2]
					bit=bit.replace(";","")
					if bit=='1':
						ScanReg[j]=ScanReg[j] + 2**i

					line = f.readline()
					#print i,bit
					i=i+1

		#print "="*20
		#for j in range(0,6):
		#	print "Reg[",j,"]=",hex(ScanReg[j])

		write(0xa000002,ScanReg)
		write(0xa000000,[1])



def setfreq1021(Freq):
	"""
	Set PLL frequency
		Currently supports following frequencies (In MHZ):
		300 - 100 (10MZ intervals),82, 75, 60, 50, 42.85, 37.5
	"""
	#Path = r"C:\\CPP_Camera\\Python\\"
	#Path = r"X:\\cameras\\projects\\CIS2051\\electrical\\test_software\\PythonScripts\\"
	Path = SystemConfig1021.MIFFilesPath
	


	if Freq == 252:
		FileName = "1021_252MHZ.mif"
	elif Freq == 225:
		FileName = "1021_225MHZ.mif"
	elif Freq == 200:
		FileName = "1021_200MHZ.mif"
	elif Freq == 160:
		FileName = "1021_160MHZ.mif"
	elif Freq == 126:
		FileName = "1021_126MHZ.mif"
	elif Freq == 100:
		FileName = "1021_100MHZ.mif"
	elif Freq == 38:
		FileName = "1021_38MHZ.mif"

	else:
		print Freq, " is not a supported frequency. Use help testcam1 for supported frequencies"
		return

	ReadFile = Path + FileName
	try:
		f = open(ReadFile)
	except:
		print "File ", FileName," was not found!"
	else:
		print "Load timing file: ", FileName
		line = f.readline()
		while line != 'CONTENT BEGIN\n':
			line = f.readline()

		i=0
		line = f.readline()

		ScanReg=[0,0,0,0,0,0]
		for j in range(0,6):
			ScanReg[j]=0
			for i in range(0,32):
				if (j<5) |((j==5) & (i<14)):
					bit = line.split()[2]
					bit=bit.replace(";","")
					if bit=='1':
						ScanReg[j]=ScanReg[j] + 2**i

					line = f.readline()
					#print i,bit
					i=i+1

		#print "="*20
		#for j in range(0,6):
		#	print "Reg[",j,"]=",hex(ScanReg[j])

		write(0xa000002,ScanReg)
		write(0xa000000,[1])




def selectsensor(Side):
	"""
	Set camera link interface mode to select between the top and the bottom half.
	The format is selectsensor(Side) where the Side can be one of the following:
	'top'(tophalf of the sensor)
	'bot'(bottom half of the sensor)
	"""
	Side=Side.lower()
	if Side == 'lg':
		print 'Top half of the sensor low gain'
		write(0x3000000,[0]);
	elif Side == 'hg':
		print 'Bottom half of the sensor low gain'
		write(0x3000000,[1]);
	elif Side == 'lghg':
		print 'Top half of the sensor high  gain'
		write(0x3000000,[2]);
	elif Side == 'hglg':
		print 'Bottom half of the sensor high  gain'
		write(0x3000000,[3]);
	else:
		print 'Error!'


	
def setmode1021(Mode):
	"""
	Set image capture mode.
	The format is setmode(Mode) where the Mode can be one of the following:
	Note: A full initialization is done before mode change
	'hg'(hg on both channels)
	'lg'(lg on both chanels)
	'hglg'(hg and lg)
	'lghg'(lg and hg)
	
	"""
	Mode=Mode.lower()
	if Mode == 'hg':
		print 'Raw low gain top--Aux Output'
		init1021()
		selectsensor('hg')
	elif Mode == 'lg':
		print 'Raw high gain top--Aux Output'
		init1021()
		selectsensor('lg')
	elif Mode == 'hglg':
		print 'Raw low gain bottom-- Main Output'
		init1021()
		selectsensor('hglg')						
	elif Mode == 'rhgb':
		print 'Raw high gain bottom -- Main Output'
		init1021()
		selectsensor('lghg')
		
	else:
		print 'Unsupported mode!'


def setmode1021NP(Mode):
	"""
	Set image capture mode.
	The format is setmode(Mode) where the Mode can be one of the following:
	Note: A full initialization is done before mode change
	'rlgt'(raw low gain top)
	'rhgt'(raw high gain top)
	'rlgb'(raw low gain bottom)
	'rhgb'(raw high gain bottom)
	
	"""
	Mode=Mode.lower()
	if Mode == 'rlgt':
		print 'Raw low gain top'
		init1021NP()
		selectsensor('top')
	
	elif Mode == 'rhgt':
		print 'Raw high gain top'
		init1021NP()
		selectsensor('top')
		
	elif Mode == 'rlgb':
		print 'Raw low gain bottom'
		init1021NP()
		selectsensor('bot')
		
	elif Mode == 'rhgb':
		print 'Raw high gain bottom'
		init1021NP()
		selectsensor('bot')
		
	else:
		print 'Unsupported mode!'

def lfsr2lin(lfsrvalue):
	table=[ \
	0,1019,1018,2037,1017,1008,2036,1570,1016,541,1007, \
	1154,2035,972,1569,2026,1015,997,540,776,1006,74, \
	1153,1990,2034,341,971,1559,1568,125,2025,277,1014, \
	1295,996,1523,539,58,775,1143,1005,1184,73,1359, \
	1152,530,1989,1266,2033,1705,340,2015,970,1794,1558, \
	439,1567,961,124,380,2024,1677,276,1092,1013,63, \
	1294,499,995,1289,1522,648,538,1499,57,1979,774, \
	1398,1142,892,1004,925,1183,676,72,986,1358,842, \
	1151,1457,529,1777,1988,828,1265,765,2032,898,1704, \
	266,339,494,2014,700,969,114,1793,625,1557,1624, \
	438,1076,1566,237,960,568,123,1344,379,1548,2023, \
	1327,1676,155,275,330,1091,1107,1012,78,62,1798, \
	1293,990,498,1348,994,1590,1288,298,1521,1173,647, \
	1698,537,918,1498,1255,56,1586,1978,209,773,519, \
	1397,230,1141,1203,891,315,1003,931,924,1916,1182, \
	1284,675,40,71,1718,985,354,1357,911,841,1512, \
	1150,47,1456,181,528,294,1776,595,1987,1903,827, \
	1132,1264,1643,764,1414,2031,1271,897,1081,1703,1517, \
	265,729,338,1666,493,1883,2013,1817,699,260,968, \
	1910,113,1234,1792,1169,624,369,1556,412,1623,470, \
	437,950,1075,1735,1565,1783,236,476,959,643,567, \
	1846,122,27,1343,428,378,748,1547,724,2022,188, \
	1326,1943,1675,1694,154,802,274,1860,329,609,1090, \
	662,1106,2004,1011,975,77,128,61,533,1797,1680, \
	1292,1401,989,831,497,1627,1347,333,993,1176,1589, \
	1206,1287,914,297,1646,1520,1820,1172,953,646,751, \
	1697,665,536,1630,917,754,1497,1494,1254,1449,55, \
	817,1585,857,1977,1491,208,1661,772,1742,518,1319, \
	1396,1251,229,1766,1140,106,1202,1045,890,1446,314, \
	1375,1002,1710,930,242,923,52,1915,193,1181,1747, \
	1283,1895,674,814,39,488,70,1278,1717,392,984, \
	1582,353,788,1356,1119,910,637,840,854,1511,511, \
	1149,706,46,1852,1455,1974,180,1968,527,19,293, \
	1430,1775,1488,594,1878,1986,1890,1902,881,826,205, \
	1131,404,1263,1387,1642,869,763,1658,1413,140,2030, \
	281,1270,1096,896,769,1080,1111,1702,319,1516,1418, \
	264,1739,728,2008,337,669,1665,1379,492,515,1882, \
	144,2012,11,1816,561,698,1316,259,7,967,1333, \
	1909,1866,112,1393,1233,174,1791,582,1168,1537,623, \
	1248,368,1812,1555,809,411,1936,1622,226,469,1476, \
	436,1227,949,98,1074,1763,1734,557,1564,385,1782, \
	160,235,1137,475,614,958,1050,642,874,566,103, \
	1845,694,121,34,26,1065,1342,1199,427,1605,377, \
	1613,747,1840,1546,1042,723,1312,2021,574,187,1949, \
	1325,887,1942,1962,1674,1058,1693,1219,153,1443,801, \
	255,273,483,1859,1956,328,311,608,1929,1089,168, \
	661,689,1105,1372,2003,3,1021,1010,543,974,999, \
	76,343,127,1297,60,1186,532,1707,1796,963,1679, \
	65,1291,1501,1400,927,988,1459,830,900,496,116, \
	1626,239,1346,1329,332,80,992,1592,1175,920,1588, \
	521,1205,933,1286,1720,913,49,296,1905,1645,1273, \
	1519,1668,1819,1912,1171,414,952,1785,645,29,750, \
	190,1696,1862,664,977,535,1403,1629,1178,916,1822, \
	753,1632,1496,819,1493,1744,1253,108,1448,1712,54, \
	1749,816,1280,1584,1121,856,708,1976,21,1490,1892, \
	207,1389,1660,283,771,321,1741,671,517,13,1318, \
	1335,1395,584,1250,811,228,1229,1765,387,1139,1052, \
	105,36,1201,1615,1044,576,889,1060,1445,485,313, \
	170,1374,1023,1001,1299,1709,67,929,902,241,82, \
	922,935,51,1275,1914,1787,192,979,1180,1634,1746, \
	1714,1282,710,1894,285,673,1337,813,389,38,578, \
	487,1025,69,84,1277,981,1716,287,391,1027,983, \
	1029,1581,1579,352,1164,787,1577,1355,1687,1118,350, \
	909,449,636,1162,839,1194,853,785,1510,1533,510, \
	1575,1148,653,705,1353,45,734,1851,1685,1454,198, \
	1973,1116,179,619,1967,348,526,1827,18,907,292, \
	739,1429,447,1774,422,1487,634,593,1244,1877,1160, \
	1985,304,1889,837,1901,1424,880,1192,825,941,204, \
	851,1130,364,403,783,1262,1213,1386,1508,1641,219, \
	868,1531,762,1600,1657,508,1412,1808,139,1573,2029, \
	1993,280,1146,1269,442,1095,651,895,845,768,703, \
	1079,1551,1110,1351,1701,212,318,43,1515,598,1417, \
	732,263,372,1738,1849,727,805,2007,1683,336,1649, \
	668,1452,1664,1769,1378,196,491,791,514,1971,1881, \
	407,143,1114,2011,147,10,177,1815,1479,560,617, \
	697,1608,1315,1965,258,1932,6,346,966,1462,1332, \
	524,1908,417,1865,1825,111,1124,1392,16,1232,1618, \
	173,905,1790,713,581,290,1167,452,1536,737,622, \
	742,1247,1427,367,222,1811,445,1554,601,808,1772, \
	410,1482,1935,420,1621,455,225,1485,468,465,1475, \
	632,435,1437,1226,591,948,462,97,1242,1073,1835, \
	1762,1875,1733,1472,556,1158,1563,1363,384,1983,1781, \
	629,159,302,234,358,1136,1887,474,432,613,835, \
	957,861,1049,1899,641,1434,873,1422,565,1541,102, \
	878,1844,1223,693,1190,120,1724,33,823,25,588, \
	1064,939,1341,1033,1198,202,426,945,1604,849,376, \
	795,1612,1128,746,459,1839,362,1545,1037,1041,401, \
	722,94,1311,781,2020,681,573,1260,186,1239,1948, \
	1211,1324,397,886,1384,1941,1070,1961,1506,1673,1754, \
	1057,1639,1692,1832,1218,217,152,718,1442,866,800, \
	1759,254,1529,272,1922,482,760,1858,1872,1955,1598, \
	327,90,310,1655,607,1730,1928,506,1088,249,167, \
	1410,660,1469,688,1806,1104,1307,1371,137,2002,553, \
	2,1020,2038,1009,1571,542,1155,973,2027,998,777, \
	75,1991,342,1560,126,278,1296,1524,59,1144,1185, \
	1360,531,1267,1706,2016,1795,440,962,381,1678,1093, \
	64,500,1290,649,1500,1980,1399,893,926,677,987, \
	843,1458,1778,829,766,899,267,495,701,115,626, \
	1625,1077,238,569,1345,1549,1328,156,331,1108,79, \
	1799,991,1349,1591,299,1174,1699,919,1256,1587,210, \
	520,231,1204,316,932,1917,1285,41,1719,355,912, \
	1513,48,182,295,596,1904,1133,1644,1415,1272,1082, \
	1518,730,1667,1884,1818,261,1911,1235,1170,370,413, \
	471,951,1736,1784,477,644,1847,28,429,749,725, \
	189,1944,1695,803,1861,610,663,2005,976,129,534, \
	1681,1402,832,1628,334,1177,1207,915,1647,1821,954, \
	752,666,1631,755,1495,1450,818,858,1492,1662,1743, \
	1320,1252,1767,107,1046,1447,1376,1711,243,53,194, \
	1748,1896,815,489,1279,393,1583,789,1120,638,855, \
	512,707,1853,1975,1969,20,1431,1489,1879,1891,882, \
	206,405,1388,870,1659,141,282,1097,770,1112,320, \
	1419,1740,2009,670,1380,516,145,12,562,1317,8, \
	1334,1867,1394,175,583,1538,1249,1813,810,1937,227, \
	1477,1228,99,1764,558,386,161,1138,615,1051,875, \
	104,695,35,1066,1200,1606,1614,1841,1043,1313,575, \
	1950,888,1963,1059,1220,1444,256,484,1957,312,1930, \
	169,690,1373,4,1022,544,1000,344,1298,1187,1708, \
	964,66,1502,928,1460,901,117,240,1330,81,1593, \
	921,522,934,1721,50,1906,1274,1669,1913,415,1786, \
	30,191,1863,978,1404,1179,1823,1633,820,1745,109, \
	1713,1750,1281,1122,709,22,1893,1390,284,322,672, \
	14,1336,585,812,1230,388,1053,37,1616,577,1061, \
	486,171,1024,1300,68,903,83,936,1276,1788,980, \
	1635,1715,711,286,1338,390,579,1026,85,982,288, \
	1028,1030,1580,1165,1578,1688,351,450,1163,1195,786, \
	1534,1576,654,1354,735,1686,199,1117,620,349,1828, \
	908,740,448,423,635,1245,1161,305,838,1425,1193, \
	942,852,365,784,1214,1509,220,1532,1601,509,1809, \
	1574,1994,1147,443,652,846,704,1552,1352,213,44, \
	599,733,373,1850,806,1684,1650,1453,1770,197,792, \
	1972,408,1115,148,178,1480,618,1609,1966,1933,347, \
	1463,525,418,1826,1125,17,1619,906,714,291,453, \
	738,743,1428,223,446,602,1773,1483,421,456,1486, \
	466,633,1438,592,463,1243,1836,1876,1473,1159,1364, \
	1984,630,303,359,1888,433,836,862,1900,1435,1423, \
	1542,879,1224,1191,1725,824,589,940,1034,203,946, \
	850,796,1129,460,363,1038,402,95,782,682,1261, \
	1240,1212,398,1385,1071,1507,1755,1640,1833,218,719, \
	867,1760,1530,1923,761,1873,1599,91,1656,1731,507, \
	250,1411,1470,1807,1308,138,554,2039,1572,1156,2028, \
	778,1992,1561,279,1525,1145,1361,1268,2017,441,382, \
	1094,501,650,1981,894,678,844,1779,767,268,702, \
	627,1078,570,1550,157,1109,1800,1350,300,1700,1257, \
	211,232,317,1918,42,356,1514,183,597,1134,1416, \
	1083,731,1885,262,1236,371,472,1737,478,1848,430, \
	726,1945,804,611,2006,130,1682,833,335,1208,1648, \
	955,667,756,1451,859,1663,1321,1768,1047,1377,244, \
	195,1897,490,394,790,639,513,1854,1970,1432,1880, \
	883,406,871,142,1098,1113,1420,2010,1381,146,563, \
	9,1868,176,1539,1814,1938,1478,100,559,162,616, \
	876,696,1067,1607,1842,1314,1951,1964,1221,257,1958, \
	1931,691,5,545,345,1188,965,1503,1461,118,1331, \
	1594,523,1722,1907,1670,416,31,1864,1405,1824,821, \
	110,1751,1123,23,1391,323,15,586,1231,1054,1617, \
	1062,172,1301,904,937,1789,1636,712,1339,580,86, \
	289,1031,1166,1689,451,1196,1535,655,736,200,621, \
	1829,741,424,1246,306,1426,943,366,1215,221,1602, \
	1810,1995,444,847,1553,214,600,374,807,1651,1771, \
	793,409,149,1481,1610,1934,1464,419,1126,1620,715, \
	454,744,224,603,1484,457,467,1439,464,1837,1474, \
	1365,631,360,434,863,1436,1543,1225,1726,590,1035, \
	947,797,461,1039,96,683,1241,399,1072,1756,1834, \
	720,1761,1924,1874,92,1732,251,1471,1309,555,2040, \
	1157,779,1562,1526,1362,2018,383,502,1982,679,1780, \
	269,628,571,158,1801,301,1258,233,1919,357,184, \
	1135,1084,1886,1237,473,479,431,1946,612,131,834, \
	1209,956,757,860,1322,1048,245,1898,395,640,1855, \
	1433,884,872,1099,1421,1382,564,1869,1540,1939,101, \
	163,877,1068,1843,1952,1222,1959,692,546,1189,1504, \
	119,1595,1723,1671,32,1406,822,1752,24,324,587, \
	1055,1063,1302,938,1637,1340,87,1032,1690,1197,656, \
	201,1830,425,307,944,1216,1603,1996,848,215,375, \
	1652,794,150,1611,1465,1127,716,745,604,458,1440, \
	1838,1366,361,864,1544,1727,1036,798,1040,684,400, \
	1757,721,1925,93,252,1310,2041,780,1527,2019,503, \
	680,270,572,1802,1259,1920,185,1085,1238,480,1947, \
	132,1210,758,1323,246,396,1856,885,1100,1383,1870, \
	1940,164,1069,1953,1960,547,1505,1596,1672,1407,1753, \
	325,1056,1303,1638,88,1691,657,1831,308,1217,1997, \
	216,1653,151,1466,717,605,1441,1367,865,1728,799, \
	685,1758,1926,253,2042,1528,504,271,1803,1921,1086, \
	481,133,759,247,1857,1101,1871,165,1954,548,1597, \
	1408,326,1304,89,658,309,1998,1654,1467,606,1368, \
	1729,686,1927,2043,505,1804,1087,134,248,1102,166, \
	549,1409,1305,659,1999,1468,1369,687,2044,1805,135, \
	1103,550,1306,2000,1370,2045,136,551,2001,2046,552, \
	2047,0]

	return table[lfsrvalue]

def setroi1length2051(Lines):	
	"""
	Set ROI1 length (in number of lines) for CIS2051 snsor
	"""
	#Save original SensrCtl values
	SavedSensrCtlT= read(0x6000000,1)[0]
	SavedSensrCtlB= read(0x7000000,1)[0]

	#stop!  (in the name of love.....)
	write(0x6000000,[SavedSensrCtlT & ~0x40])
	write(0x7000000,[SavedSensrCtlB & ~0x40])

	#set roi1 len for both halves        
	write(0x1000048,[Lines])
	write(0x2000048,[Lines])

	#restore SensrCtl
	write(0x6000000,[SavedSensrCtlT])
	write(0x7000000,[SavedSensrCtlB])

def setbits(number,msb,lsb,value):
	"""
	Change bits msb:lsb from teri original value in number to the new value
	"""
	mask=(2**(msb-lsb+1)-1)<<lsb
	number = number & ~mask
	number=number |(mask & (value<<lsb))
	return number

if __name__ == "__main__":
	import sys, PythonCall
	PythonCall.PythonCall(sys.argv).execute()

def	settestpattern1021():
	write(0x4000000,[1])
	write(0x5000000,[1])

def bringuppower():

	from msvcrt import getch
	opencom(SystemConfig1021.ComPort)
	print "press any key to begin Powering sequence";
	##x = getkey()
	##x = getch()
	##x = keyboard.read(100000, timeout = 0) 
	

	sys.stdin.readline()
	print "Powering DVDD_IO";
	write(2,[0x4])
	time.sleep(0.1)


	sys.stdin.readline()
	print "Powering DVDD_IO + DVDD";
	write(0x00000002,[0x5])
	time.sleep(0.1)

	#resetb release

	sys.stdin.readline()
	print "Powering AVDD + DVDD_IO + DVDD";
	write(2,[0xd])
	time.sleep(0.1)

	sys.stdin.readline()
	print "Powering VTX1N,VTX2N,ARST1,ARTS2,AVDD_pix + AVDD + DVDD_IO + DVD";
	write(2,[0x2d])
	time.sleep(0.1)
	
	
	sys.stdin.readline()
	print "Powering VTX12P + VTX1N,Vtx2N,ARST1,ARTS2,AVDD_pix + AVDD + DVDD_IO + DVD";
	write(2,[0x3d])
	time.sleep(0.1)

	#not needed
	#sys.stdin.readline()
	#print "Powering VNEG";
	#write(2,[0x5d])
	#time.sleep(0.1)	

	#Areset??

	sys.stdin.readline()
	print "Powering DVDD3 + VTX12P + VTX1N,Vtx2N,ARST1,ARTS2,AVDD_pix + AVDD + DVDD_IO + DVD";
	write(2,[0x3f])
	time.sleep(0.1)


	closecom()


	#added ----------------------------------------------6/19/2010

def readall1021():
	#for i in range(0,48):
	#	print hex(i),"-",hex(read(0x0e000080+i,1)[0])
	for i in range(0,48):
		print hex(i),"-",hex(read(0x0f000080+i,1)[0])
		
def readallcamlink():
	for i in range(0,2):
		print hex(i),"-",hex(read(0x03000000+i,1)[0])
	for i in range(0,2):
		print hex(i),"-",hex(read(0x04000000+i,1)[0])
	for i in range(0,2):
		print hex(i),"-",hex(read(0x05000000+i,1)[0])
		
def readallsensor():
	for i in range(0,16):
		print hex(i),"-",hex(read(0x06000000+i,1)[0])
	for i in range(0,21):
		print hex(i),"-",hex(read(0x07000000+i,1)[0])	
		
		

def jwrtbits(Address,MSB,LSB,Value):
	"""
	sensor write bits
	Change bits msb:lsb from the original value read from the sensor address
	to the new value
	
	The format is swrbits(Address,msb,lsb,value) 
	"""
	number=read(0x0e000080+Address,1)[0]
	print "Original:", number," (",hex(number),")"
	number=setbits(number,MSB,LSB,Value)
	print "New value:", number," (",hex(number),")"
	jwrt(Address,number)	

def jwrbbits(Address,MSB,LSB,Value):
	"""
	sensor write bits
	Change bits msb:lsb from the original value read from the sensor address
	to the new value
	
	The format is swrbits(Address,msb,lsb,value) 
	"""
	number=read(0x0f000080+Address,1)[0]
	print "Original:", number," (",hex(number),")"
	number=setbits(number,MSB,LSB,Value)
	print "New value:", number," (",hex(number),")"
	jwrb(Address,number)	

def jwrt(Address,Data):
	"""
	Write to the sensor regsiter (offset 0x0e000080)
	The format is swr(Address,Data) where Address is 0-47
	and Data is 32 bit value
	"""
	write(0x0e000080+Address,[Data])	

def jwrb(Address,Data):
	"""
	Write to the sensor regsiter (offset 0x0f000080)
	The format is swr(Address,Data) where Address is 0-47
	and Data is 32 bit value
	"""
	write(0x0f000080+Address,[Data])
	
	
def spiloop(exposure,looptimes):
	print 'spi loop'
		
	
	time.sleep(exposure)
	while looptimes !=0:
		looptimes = looptimes-1
		jwrtbits(3,0,0,1)
		time.sleep(exposure)
	

def setroi1length1021(Lines):	
	"""
	Set ROI1 length (in number of lines) for CIS1021 snsor
	"""
	print " "
#Save original SensrCtl values
	SavedSensrCtlT= read(0x6000000,1)[0]
	SavedSensrCtlB= read(0x7000000,1)[0]

	number=read(0x06000000,1)[0]
	print "OriginalTop:", number," (",hex(number),")"
	number=read(0x07000000,1)[0]
	print "OriginalBot:", number," (",hex(number),")"
	
	print " "
	print " "
	
	#stop!
	write(0x6000000,[SavedSensrCtlT & ~0x40])
	write(0x7000000,[SavedSensrCtlB & ~0x40])
	
	number=read(0x06000000,1)[0]
	print "OriginalTop after first write:", number," (",hex(number),")"
	number=read(0x07000000,1)[0]
	print "OriginalBot:", number," (",hex(number),")"
	
	#set roi1 len for both halves
	#write(0x0e000088,[Lines])
	#write(0x0f000088,[Lines])
	
	swrbbits(8,17,0,Lines)				

	#write(0x0f000088,[ROI1+4194304+8388608])
	#    4194304+8388608= 0xC00000 (default for reg #8)
	#    fixed by sm 1/18/11

	#restore SensrCtl
	write(0x6000000,[SavedSensrCtlT])
	write(0x7000000,[SavedSensrCtlB])
	
	print " "
	print " "
	
	number=read(0x06000000,1)[0]
	print "OriginalTop after restore write:", number," (",hex(number),")"
	number=read(0x07000000,1)[0]
	print "OriginalBot:", number," (",hex(number),")"
	
	number=read(0x0e000088,1)[0]
	print "Roi1Length_Top", number," (",hex(number),")"
	number=read(0x0f000088,1)[0]
	print "Roi1Length_Bot:", number," (",hex(number),")"
	
	####

def SetFvalWave(HighPeriod,LowPeriod):
	write(0x11000000,[HighPeriod])	#was 3
	write(0x11000001,[LowPeriod])	#was 4



#####
def swrsensorbitst(Address,MSB,LSB,Value):
	"""
	sensor write bits    address should be 00
	Change bits msb:lsb from the original value read from the sensor address
	to the new value
	
	The format is swrbits(Address,msb,lsb,value) 
	"""
	number=read(0x06000000+Address,1)[0]
	print "Original:", number," (",hex(number),")"
	number=setbits(number,MSB,LSB,Value)
	print "New value:", number," (",hex(number),")"
	swrsensort(Address,number)	


def swrsensort(Address,Data):
	"""
	Write to the sensor regsiter (offset 0x06000000)
	The format is swr(Address,Data) where Address is 0-47
	and Data is 32 bit value
	"""
	write(0x06000000+Address,[Data])	


#####
def swrsensorbitsb(Address,MSB,LSB,Value):
	"""
	sensor write bits    address should be 00
	Change bits msb:lsb from the original value read from the sensor address
	to the new value
	
	The format is swrbits(Address,msb,lsb,value) 
	"""
	number=read(0x07000000+Address,1)[0]
	print "Original:", number," (",hex(number),")"
	number=setbits(number,MSB,LSB,Value)
	print "New value:", number," (",hex(number),")"
	swrsensorb(Address,number)	


def swrsensorb(Address,Data):
	"""
	Write to the sensor regsiter (offset 0x06000000)
	The format is swr(Address,Data) where Address is 0-47
	and Data is 32 bit value
	"""
	write(0x07000000+Address,[Data])


##Lap

def setprescanlength1021(Lines):	
	"""
	Set ROI1 length (in number of lines) for CIS1021 snsor
	"""
	print " "
#Save original SensrCtl values
	SavedSensrCtlT= read(0x6000000,1)[0]
	SavedSensrCtlB= read(0x7000000,1)[0]

	number=read(0x06000000,1)[0]
	print "OriginalTop:", number," (",hex(number),")"
	number=read(0x07000000,1)[0]
	print "OriginalBot:", number," (",hex(number),")"
	
	print " "
	print " "
	
	#stop!
	write(0x6000000,[SavedSensrCtlT & ~0x40])
	write(0x7000000,[SavedSensrCtlB & ~0x40])
	
	number=read(0x06000000,1)[0]
	print "OriginalTop after first write:", number," (",hex(number),")"
	number=read(0x07000000,1)[0]
	print "OriginalBot:", number," (",hex(number),")"
	
	#set roi1 len for both halves
	#write(0x0e000088,[Lines])
	#write(0x0f000088,[Lines])
	
	nprescan=Lines+16		#def is 16 to keep total lines out consistent
	swrbbits(8,17,0,nprescan)				

	#write(0x0f000088,[ROI1+4194304+8388608])
	#    4194304+8388608= 0xC00000 (default for reg #8)
	#    fixed by sm 1/18/11

	#restore SensrCtl
	write(0x6000000,[SavedSensrCtlT])
	write(0x7000000,[SavedSensrCtlB])
	
	print " "
	print " "
	
	number=read(0x06000000,1)[0]
	print "OriginalTop after restore write:", number," (",hex(number),")"
	number=read(0x07000000,1)[0]
	print "OriginalBot:", number," (",hex(number),")"
	
	number=read(0x0e000088,1)[0]
	print "Roi1Length_Top", number," (",hex(number),")"
	number=read(0x0f000088,1)[0]
	print "Roi1Length_Bot:", number," (",hex(number),")"
	
	####



####Boris

def setmode1021global(Mode,rlines):
	"""
	Set image capture mode.
	The format is setmode(Mode) where the Mode can be one of the following:
	Note: A full initialization is done before mode change
	'rlgt'(raw low gain top)
	'rhgt'(raw high gain top)
	'rlgb'(raw low gain bottom)
	'rhgb'(raw high gain bottom)
	
	"""
	Mode=Mode.lower()
	if Mode == 'lg':
		print 'Raw low gain top'
		init1021global()
		setcam1021gbasef(rlines)
		selectsensor('lg')
	
	elif Mode == 'hg':
		print 'Raw high gain top'
		init1021global()
		setcam1021gbasef(rlines)		
		selectsensor('hg')
		
	elif Mode == 'lghg':
		print 'Raw low gain bottom'
		setcam1021gbasef(rlines)
		init1021global()
		selectsensor('lghg')
		
	elif Mode == 'hglg':
		print 'Raw high gain bottom'
		setcam1021gbasef(rlines)
		init1021global()
		selectsensor('hglg')
		
	else:
		print 'Unsupported mode!'


def setmode1021NP(Mode):
	"""
	Set image capture mode.
	The format is setmode(Mode) where the Mode can be one of the following:
	Note: A full initialization is done before mode change
	'rlgt'(raw low gain top)
	'rhgt'(raw high gain top)
	'rlgb'(raw low gain bottom)
	'rhgb'(raw high gain bottom)
	
	"""
	Mode=Mode.lower()
	if Mode == 'rlgt':
		print 'Raw low gain top'
		init1021NP()
		selectsensor('top')
	
	elif Mode == 'rhgt':
		print 'Raw high gain top'
		init1021NP()
		selectsensor('top')
		
	elif Mode == 'rlgb':
		print 'Raw low gain bottom'
		init1021NP()
		selectsensor('bot')
		
	elif Mode == 'rhgb':
		print 'Raw high gain bottom'
		init1021NP()
		selectsensor('bot')
		
	else:
		print 'Unsupported mode!'


def ReadWaveTables1021():
	"""
	Read and display wavetable for CIS1021 sensor
	"""
	#Save sensorcontrol value
	SavedSensorCtlB	=read(0x7000000,1)

	#Set datasel low
	write(0x7000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x0001])

	#Read Wavetable A
	print 'Wavetable A data:'
	print hex(read(0x0F0000AF,1)[0])
	print hex(read(0x0F0000AE,1)[0])
	print hex(read(0x0F0000AD,1)[0])
	print hex(read(0x0F0000AC,1)[0])
	print hex(read(0x0F0000AB,1)[0])
	print hex(read(0x0F0000AA,1)[0])
	print hex(read(0x0F0000A9,1)[0])
	print hex(read(0x0F0000A8,1)[0])
	print hex(read(0x0F0000A7,1)[0])
	print hex(read(0x0F0000A6,1)[0])
	print hex(read(0x0F0000A5,1)[0])
	print hex(read(0x0F0000A4,1)[0])
	print hex(read(0x0F0000A3,1)[0])
	print hex(read(0x0F0000A2,1)[0])
	print hex(read(0x0F0000A1,1)[0])
	print hex(read(0x0F0000A0,1)[0])
	print hex(read(0x0F00009F,1)[0])
	print hex(read(0x0F00009E,1)[0])
	print hex(read(0x0F00009D,1)[0])
	print hex(read(0x0F00009C,1)[0])
	print hex(read(0x0F00009B,1)[0])
	print hex(read(0x0F00009A,1)[0])
	print hex(read(0x0F000099,1)[0])
	print hex(read(0x0F000098,1)[0])
	print hex(read(0x0F000097,1)[0])
	print hex(read(0x0F000096,1)[0])
	print hex(read(0x0F000095,1)[0])
	print hex(read(0x0F000094,1)[0])
	print hex(read(0x0F000093,1)[0])
	print hex(read(0x0F000092,1)[0])
	print hex(read(0x0F000091,1)[0])
	print hex(read(0x0F000090,1)[0])

	#Set datasel high
	write(0x7000000,[(SavedSensorCtlB[0] & 0xEDBF) | 0x1001])

	#Read Wavetable B
	print 'Wavetable B data:'
	print hex(read(0x0F0000AF,1)[0])
	print hex(read(0x0F0000AE,1)[0])
	print hex(read(0x0F0000AD,1)[0])
	print hex(read(0x0F0000AC,1)[0])
	print hex(read(0x0F0000AB,1)[0])
	print hex(read(0x0F0000AA,1)[0])
	print hex(read(0x0F0000A9,1)[0])
	print hex(read(0x0F0000A8,1)[0])
	print hex(read(0x0F0000A7,1)[0])
	print hex(read(0x0F0000A6,1)[0])
	print hex(read(0x0F0000A5,1)[0])
	print hex(read(0x0F0000A4,1)[0])
	print hex(read(0x0F0000A3,1)[0])
	print hex(read(0x0F0000A2,1)[0])
	print hex(read(0x0F0000A1,1)[0])
	print hex(read(0x0F0000A0,1)[0])
	print hex(read(0x0F00009F,1)[0])
	print hex(read(0x0F00009E,1)[0])
	print hex(read(0x0F00009D,1)[0])
	print hex(read(0x0F00009C,1)[0])
	print hex(read(0x0F00009B,1)[0])
	print hex(read(0x0F00009A,1)[0])
	print hex(read(0x0F000099,1)[0])
	print hex(read(0x0F000098,1)[0])
	print hex(read(0x0F000097,1)[0])
	print hex(read(0x0F000096,1)[0])
	print hex(read(0x0F000095,1)[0])
	print hex(read(0x0F000094,1)[0])
	print hex(read(0x0F000093,1)[0])
	print hex(read(0x0F000092,1)[0])
	print hex(read(0x0F000091,1)[0])
	print hex(read(0x0F000090,1)[0])	
	
	#Set datasel low
	write(0x7000000,[SavedSensorCtlB[0]])

		
def init1021global():
	"""
	Initialize com port and test camera registers for CIS2051 sensor
	"""
	import time
	
	try:
		opencom(SystemConfig1021.ComPort)
	except:
		print "COM port is open"
	else:
		print "COM port is open"

	#flush serial port
	read(4,4)

	#Enable power 1st dvddio
	write(2,[0x4])
	time.sleep(0.1)

	#Enable power dvddio+ DVDD
	write(0x00000002,[0x5])
	time.sleep(0.1)

	#orig write(2,[0xf85]) 		#Enable ONLY DVDD and DVDDIO
	#orig time.sleep(0.1)

	#Board Soft Reset - same as pushbutton
	write(0,[4])
	time.sleep(0.1)

	#Check board revision number
	print 'FPGA rev = ',read(4,1)[0],'.',read(5,1)[0],'.',read(6,1)[0]
	# was orig                    write(2,[0xfff])  #Power supplies to sensor enabled
	FrameLenMult=1
	#Set clock divider of the sensor SPI controller 
	#write(0xe000000,[1]) # 1 - 22MHz; 2 - 15MHz 	  
	#write(0xe000001,[1]) # 1 - 22MHz; 2 - 15MHz 	  
	write(0xf000000,[1]) # 1 - 22MHz; 2 - 15MHz 	
	write(0xf000001,[1]) # 1 - 22MHz; 2 - 15MHz 	

	#Setup CLController for mode 0
	write(0x3000000,[2])

	#Set clock frequency
	setfreq(SystemConfig1021.SensorFreq)
	#setfreq(141)
	#Set JTAG controller
	#write(0x14000000,[0x7F])#0x7F=5.31MHz ,0x4F=21.25MHz(works) ,0x4B=28.33MHz ,0x47=42.5MHz  'CLK must be inverted (bit 6 on)
	#write(0x15000000,[0x7F])#0x7F=5.31MHz ,0x4F=21.25MHz(works) ,0x4B=28.33MHz ,0x47=42.5MHz  'CLK must be inverted (bit 6 on)

	#Set top/bot to sync mode
	#write(0x06000000,[0x22000])
	#write(0x07000000,[0x20000])

	#Prepare for Global Shutter op.
 	#write(0x06000000,[0x22380])
 	write(0x07000000,[0x22380])

	
	#Release sensor resetb
 	#write(0x06000000,[0x22381]) #top auto
 	write(0x07000000,[0x2001])

	#Prepare for Global Shutter op.
 	#write(0x06000000,[0x22380])
 	write(0x07000000,[0x22381])

	time.sleep(0.1)

	#Release sensor reset
	#write(0x6000000,[0x2001])
	#write(0x7000000,[0x2001])

	#Set READ to high
	#write(0x06000000,[0x2041])
	#write(0x07000000,[0x2041])

	#WriteWaveTables2051()
	
	#Enable power to AVDD+DVDD+DVDD_IO
	write(2,[0xd])	
	time.sleep(0.1)

	#enable the rest of power
	write(2,[0xfff]) 		#enable all power supplies
	time.sleep(0.1)

	#Enable data path
	#Enable data path
	#write(0x0,[0]) 		#leds off
	#write(0x0,[0xA]) 	#data path enable and camera link tx enable
	#write(0x1,[0xFF]) #clear error flags

#	lap	write(0x0e000088,[ROI1+(1080+64)*(FrameLenMult-1)]) #16+16 V overscan
#	srdb(8);
#	write(0x0f000088,[4194304+8388608])
#    4194304+8388608= 0xC00000 (default for reg #8)
#	srdb(8);

#	leave Roi1,2, and 3 border as default -- Lap OK to leave Out
	swrbbits(8,23,23,1)		# V border on
	swrbbits(8,22,18,16)	# Vroi1=16 dk
	swrbbits(8,17,0,16)		# Vroi2=16 dk +  16 prescan
	swrbbits(6,10,0,0)		# VROI3 starts
	swrbbits(7,10,0,1079)		# VROI3 ends border on

	ROI1=0
	print ROI1
	print FrameLenMult
	
	#print '0x0e000088',read(0x0e000088,1)	
	print '0x0f000088',read(0x0f000088,1)

	frame=(1080+64)*FrameLenMult
	rowclockbeg=4	#500    #Clock here is 85/4 MHz!!! also adds 4xoutclk jitter!! occurs at n*4 (0 = 9 to 11 outclks after chartran, 1=12 to 15)
	rowclockend=80 	#554  ' 0..564 for 2656 wavetable   maxoccurs at n*4
	
 	#write(0x01000048,[ROI1])
 	#write(0x02000048,[ROI1])
# 	write(0x01000048,[64+(1080+64)*(FrameLenMult-1)]) #16+16 V overscan
#	write(0x02000048,[64+(1080+64)*(FrameLenMult-1)]) 

#	frame=(1080+64)*FrameLenMult
	frame=(1144+ROI1)*FrameLenMult   # reduced to match framegrabber's 1112 frame length
	
	rowclockbeg=4	#500    #Clock here is 85/4 MHz!!! also adds 4xoutclk jitter!! occurs at n*4 (0 = 9 to 11 outclks after chartran, 1=12 to 15)
	rowclockend=80 	#566  ' 0..564 for 2656 wavetable   maxoccurs at n*4
#	rowclockend=80 	#554  ' 0..564 for 2656 wavetable   maxoccurs at n*4

	#top sensor
	
    #bottom sensor
	write(0x7000003,[2])            #2 frames, one reset one read
	write(0x7000014,[1144])        #each frame this many rows
#									16 borderT+16dkT+1080+16dkB+ 16borderB

#	write(0x7000005,[2]) #1,2   'tx2 rise    'polarity is inverted...
#	write(0x7000004,[2]) #0,1   'tx2 fall    'made to integrate only 1 frame (1/2 of possible in GS mode)
#	write(0x7000007,[0])  #tx2 fall rowclock 'begin integration
#	write(0x7000006,[0])  #tx2 rise rowclk   'dump

#   Tx2 modified
	#write(0x7000005,[0x00001]) #1,2   'tx2 rise    'polarity is inverted...
	#write(0x7000004,[0x00001]) #0,1   'tx2 fall    'made to integrate only 1 frame (1/2 of possible in GS mode)
	write(0x7000005,[0x40000*1+1141]) #1,2   'tx2 rise    'polarity is inverted...
	write(0x7000004,[0x40000*1+1141]) #0,1   'tx2 fall    'made to integrate only 1 frame (1/2 of possible in GS mode)

	write(0x7000007,[010])  #tx2 fall rowclock 'begin integration
	write(0x7000006,[01000])  #tx2 rise rowclk   'dump
	
	
	#write(0x7000008,[0x40001]) #1,0 'tx1 rise  fr-2
	#write(0x7000009,[0x40001]) #1,1 'tx1 fall  fr-1
	write(0x7000008,[0x40000*0+1141]) #1,0 'tx1 rise  fr-2
	write(0x7000009,[0x40000*0+1141]) #1,1 'tx1 fall  fr-1

	write(0x700000A,[0x3])  #tx1 rise 'start transfer
	write(0x700000B,[0x01a4])  #tx1 fall 'end integrationwas 20  width= 420-3

	write(0x700000C,[0x40000*0+1141]) #1,3    'datasel rise    'frame+2 is at lval falling
	#write(0x700000C,[0x40000*0+1111-32+ROI1]) #1,3    'datasel rise    'frame+2 is at lval falling (cis2051)
	#write(0x700000E,[0x00001]) #0,3          'datasel fall    '2 is at lval falling (old cis1021)
	write(0x700000E,[0x40000*1+1141]) #0,3          'datasel fall    '2 is at lval falling
	write(0x700000D,[10])  #520 datasel rise  6=chartran+4
	write(0x700000F,[10])  #520 datasel fall
	write(0x7000017,[0x40001]) #0,0 'tx3 rise
	write(0x7000018,[0x40001])#0,10 'tx3 fall
	write(0x7000019,[0])  #tx3 rise
	write(0x700001A,[0])  #tx3 fall

    #set global shutter mode
	#write(0x0e000082,[read(0x0e000082,1)[0] | 0x6002]) #also iv clockout
	write(0x0f000082,[read(0x0f000082,1)[0] | 0x20002])
	#  sets Register 2, bit 17 on (GlobalShutter), and bit 1 on (invclkb)

		
	
	#READ high
	#write(0x06000000,[0x223c1])  #23c1
	#write(0x07000000,[0x223c1])

	#Setup CLController For mode 0 - CL0=TopLG; CL1=TopHG
	write(0x3000000,[2])   #5=HG_T HG_B

	#Setup DataSamplerTop For sensor data
	write(0x04000000,[0])
	write(0x05000000,[0])

	
	
	#Enable data path And leds
	write(0x00000000,[3])
	write(1,[0xFF])   #clear error flags

	#WriteWaveTables2051LoadFile()
	WriteWaveTables1021()
	#write(0x0e000082,[(read(0x0e000082,1)[0] & 0xFFFFFFCF) | 0x30])
	write(0x0f000082,[(read(0x0f000082,1)[0] & 0xFFFFFFCF) | 0x30])
	print '0x0f000082',read(0x0f000082,1)

	#print '0x0e000088',read(0x0e000088,1)	
	print '0x0f000088',read(0x0f000088,1)	

	#turn LEDs off
	write(0x0,[(read(0x0,1)[0] & 0xFFFFFFFE | 0x8)])
	
	# Finally, turn READ high
	#write(0x07000000,[0x223c1])
	write(0x07000000,[0x323c1])
	# Turns READ high, turns on FVAL sync, etc
	
	#### based frame plus add pslines lap
#	adding prescan lines = nlines to base frame

def setcam1021gbasef(nlines):			# top set roi for global integration only
	blines=1144
	tlines=blines+nlines
	Vroi1=16+nlines

	swrbbits(8,17,0,Vroi1)				# Vroi1=16 dk +  nlines
	write(0x07000014,[tlines])			# Total rows per cycle 54 roi2+3 dk+ extra

	
	
def loopspiWrite(exposure, looptimes):
#	write read start line and frame -- snap global ---not working
	
#	number1=read(0x0f000082,1)[0]
#	print "read endFrame:", number1," (",hex(number1),")"
	
	time.sleep(exposure)
	while looptimes !=0:
		looptimes = looptimes-1
		write(0x0f000082,[0x01])
#		number1=read(0x0f000082,1)[0]
#		print "write  0f000082:", number1," (",hex(number1),")"
		print"write 0x0f000082"
		time.sleep(exposure)
		
def loopspiRead(exposure, looptimes):
#	write read start line and frame -- snap global ---not working
	
#	number1=read(0x0f000082,1)[0]
#	print "read endFrame:", number1," (",hex(number1),")"
	
	time.sleep(exposure)
	while looptimes !=0:
		looptimes = looptimes-1
#		read(0x0f000082,1)
		number1=read(0x0f000082,1)[0]
		print "read  0f000082:", number1," (",hex(number1),")"
#		print"read 0x0f000082"
		time.sleep(exposure)