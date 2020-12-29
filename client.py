import socket
import random

HOST, PORT = "localhost", 8765

START_SYNC = "HELLO"

RESPONSE_SYNC = "OLLEH"

END_GAME = "GG"


def user_bomb_input():
    x = input("Choose X: ")
    y = input("Choose Y: ")
    return "BOMB~{}~{}".format(x, y)


def client_connect():
    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        # SYNC PART
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))
        if received == START_SYNC:
            sock.sendall(bytes(RESPONSE_SYNC, "utf-8"))

        while received != END_GAME:
            received = str(sock.recv(1024), "utf-8")
            print("Received: {}".format(received))

            data = random_answer()
            sock.sendall(bytes(data + "\n", "utf-8"))

            if "MISS" == data:
                # GAME PART
                while received != END_GAME:
                    data = user_bomb_input()
                    sock.sendall(bytes(data + "\n", "utf-8"))

                    # Receive ANSWER for our bomb
                    received = str(sock.recv(1024), "utf-8")

                    print("Sent:     {}".format(data))
                    print("Received: {}".format(received))

                    if received == "MISS":
                        break

    sock.close()


def random_answer():
    bank = ["MISS", "MISS", "MISS", "HIT", "SINK"]
    index = random.randint(0, 4)
    return bank[index]


client_connect()
