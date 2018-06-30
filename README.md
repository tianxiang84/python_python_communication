# python_python_communication
Communication between 2 python programs: client sends data to server

Run server.py first. It will open a socket and keep listening
Run client.py next. It will promt user for message to send to server and then send the message to the server.
You will see server display the message received.

Works for python 3+
encode() added fro python 3, no need for py2
decode() added for python 3, no need for py2



Matlab

Start 2 instances of MATLAB

in the first execute the following:  

message = '1'

server(message, 3000, 10) 

in the second execute the following

data = client('localhost', 3000) 

