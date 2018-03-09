
# Echo client program
import socket

HOST = '127.0.0.1'    # The remote host
PORT = 50007          # The same port as used by the server



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
print "type input:"
text = raw_input()

# when we send data to the server, we are using a colon
# at the end of a sentence to mark the end of the current sentence
# later when the input comes back, we will then be breaking the input
# into individual parts using the colon : to separate the lines
s.sendall(text + ":")

data = s.recv(80000)

# breaking apart the data we get back.
response = data.split(':')

for x in response:
    print "Response:" + str(x)
    
s.close()
