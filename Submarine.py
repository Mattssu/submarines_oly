class Submarine:
    def __init__(self, size, location_1, location_2):
        self.location_1 = location_1
        self.location_2 = location_2
        self.size = size
        self.locations = {}
        self.init_locations()
        print("Locations set")  # todo remove

    def init_locations(self):
        x_1, y_1 = self.location_1
        x_2, y_2 = self.location_2
        if x_1 == x_2:
            if y_1 > y_2:
                for i in range(y_2, self.size):
                    self.locations[(x_1, i)] = False
            else:
                for i in range(y_1, self.size):
                    self.locations[(x_1, i)] = False
        else:
            if x_1 > x_2:
                for i in range(x_2, self.size):
                    self.locations[(i, y_1)] = False
            else:
                for i in range(x_1, self.size):
                    self.locations[(i, y_1)] = False

    def hit_location(self, location):
        # todo check dict errors try catch
        if not self.locations[location]:
            self.locations[location] = True

    def is_sink(self):
        counter = 0
        for location in self.locations:
            if self.locations[location] is True:
                counter += 1
        if counter == self.size:
            return True
        else:
            return False
