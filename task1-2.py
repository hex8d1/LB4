import socket

def echo_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)  # Очередь до 5 подключений
    print(f"Сервер запущен на {host}:{port}. Ожидание подключения...")

    while True:
        conn, addr = server_socket.accept()
        print(f"Подключён клиент: {addr}")

        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f"Получено от клиента {addr}: {data.decode()}")
            conn.sendall(data)
            print(f"Сообщение отправлено обратно клиенту {addr}.")

        conn.close()
        print(f"Соединение с клиентом {addr} закрыто.")

if __name__ == "__main__":
    echo_server()
