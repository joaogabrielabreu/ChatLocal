import socket

HOST = '127.0.0.1'  # troque pelo IP do servidor se estiver em outra máquina
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))
print("Conectado ao servidor!")

while True:
    msg = input("Você: ")
    client.send(msg.encode())
    resposta = client.recv(1024).decode()
    print(f"Servidor: {resposta}")
