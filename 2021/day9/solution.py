import sys; sys.path.append("../"); from utils import *
import numpy as np
import operator
import functools

def is_in_matrix(matrix, position):
    i = position[0]
    j = position[1]
    return i >= 0 and i < matrix.shape[0] and j >= 0 and j < matrix.shape[1]

def get_value(matrix, position):
    if is_in_matrix(matrix, position):
        return matrix[position[0], position[1]]
    return None

def is_lower(cur_value, other_value):
    if other_value is None:
        return True
    return cur_value < other_value

def is_low_point(i, j, heights):
    value = heights[i][j]
    cur_point = (i, j)
    positions = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    is_lowers = [is_lower(value, get_value(heights, position)) for position in positions]
    return sum([int(lower) for lower in is_lowers]) == 4
    
    

lines = read_file_lines("input.txt")

heights = np.array([[char for char in line] for line in lines]).astype(int)

low_values = []
low_points = []
for i, row in enumerate(heights):
    for j, item in enumerate(row):
        if is_low_point(i, j, heights):
            low_values.append(heights[i, j])
            low_points.append((i, j))

print("Part 1:", (np.array(low_values) + 1).sum() )



def search(matrix, i, j, count, visited, points):
    if (i,j) in visited:
        return count
    visited.append((i, j))
    if not is_in_matrix(matrix, (i, j)) or matrix[i, j] == 9:
        return count
    else:
        points.append((i,j))
        count += 1 
        for position in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
            search(matrix, position[0], position[1], count, visited, points)
    return count

basin_sizes = []
for low_point in low_points:
    i, j = low_point
    count = 0
    visited = []
    points = []
    search(heights, i, j, count, visited, points)
    basin_size = len(points)
    if len(basin_sizes) == 3:
        largers = [basin_size > size for size in basin_sizes]
        if sum([int(larger) for larger in largers]) > 0:
            index = largers.index(True)
            del basin_sizes[index]
            basin_sizes.append(basin_size)
    else:
        basin_sizes.append(basin_size)
print("Part 2:", functools.reduce(operator.mul, basin_sizes, 1))