import numpy as np

with open('input.txt') as f:
    positions = np.array(f.readline().strip().split(",")).astype(int)

print("Part 1:", min([np.abs(positions - position).sum() for position in positions]))

costs = {i: sum(range(i+1)) for i in range(positions.max() + 1)}
print("Part 2:", min([sum([costs[distance] for distance in np.abs(positions - position)]) for position in range(positions.max() + 1)]))
#print("Part 2:", min([sum([sum(range(distance+1)) for distance in np.abs(positions - position)]) for position in range(positions.max() + 1)]))

