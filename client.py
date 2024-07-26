import socket
import argparse

def start_echo_client(host, port, message):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(message.encode())
            data = s.recv(1024)
            print(f'Received {data.decode()!r}')
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description='Start an echo client.')
    parser.add_argument('--host', default='127.0.0.1', help='Host to connect to')
    parser.add_argument('--port', type=int, default=12345, help='Port to connect to')
    parser.add_argument('--message', required=True, help='Message to send')
    args = parser.parse_args()
    start_echo_client(args.host, args.port, args.message)

if __name__ == '__main__':
    main()
