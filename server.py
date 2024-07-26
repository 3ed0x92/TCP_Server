import socket
import argparse
import threading
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def handle_client(conn,addr):
    logging.info(f'Connected by {addr}')
    with conn:
        while True:
            data=conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
            logging.info(f'Received and echoed data: {data!r}')

def start_echo_server(host,port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(host,port)
        s.listen()
        logging.info(f"Server listening on {host}:{port}")

        while True:
            conn,addr=s.accept()
            client_threaad= threading.Thread(args=(conn, addr))
            client_threaad.start()


def main():
    parser = argparse.ArgumentParser(description="Start an echo server.")
    parser.add_argument("host",default='127.0.0.1',help="'Host to bind the server to'")
    parser.add_argument("--port",type=int,default=9292,help="Port to bind the server to")
    args = parser.parse_args()
    start_echo_server(args.host, args.port)

    if __name__=='__main__':
        main()
