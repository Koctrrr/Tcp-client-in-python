import socket

target_host = "what ever website
target_port = 80

# creat a socket object
client = socket.socket(socket.Af_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host,target_port))

# send some data
client.send("GET / HTTP/1.1/r/nHost: what ever web/r/n/r/n")

# receive some data
response = client.recv(4096)

print response 
