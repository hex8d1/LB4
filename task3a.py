import socket


def send_file(file_path):
    host = '127.0.0.1'
    port = 12345

    try:
        with open(file_path, 'r') as file:
            file_content = file.read()

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Подключено к серверу {host}:{port}")

        client_socket.sendall(file_content.encode())
        print("Файл успешно отправлен на сервер.")

        client_socket.close()
        print("Соединение закрыто.")
    except FileNotFoundError:
        print("Файл не найден. Укажите корректный путь к файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    file_path = input("Введите путь к текстовому файлу: ")
    send_file(file_path)
