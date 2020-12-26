from collections import deque
import time

start_time = time.time()
with open("3_input.txt") as f:
    mylist = f.read().splitlines()

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = 1
part1 = 0

for slope in slopes:
    rotate = slope[0]
    char = []
    for a in mylist[slope[1]::slope[1]]:
        a = deque(a)
        a.rotate(-rotate)
        char.append(a[0])
        rotate += slope[0]

    # hold result for part 1:
    if slope == (3, 1):
        part1 = char.count("#")
    trees = trees * char.count("#")

print(f"Day 3 Part 1: {part1}")
print(f"Day 3 Part 2: {trees}")
print(f"--- {time.time() - start_time} seconds ---")
