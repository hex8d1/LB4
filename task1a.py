import socket

def echo_client():
    host = '127.0.0.1'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Подключено к серверу {host}:{port}")

    while True:
        message = input("Введите сообщение для отправки (или 'exit' для выхода): ")
        if message.lower() == 'exit':
            break
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Получено от сервера: {data.decode()}")

    client_socket.close()
    print("Соединение закрыто.")

if __name__ == "__main__":
    echo_client()
