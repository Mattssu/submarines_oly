import socket

START_SYNC = "HELLO"

RESPONSE_SYNC = "OLLEH"

END_GAME = "GG"

BUFFER_SIZE = 1024

HOST, PORT = "localhost", 8765

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


def host_connect(submarine_game):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

        server.bind((HOST, PORT))
        server.listen()

        conn, addr = server.accept()
        with conn:
            print('Connected by', addr)
            while True:
                data = (bytes(format_message(START_SYNC), "utf-8"))
                conn.sendall(data)

                data = conn.recv(BUFFER_SIZE)
                print(data)

                if str(data[3:], "utf-8") == RESPONSE_SYNC:
                    print("SYNCED")

                while data[3:] != b"GG":
                    # SEND BOMB
                    data = user_bomb_input()
                    data = (bytes(format_message(data), "utf-8"))
                    conn.sendall(data)
                    print("Sent BOMB")
                    print(data)

                    # WAIT FOR RESPONSE
                    data = conn.recv(BUFFER_SIZE)
                    print("RECEIVED RESPONSE")
                    print(str(data, "utf-8"))

                    if data[3:] == b"GG":
                        return

                    # IF MISS THEN WAIT TURN ELSE CONTINUE
                    if data[3:] == b"MISS":
                        while data[3:] != b"GG":
                            # WAIT FOR BOMB
                            data = conn.recv(BUFFER_SIZE)
                            print("GOT BOMBED")
                            print(str(data, "utf-8"))

                            # RESPOND
                            cord = str(data, "utf-8").split("~")
                            response = submarine_game.bomb_a_location((int(cord[1]), int(cord[2])))

                            data = (bytes(format_message(response), "utf-8"))
                            conn.sendall(data)

                            print("SENT RESPONSE")
                            print(str(data, "utf-8"))
                            # IF RESPONSE WAS MISS THEN ITS MY TURN
                            if data[3:] == b"MISS":
                                break
                return
