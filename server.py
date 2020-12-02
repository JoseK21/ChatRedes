import socket
import os
from _thread import *

from bcolors import *  

ServerSideSocket = socket.socket()
host = '127.0.0.1'
port = 2004
ThreadCount = 0
try:
    ServerSideSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print(f"{bcolors.OKGREEN}Server Running...{bcolors.ENDC}")

ServerSideSocket.listen(5)

def multi_threaded_client(connection):
    connection.send(str.encode('Server is working:'))
    while True:
        data = connection.recv(2048)
        response = data.decode('utf-8')
        if not data:
            break
        r = response.split('<::>')
        print( f"{bcolors.HEADER}{r[0]}{bcolors.ENDC}: {r[1]}")
    connection.close()

while True:
    Client, address = ServerSideSocket.accept()
    print(f"New user [{str(address[1])}]")
    start_new_thread(multi_threaded_client, (Client, ))
ServerSideSocket.close()