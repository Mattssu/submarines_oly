class Submarine:
    def __init__(self, size, location_1, location_2):
        # TODO LOCATION FIX
        self.location_1 = location_1
        self.location_2 = location_2
        self.size = size
        self.locations = []
        self.init_locations()
        print("Locations set")

    def init_locations(self):
        x_1, y_1 = self.location_1
        x_2, y_2 = self.location_2
        if x_1 == x_2:
            if y_1 > y_2:
                for i in range(y_2, self.size):
                    self.locations.append((x_1, i))
            else:
                for i in range(y_1, self.size):
                    self.locations.append((x_1, i))
        else:
            if x_1 > x_2:
                for i in range(x_2, self.size):
                    self.locations.append((i, y_1))
            else:
                for i in range(x_1, self.size):
                    self.locations.append((i, y_1))

    def hit_location(self, location):
        pass

    def is_sink(self):
        pass
