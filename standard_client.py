#Código para criar cliente TCP.
import socket
import datetime
#definindo porta e address.
adress = '127.0.0.1'
port = 5002
#criando o socket TCP.
socket_cliente_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#definição do destino
destiny = (adress, port)
#link do socket com o endereço de destino
socket_cliente_tcp.connect(destiny)
print("conexão estabelecida")
#mensagem a ser enviada
mensagem = input("envie algo")
#o socket envia a mensagem para o servidor tcp codificado com UTF-8
socket_cliente_tcp.send(mensagem.encode('utf-8'))
#O método recv lê os bytes recebidos, retornando-os em uma string, até o limite 2000. não esqueça de decodificar de UTF-8
mensagem_recebida = socket_cliente_tcp.recv(2000).decode('utf-8')
print("Mensagem recebida: %s" %mensagem_recebida)
#temos que fechar o socket
socket_cliente_tcp.close()
