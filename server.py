from concurrent.futures import thread
import socket
from sqlite3 import connect
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


def handel_client(conn, addr):
    print(f"=> NEW CONNECTIONS {addr} connected.")
    connected = True

    while connected:
        msg = conn.recv(64)


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handel_client, args={conn, addr})
        thread.start()  # starting
        print(f"=> ACTIVE CONNECTIONS {threading.activeCount() - 1 }")
