import socket

host = '0.0.0.0' #aceita conexões de qualquer IP
port = 8109

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print(f"--------Servidor escutando na porta {port}.--------")

conn, addr = server.accept()
print(f"--------Conectado com {addr}!--------")

while True: # loop infinito para conexão entre servidor e cliente.
    msg = conn.recv(1024).decode()
    if not msg:
        break
    print(f"Cliente: {msg}")
    resposta = input("Você: ")
    conn.send(resposta.encode())

server.close()
