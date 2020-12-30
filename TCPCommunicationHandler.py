import socketserver
import random

START_SYNC = "HELLO"

RESPONSE_SYNC = "OLLEH"

END_GAME = "GG"


class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def user_bomb_input(self):
        x = input("Choose X: ")
        y = input("Choose Y: ")
        self.data = "BOMB~{}~{}".format(x, y)

    def handle(self):
        flag = False
        self.data = (bytes(START_SYNC, "utf-8"))
        self.request.sendall(self.data)

        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        if str(self.data, "utf-8") == RESPONSE_SYNC:
            print("SYNCED")

            while self.data != b"GG":
                # SEND BOMB
                self.user_bomb_input()
                self.data = (bytes(self.data, "utf-8"))
                self.request.sendall(self.data.upper())
                print("Sent BOMB")
                print(str(self.data, "utf-8"))
                # WAIT FOR RESPONSE
                self.data = self.request.recv(1024).strip()
                print("RECEIVED RESPONSE")
                print(str(self.data, "utf-8"))
                # IF MISS THEN WAIT TURN ELSE CONTINUE
                if self.data == b"MISS":
                    while self.data != b"GG":
                        # WAIT FOR BOMB
                        self.data = self.request.recv(1024).strip()
                        print("GOT BOMBED")
                        print(str(self.data, "utf-8"))
                        # RESPOND
                        self.data = (bytes(random_answer(), "utf-8"))
                        self.request.sendall(self.data)

                        print("SENT RESPONSE")
                        print(str(self.data, "utf-8"))
                        # IF RESPONSE WAS MISS THEN ITS MY TURN
                        if self.data == b"MISS":
                            break


def random_answer():
    bank = ["GG", "GG", "GG", "GG", "GG"]
    index = random.randint(0, 4)
    return bank[index]


if __name__ == "__main__":
    HOST, PORT = "localhost", 8765

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
