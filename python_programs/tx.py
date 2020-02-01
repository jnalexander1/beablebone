#!/usr/bin/python

import Adafruit_BBIO.UART as UART
import serial
import time

#UART.setup("UART1")

ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()

if ser.isOpen():
	print "Serial port NOT open!"
else:
	print "Port open for writing."

i=0
while i< 10:
	print "Writing data - " + str(i)
	i += 1
	ser.write("Hello World - " + str(i) + "\n")
	time.sleep(3)

ser.close()

# Eventually, you'll want to clean up, but leave this commented for now, 
# as it doesn't work yet
#UART.cleanup()
