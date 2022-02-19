import socket
import threading
#threading is an essential for creating multiple thread

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = "192.168.56.1"