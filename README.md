TCP Server and Client
This repository contains a simple implementation of a TCP server and client in Python. The server listens for incoming connections, while the client connects to the server, sends a message, and receives the echoed response.
Features

    TCP Server:
        Listens for incoming TCP connections.
        Handles multiple clients concurrently using threading.
        Echoes received messages back to the clients.
        Logs connection and message details.

    TCP Client:
        Connects to the TCP server.
        Sends a user-defined message.
        Receives and prints the echoed message from the server.

Requirements

    Python 3.x

Installation

    Clone the repository:

    bash

git clone https://github.com/3ed0x92/TCP_Server.git

Navigate to the project directory:

bash

    cd TCP_Server

Usage
Running the TCP Server

To start the TCP server, use the following command:

bash

python server.py --host <HOST> --port <PORT>

    --host: The IP address to bind the server to (default: 127.0.0.1).
    --port: The port number to bind the server to (default: 12345).

Example:

bash

python server.py --host 0.0.0.0 --port 8080

This command will start the server and it will listen on all available interfaces (0.0.0.0) at port 8080.
Running the TCP Client

To start the TCP client and send a message, use the following command:

bash

python client.py --host <HOST> --port <PORT> --message "<MESSAGE>"

    --host: The IP address of the server (default: 127.0.0.1).
    --port: The port number of the server (default: 9292).
    --message: The message to send to the server.

Example:

bash

python client.py --host 127.0.0.1 --port 8080 --message "Hello, Server!"

This command will connect to the server at 127.0.0.1 on port 8080 and send the message "Hello, Server!".
Logging

Both the server and client use the logging module to provide information about their operation. Logs include:

    Connection and disconnection events.
    Messages sent and received.
    Any errors that occur.

Examples

    Start the server:

    bash

python server.py --host 127.0.0.1 --port 9292

Send a message using the client:

bash

python client.py --host 127.0.0.1 --port 9292 --message "Hello World"

You should see the following output on the client side:

arduino

Received 'Hello World'

And the server will log the connection details and the message received.
