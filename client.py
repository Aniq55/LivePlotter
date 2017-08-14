import socket
import sys
import math
import time

# For sending data coming from arduino serial port
# import serial
# ser = serial.Serial('/dev/ttyACM0', 9600)

#declaring constants
K=5000

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
while True:
	try:
	    # Send data 
	    message = '1*10*' + str(int(100*math.sin(K*time.clock()))) +'*~' #Dummy data
	    # message = ser.readline()	# for arduino serial data
	    print >>sys.stderr, 'sending "%s"' % message
	    sock.sendall(message)

	    # Look for the response
	    amount_received = 0
	    amount_expected = len(message)

	    
	    while amount_received < amount_expected:
	        data = sock.recv(16)
	        amount_received += len(data)
	        print >>sys.stderr, 'received "%s"' % data

	except:
	    print >>sys.stderr, 'Error'

