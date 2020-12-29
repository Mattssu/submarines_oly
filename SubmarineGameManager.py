import Submarine

GAME_SIZE = 10


class SubmarineGame:
    def __init__(self):
        self.game_map = []
        self.game_map_size = GAME_SIZE
        self.init_map()
        self.submarines = []

    def init_map(self):
        for row in range(self.game_map_size):
            self.game_map.append([])
            for col in range(self.game_map_size):
                self.game_map[row].append("O")

    def is_within_range(self, num):
        return self.game_map_size > num >= 0

    def location_input(self, size):
        try:
            x_1 = int(input("Loc 1 , X Value:"))
            y_1 = int(input("Loc 1 , Y Value:"))
            x_2 = int(input("Loc 2 , X Value:"))
            y_2 = int(input("Loc 2 , Y Value:"))

            if not (self.is_within_range(x_1) and self.is_within_range(y_1) and self.is_within_range(
                    x_2) and self.is_within_range(y_2)):
                print("Values not in range , try again")
                return self.location_input(size)

            if not (x_1 == x_2 or y_1 == y_2):
                print("Values not logical (no diagonal placement) , try again")
                return self.location_input(size)

            if x_1 == x_2:
                if abs(y_2 - y_1) != size - 1:
                    raise Exception
            else:
                if abs(x_2 - x_1) != size - 1:
                    raise Exception

            return (x_1, y_1), (x_2, y_2)
        except ValueError:
            print("Location is not an integer number")
            return self.location_input(size)
        except Exception:
            print("Values not logical (wrong size placement), try again")
            return self.location_input(size)

    def add_submarine_to_game_map(self, submarine):
        for location in submarine.locations:
            x, y = location
            self.game_map[y][x] = submarine

    def place_submarine_on_board(self, size):
        print("Size " + str(size))
        location_1, location_2 = self.location_input(size)
        submarine = Submarine.Submarine(size, location_1, location_2)
        self.submarines.append(submarine)
        self.add_submarine_to_game_map(submarine)

    def init_submarine_locations(self):
        try:
            self.place_submarine_on_board(5)
            print("Placed")
        except KeyError:
            pass
        # TODO sanity checks

    def draw_game(self):
        drawing = []
        for row in self.game_map:
            line = []
            for col in row:
                if col != "O" and col != "X":
                    line.append("S")
                else:
                    line.append(col)
            drawing.append(line)
        for line in drawing:
            print(line)

    def bomb_location(self, location):
        pass


sub = SubmarineGame()
sub.init_submarine_locations()
sub.draw_game()
print("Test")
