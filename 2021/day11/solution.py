import sys; sys.path.append("../"); from utils import *
import numpy as np
from tqdm import tqdm


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
        self.steps = 100
        self.num_flashes = 0

    def get_value(self, location):
        y, x = location
        height, width = self.grid.shape
        if y < 0 or y >= height or x < 0 or x >= width:
            return None
        return self.grid[y, x]

    def increment_grid(self):
        self.grid = (self.grid + 1) % 10

    def run(self):
        for _ in tqdm(range(1, self.steps + 1)):
            self.increment_grid()
            i = 0
            while True:
                if i > 0:
                    # keep track of where the zeros are that were just used
                    zeros = np.where(self.grid == 0)
                    # set all 10 or greater to zero (flashes)
                    self.grid[np.where(self.grid >= 10)] = 0
                    # get locations of all non-zero values
                # iterate over all non-zero locations, and increment them for each adjacent zero
                locations = np.argwhere(self.grid != 0)
                if i > 0:
                    # set old zeros to -1 so they don't repeat
                    self.grid[zeros] = -1
                for location in locations:
                    for direction in self.directions:
                        adj_loc = location + direction
                        if self.get_value(adj_loc) == 0:
                            self.grid[location[0], location[1]] += 1
                if i > 0:
                    self.grid[np.where(self.grid == -1)] = 0
                i += 1
                if self.grid[self.grid > 9].sum() == 0:
                    self.num_flashes += len(self.grid[self.grid == 0])
                    break
                #if i > 10:
                #    breakpoint()
                #    break
        print("Part 1:", self.num_flashes)
            


if __name__ == "__main__":
    oct = Octopuses("sample.txt")
    oct.run()
