#!/usr/bin/python

import Adafruit_BBIO.UART as UART
import serial
import time

#OUART.setup("UART2")

ser = serial.Serial(port = "/dev/ttyO2", baudrate=9600)
ser.close()
ser.open()

if ser.isOpen():
	print "Serial port NOT open!"
else:
	print "Port open for reading."

print "Waiting to receive data..."

while True:
	data = ser.readline()
	print data

ser.close()

# Eventually, you'll want to clean up, but leave this commented for now, 
# as it doesn't work yet
#UART.cleanup()
