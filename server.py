from ipaddress import ip_address
import sys
import socket

from _thread import start_new_thread

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if len(sys.argv) != 3:
    print("O uso correto é: python server.py [IP] [PORTA]")
    exit ()

#Pega os parametros passados na linha de comando
IP_ADDRESS = sys.argv[1]
PORT = int(sys.argv[2])

#Conecta o servidor no endereço especificado em IP_ADDRESS e PORT
server.bind( (IP_ADDRESS, PORT) )

#Determina o numero de clientes ativos no chat
server.listen(100)

#Lista de clientes ativos
list_of_clients = []










server.close()
