import socket
from bcolors import *  

ClientMultiSocket = socket.socket()
host = '127.0.0.1'
port = 2004

nombre = input(f"{bcolors.OKCYAN}¿Cómo se llama? {bcolors.ENDC}")
print(f"Bienvenido, {bcolors.HEADER}{nombre}{bcolors.ENDC}!")

try:
    ClientMultiSocket.connect((host, port))
except socket.error as e:
    print(str(e))

res = ClientMultiSocket.recv(1024)
while True:
    Input = input('> ')
    if Input != "" :
        ClientMultiSocket.send(str.encode(nombre + "<::>" + Input))

ClientMultiSocket.close()