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


def random_answer():
    bank = ["MISS", "MISS", "GG", "GG", "GG"]
    index = random.randint(0, 4)
    return bank[index]


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
            # WAIT FOR BOMB
            received = str(sock.recv(1024), "utf-8")
            print("Received BOMB location: {}".format(received))
            # CREATE RESPONSE
            data = random_answer()
            sock.sendall(bytes(data + "\n", "utf-8"))
            print("Sent ANSWER:     {}".format(data))
            if data == END_GAME:
                break
            # IF ENEMY MISS THEN ITS MY TURN
            if "MISS" == data:
                while received != END_GAME:
                    # MY TURN TO BOMB
                    data = user_bomb_input()
                    sock.sendall(bytes(data + "\n", "utf-8"))
                    print("Sent BOMB:     {}".format(data))

                    # RECEIVE RESPONSE FOR BOMB
                    received = str(sock.recv(1024), "utf-8")
                    print("Received ANSWER: {}".format(received))
                    # IF IT WAS A MISS THEN IT'S ENEMY'S TURN
                    if received == "MISS":
                        break

    sock.close()


client_connect()
