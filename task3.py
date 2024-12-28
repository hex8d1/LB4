import socket
import threading

def handle_client(conn, addr):
    print(f"Подключён клиент: {addr}")
    with open("received_file.txt", "w") as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data.decode())
    print(f"Файл от клиента {addr} успешно сохранён.")
    conn.close()
    print(f"Соединение с клиентом {addr} закрыто.")

def echo_server():
    host = '127.0.0.1'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен на {host}:{port}. Ожидание подключения...")

    while True:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr))
        client_thread.start()
        print(f"Поток для клиента {addr} запущен.")

if __name__ == "__main__":
    echo_server()
