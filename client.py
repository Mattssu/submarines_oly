import socket

HOST, PORT = "localhost", 8765

START_SYNC = "HELLO"

RESPONSE_SYNC = "OLLEH"

END_GAME = "GG"

MAX_NUM = "999"
MAX_INT = 999

PROTOCOL_LEN = 3


def user_bomb_input():
    x = input("Choose X: ")
    y = input("Choose Y: ")
    return "BOMB~{}~{}".format(x, y)


def format_message(msg):
    msg_len = len(msg)
    if msg_len > MAX_INT:
        return MAX_NUM + msg
    result = str(msg_len)
    while len(result) != PROTOCOL_LEN:
        result = f'0{result}'
    return result + msg


def client_connect(submarine_game):
    try:
        host = input("Insert ip to connect to :")
        if len(host.split(".")) != 4:
            raise ValueError
    except ValueError:
        print("Wrong IP format")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, PORT))
        # SYNC PART
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))
        if received[3:] == START_SYNC:
            sock.sendall(bytes(format_message(RESPONSE_SYNC), "utf-8"))

        while received[3:] != END_GAME:
            # WAIT FOR BOMB
            received = str(sock.recv(1024), "utf-8")
            print("Received BOMB location: {}".format(received))

            cord = received.split("~")
            data = submarine_game.bomb_a_location((int(cord[1]), int(cord[2])))
            data = format_message(data)

            # CREATE RESPONSE
            sock.sendall(bytes(data, "utf-8"))
            print("Sent ANSWER:     {}".format(data))
            if data == format_message(END_GAME):
                break
            # IF ENEMY MISS THEN ITS MY TURN
            if "MISS" == data[3:]:
                while received[3:] != END_GAME:
                    # MY TURN TO BOMB
                    data = user_bomb_input()
                    sock.sendall(bytes(format_message(data), "utf-8"))
                    print("Sent BOMB:     {}".format(data))

                    # RECEIVE RESPONSE FOR BOMB
                    received = str(sock.recv(1024), "utf-8")
                    print("Received ANSWER: {}".format(received))
                    # IF IT WAS A MISS THEN IT'S ENEMY'S TURN
                    if received[3:] == "MISS":
                        break

    sock.close()


def client_sync_demo():
    try:
        host = input("Insert ip to connect to :")
        if len(host.split(".")) != 4:
            raise ValueError
    except ValueError:
        print("Wrong IP format")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((host, PORT))
        # SYNC PART
        received = str(sock.recv(1024), "utf-8")
        print("Received: {}".format(received))
        if received[3:] == START_SYNC:
            sock.sendall(bytes(format_message(RESPONSE_SYNC), "utf-8"))
