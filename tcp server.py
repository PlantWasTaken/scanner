import socket

HOST = "192.168.50.160"  # The server's hostname or IP address
PORT = 3000  # The port used by the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen(1)

conn, addr = server.accept()

data_log = open("tcp.txt","wb")
while 1:
    data = conn.recv(1024)
    if not data:
        break
    if(data == "END"):
        conn.close() 
        data_log.close()
    else:
        print(data.decode('utf-8').rstrip()+"\n")
        data_log.write(data)
    
