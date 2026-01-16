import socket 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Criando objeto socket para receber dados de um socket client.

server.bind(("localhost", 1986)) #configure para colocar o seu ip e uma porta qualquer acima de 1024.
server.listen()

conn, addr = server.accept()#Ouve a porta e so entao se conecta

while True:
    msg = input("Digite aqui sua mensagem:")
    conn.send(msg.encode())
    resposta = conn.recv(1024)
    print("Mensagem do Cliente: %s: %s" %(addr, resposta.decode())) #Passando a mensagem de Bytes para Str com o metodo ".decode".