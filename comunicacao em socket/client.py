import socket 

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(("localhost", 1986)) #Conecta no IP do server e a porta a ser escolhida.
conn, addr = cliente, ("localhost", 1986) #Simulando o mesmo comportamento do server para printar o endereco.

while True:   
    msg = input("Digite aqui sua mensagem: ")
    conn.send(msg.encode()) #

    resposta = conn.recv(1024)
    print("Servidor: %s: %s" %(addr, resposta.decode())) 