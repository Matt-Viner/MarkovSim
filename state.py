import random

class State():
    def __init__(self, name: str, dist: list) -> None:
        self.name = name
        self.dist = dist
    
    def get_dist(self):
        return self.dist

    def get_random_value(self):
        return random.choice(self.dist)
