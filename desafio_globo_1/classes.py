class Player:
    def __init__(self, name):
        self.name = name
        self.points = 0

    def add_points(self, points):
        self.points += points
    
    def clear_score(self):
        self.points = 0

    def print_score(self):
        print(self.name + ' has ' + str(self.points) + ' points')