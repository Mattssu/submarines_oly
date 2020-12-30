import SubmarineGameManager
import client
import host

WELCOME_MESSAGE = "Welcome to a game of SUBMARINES"
CHOICE = "Choose Host or Client: 1 or 2\n"
HOST = "1"
CLIENT = "2"

WRONG_INPUT = "Wrong input , try again"


class GameClient:

    def menu(self):
        try:
            print(WELCOME_MESSAGE)
            submarine_game = SubmarineGameManager.SubmarineGame()
            submarine_game.init_submarine_locations()
            while True:
                choice = input(CHOICE)
                if choice == HOST:
                    host.host_connect(submarine_game)
                elif choice == CLIENT:
                    client.client_connect(submarine_game)
                else:
                    raise ValueError
        except ValueError:
            print(WRONG_INPUT)


if __name__ == '__main__':
    game_client = GameClient()
    game_client.menu()
