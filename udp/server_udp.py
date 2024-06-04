import socket
# crei um socket udp/ip
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# liga o socket ao endereço e porta que eu quero.

server_socket.bind(('localhost', 9195))

print("Servidor UDP aguardando mensagens...")

while True:
  data, address = server_socket.recvfrom(1024)
  print(f"Recebido {data.decode('utf-8')} de {address}")

# Resposta
if data:
  server_socket.sendto(data, address)