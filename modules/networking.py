import socket


class TCPClient:
    """
    A simple TCP client to connect to a server and send messages.
    """

    def __init__(self, ip: str, port: int):
        """
        Initialize the client with a target IP and port.
        """
        self.ip = ip
        self.port = port
        self.client_socket = None

    def connect(self):
        """
        Connect to the server at the specified IP and port.
        """
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.ip, self.port))
        print(f"Connected to server at {self.ip}:{self.port}")

    def send_message(self, message: str):
        """
        Send a string message to the server.
        """
        if self.client_socket is None:
            raise ConnectionError("Not connected to any server.")

        self.client_socket.sendall(message.encode("utf-8"))
        print(f"Message sent: {message}")

    def close(self):
        """
        Close the connection to the server.
        """
        if self.client_socket:
            self.client_socket.close()
            print("Connection closed.")
