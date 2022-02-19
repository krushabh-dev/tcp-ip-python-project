import socket
import threading
#threading is an essential for creating multiple thread

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = "10.252.1.144"
# print("SERVER CODE: ", socket.gethostname())

ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#binding to a address
server.bind(ADDR)

