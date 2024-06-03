import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 8458))

server_socket.listen(4) # escutando

print("Servidor aguardando conexão...")
while True:
  # Aceitando a conexão
  client_socket, client_address = server_socket.accept()

  print(f"client_socket: {client_socket} | Address: {client_address}")

  data = client_socket.recv(1024)

  if data:
    print(f"Recebido: {data.decode('utf-8')}")

    # Criar uma resposta JSON
    response = json.dumps({ "message": "Hello World, Python" })

    # Enviar a resposta JSON AO CLIENT

    client_socket.sendall(response.encode( 'utf-8'))
  client_socket.close()

  