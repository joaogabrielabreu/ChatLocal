import socket

host = '0.0.0.0'  # troque pelo IP do servidor se estiver em outra máquina
port = 8109

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
print("Conectado ao servidor!")

while True:
    msg = input("Você: ")
    client.send(msg.encode())
    resposta = client.recv(1024).decode()
    print(f"Servidor: {resposta}")

