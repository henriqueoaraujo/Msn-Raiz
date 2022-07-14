from ipaddress import ip_address
import sys
import socket

from _thread import start_new_thread

from xarray import broadcast

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


def remove_cliente(cliente):
    #Esta função remove o cliente da lista de cliente ativos

    if cliente in list_of_clients:
        list_of_clients.remove(cliente)



def broadcast(mensagem, conexao):
    #Esta função encaminha a mensagem de um cliente para todos 
    for cliente in list_of_clients:
        if cliente != conexao:
        try:
            cliente.send(mensagem)    
        except:
            cliente.close()

            # se a conexao estiver quebrada, vamos remover o cliente dam inha lista de cliente ativos
            remove_cliente(cliente)


def thread_do_cliente (conexao, endereco):
    # Mando mensagem de boas vindas atraves do objeto de conexão
    conexao.send("Bem vindo ao chat Master Python".encode())    

    while True:

        try: 

            mensagem = conexao.recv(2048)

            if mensagem is not None:
                #Print mensagem que o cliente mandou no terminal do servidor
                mensagem_para_encaminhar = "[" + endereco[0] + "]: " + mensagem
                
                print(mensagem_para_encaminhar)

                broadcast(mensagem_para_encaminhar, conexao)
        except:
            continue


while True:
    
    """
    Aceitar conexão de clientes
     Objeto de conexao
     Endereço de ip.
    """
    conexao, endereco = server.accept()
  
    #Salvar cliente na minha lista de clientes ativos
    list_of_clients.append(conexao)

    print("Cliente conectado endereço: " + endereco)

    start_new_thread ( thread_do_cliente, (conexao, endereco))



server.close()
