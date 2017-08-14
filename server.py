import socket
import sys
import time

import matplotlib.pyplot as plt
import numpy as np


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
# server_address = ('10.14.86.132', 10000)
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axis_bgcolor('black')
plt.ylim(150, -150)

while True:
    # Wait for a connection
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    
    try:
        print >>sys.stderr, 'connection from', client_address

        # Receive the data sequentially and save it in the database

        d = 0
        prev = 0
        x= 10
        t_ini= (int(10*float(time.time()))%100000)
        i= t_ini
        t_ins= t_ini
        while True:
            data = connection.recv(16)
            if data == '':
            	exit()
            data_copy= data
            data= data.split('*')
            # Plot
            t_prev= t_ins
            t_ins=(int(10*float(time.time()))%100000)
            i= t_ins
            t= str(t_ins)
            prev = d

            d= int(data[2])
            x= int(data[1])
            if i>t_ini+30:
                plt.xlim(i-100, i+5)
            
            plt.plot([t_prev,t_ins], [prev,d], linewidth= 3, c='#21ff00')
            plt.show()
            fig.canvas.draw()
            
            print >>sys.stderr, 'received "%s"' % data[2]
            if data:
                print >>sys.stderr, 'sending data back to the client'
                connection.sendall(data_copy)
                
            else:
                print >>sys.stderr, 'no more data from', client_address
                break

    finally:
        # Clean up the connection
        connection.close()