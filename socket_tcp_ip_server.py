import socket
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('localhost', 8458))

server_socket.listen(4) # escutando

print("Servidor aguardando conexão...")
while True:
  # Aceitando a conexão
  client_socket, client_address = server_socket.accept()

  print(f"Conexão estabelecida com {client_address}")

  data = client_socket.recv(1024)

  if data:
    print(f"Recebido: {data.decode('utf-8')}")

    # Criar uma resposta JSON
    data = json.dumps({ "message": "Hello World, Python" })

    response = (
      "HTTP/1.1 200 OK\r\n"
      "Content-Type: application/json\r\n"
      f"Content-length: {len(data)}\r\n"
      "Connection: close\r\n"
      "\r\n"
      f"{data}"
    )

    # Enviar a resposta JSON AO CLIENT

    client_socket.sendall(response.encode( 'utf-8'))
  client_socket.close()

  