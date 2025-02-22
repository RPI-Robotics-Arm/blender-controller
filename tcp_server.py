import socket

def start_server(ip="127.0.0.1", port=6969):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((ip, port))
    server_socket.listen(1)
    print(f"Server listening on {ip}:{port}...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Received: {data}")
        conn.sendall("Acknowledged: {}".format(data).encode())
        conn.close()
        print("Connection closed.")

if __name__ == "__main__":
    start_server()
