from tqdm import tqdm
from copy import deepcopy

with open("input.txt") as f:
    all_fish = f.readline().strip().split(",")
    all_fish = [int(fish) for fish in all_fish]

fish_counts = {timer: 0 for timer in range(9)}
for fish in all_fish:
    fish_counts[fish] += 1
print(fish_counts)

num_fish = 0
#for i in tqdm(range(18)):
for i in range(256):
    fish_counts_copy = deepcopy(fish_counts)
    for timer in reversed(range(9)):
        fish_counts[timer] = fish_counts_copy[(timer +1) % 9]
        if timer == 0:
            fish_counts[6] += fish_counts_copy[timer]
    print(fish_counts)

print(sum([count for count in fish_counts.values()]))
