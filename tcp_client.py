import socket

class TCPClient:
    def __init__(self, ip_address: str, port: int):
        self.ip_address = ip_address
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._connect_to_server()
    
    def _connect_to_server(self):
        try:
            self.client_socket.connect((self.ip_address, self.port))
            print(f"Connected to server at {self.ip_address}:{self.port}")
        except socket.error as e:
            print(f"Failed to connect: {e}")
    
    def send_data(self, data: str):
        try:
            self.client_socket.sendall(data.encode())
            print(f"Data sent: {data}")
        except socket.error as e:
            print(f"Failed to send data: {e}")

    def close_connection(self):
        self.client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    ip = "127.0.0.1"  # Example IP (localhost)
    port = 6969       # Example port

    client = TCPClient(ip, port)
    client.send_data("Hello, Server!")
    client.close_connection()
