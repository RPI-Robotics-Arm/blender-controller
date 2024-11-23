import pytest
from unittest.mock import patch, MagicMock
from modules.networking import TCPClient
import socket


@pytest.fixture
def tcp_client():
    return TCPClient(ip="127.0.0.1", port=8080)


def test_tcp_client_initialization(tcp_client):
    assert tcp_client.ip == "127.0.0.1"
    assert tcp_client.port == 8080
    assert tcp_client.client_socket is None


@patch("socket.socket")
def test_tcp_client_connect(mock_socket, tcp_client):
    mock_socket_instance = MagicMock()
    mock_socket.return_value = mock_socket_instance

    tcp_client.connect()

    mock_socket.assert_called_once_with(socket.AF_INET, socket.SOCK_STREAM)
    mock_socket_instance.connect.assert_called_once_with(("127.0.0.1", 8080))
    assert tcp_client.client_socket == mock_socket_instance


@patch("socket.socket")
def test_tcp_client_send_message(mock_socket, tcp_client):
    mock_socket_instance = MagicMock()
    mock_socket.return_value = mock_socket_instance
    tcp_client.connect()

    tcp_client.send_message("Hello, Server!")

    mock_socket_instance.sendall.assert_called_once_with(b"Hello, Server!")


@patch("socket.socket")
def test_tcp_client_send_message_not_connected(mock_socket, tcp_client):
    with pytest.raises(ConnectionError, match="Not connected to any server."):
        tcp_client.send_message("Hello, Server!")


@patch("socket.socket")
def test_tcp_client_close(mock_socket, tcp_client):
    mock_socket_instance = MagicMock()
    mock_socket.return_value = mock_socket_instance
    tcp_client.connect()

    tcp_client.close()

    mock_socket_instance.close.assert_called_once()
