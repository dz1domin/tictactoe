import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
message = b"fkdsapjf"
s.connect(('127.0.0.1', 5005))
s.send(message)
