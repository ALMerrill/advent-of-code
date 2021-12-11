import sys; sys.path.append("../"); from utils import *
import numpy as np


class Octopuses:
    def __init__(self, filename):
        lines = read_file_lines(filename)
        grid = []
        for line in lines:
            values = [int(value) for value in line]
            grid.append(values)
        self.grid = np.array(grid)
        self.directions = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, -1],
            [0, 1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        self.steps = 2

    def get_value(self, location):
        y, x = location
        height, width = self.grid.shape
        if y < 0 or y >= height or x < 0 or x >= width:
            return None
        return self.grid[y, x]

    def increment_grid(self):
        self.grid = (self.grid + 1) % 10

    def run(self):
        print(self.grid)
        for step in range(self.steps):
            print("Step:", step)
            self.increment_grid()
            # TODO: change this so instead of doing it twice, it is in a while loop
            # condition for while would be while the board is the same before and after? or maybe just while there are tens to check?
            locations = np.argwhere(self.grid != 0)
            for location in locations:
                for direction in self.directions:
                    adj_loc = location + direction
                    if self.get_value(adj_loc) == 0:
                        self.grid[location[0], location[1]] += 1
            zeros = np.where(self.grid == 0)
            self.grid[np.where(self.grid == 10)] = 0
            locations = np.argwhere(self.grid != 0)
            self.grid[zeros] = -1
            for location in locations:
                for direction in self.directions:
                    adj_loc = location + direction
                    if self.get_value(adj_loc) == 0:
                        self.grid[location[0], location[1]] += 1
            self.grid[np.where(self.grid == -1)] = 0
            print(self.grid)
            


if __name__ == "__main__":
    oct = Octopuses("sample.txt")
    oct.run()
