import numpy as np


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x},{self.y})"


class LineSegment:
    def __init__(self, x1, y1, x2, y2):
        self.start = Point(x1, y1)
        self.end = Point(x2, y2)

    @property
    def minX(self):
        return min(self.x1, self.x2)

    @property
    def minY(self):
        return min(self.y1, self.y2)

    @property
    def maxX(self):
        return max(self.x1, self.x2)

    @property
    def maxY(self):
        return max(self.y1, self.y2)

    @property
    def x1(self):
        return self.start.x

    @property
    def y1(self):
        return self.start.y

    @property
    def x2(self):
        return self.end.x

    @property
    def y2(self):
        return self.end.y

    def get_points_on_vert_horiz_line(self):
        pass

    @property
    def points_on_line(self):
        if self.x1 == self.x2:
            # Vertical line
            return [Point(self.x1, y) for y in range(self.minY, self.maxY + 1)]
        elif self.y1 == self.y2:
            # Horizontal line
            return [Point(x, self.y1) for x in range(self.minX, self.maxX + 1)]
        else:
            # Diagonal line
            x_values = range(self.minX, self.maxX + 1)
            y_values = range(self.minY, self.maxY + 1)
            if self.x1 > self.x2:
                x_values = reversed(x_values)
            if self.y1 > self.y2:
                y_values = reversed(y_values)
            return [Point(x, y) for x, y in zip(x_values, y_values)]

    def __repr__(self):
        return f"(Line: ({self.x1},{self.y1}) -> ({self.x2},{self.y2}))"

class HydroThermalVents:
    def __init__(self, filename):
        self.lines = []
        with open(filename) as f:
            for line in f:
                first, second = line.strip().split(" -> ")
                x1, y1 = first.split(",")
                x2, y2 = second.split(",")
                self.lines.append(LineSegment(int(x1), int(y1), int(x2), int(y2)))
        maxX = max([line.maxX for line in self.lines])
        maxY = max([line.maxY for line in self.lines])
        self.grid = np.zeros((maxX + 1, maxY + 1)).astype(int)

    @property
    def allX1(self):
        return [line.x1 for line in self.lines]

    @property
    def allY1(self):
        return [line.y1 for line in self.lines]

    @property
    def allX2(self):
        return [line.x2 for line in self.lines]

    @property
    def allY2(self):
        return [line.y2 for line in self.lines]

    def print_grid(self):
        for row in self.grid:
            for col in row:
                if col == 0:
                    col = "."
                print(col, end="")
            print()

    def run(self):
        for line in self.lines:
            for point in line.points_on_line:
                self.grid[point.y, point.x] += 1
        points = self.grid[self.grid >= 2]
        self.print_grid()
        print("Points where at least 2 lines overlap:", len(points))


if __name__ == "__main__":
    print("Part 1")
    vents = HydroThermalVents("input.txt")
    vents.run()