import socket 

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("localhost", 1986))

while True:

    msg = input("Digite aqui sua mensagem: ")
    cliente.send(msg.encode())