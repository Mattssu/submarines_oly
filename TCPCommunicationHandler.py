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

            while self.data != "GG":
                self.user_bomb_input()
                self.data = (bytes(self.data, "utf-8"))
                self.request.sendall(self.data.upper())

                self.data = self.request.recv(1024).strip()

                if self.data == "MISS":
                    while self.data != "GG":

                        self.data = self.request.recv(1024).strip()
                        print(self.data)

                        self.data = (bytes(random_answer(), "utf-8"))
                        self.request.sendall(self.data)

                        if self.data == "MISS":
                            break

                        # if b"gg" == self.data or b"GG" == self.data:
                        # TODO TEST the thing


def random_answer():
    bank = ["MISS", "MISS", "MISS", "HIT", "SINK"]
    index = random.randint(0, 4)
    return bank[index]


if __name__ == "__main__":
    HOST, PORT = "localhost", 8765

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        server.serve_forever()
