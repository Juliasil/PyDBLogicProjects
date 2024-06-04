import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Enviar dados
message = "Olá servidor, eu sou cliente!"
client_socket.sendto(message.encode('utf-8'), ('localhost', 9195))


# Receber o pacote da resposta do servidor
data, server = client_socket.recvfrom(1024)
print(f"Resposta do servidor: {data.decode('utf-8')}")

client_socket.close()