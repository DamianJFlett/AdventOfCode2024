f = open("input.txt", "r")
from math import gcd

total = 0
antennas = {}
antinodes = set()

grid = []
for (x, l) in enumerate(f):
    grid.append(l[:-1])
    for (y, c) in enumerate(l):
        if c not in [".", "\n"]:
            antennas[(x,y)] = c
for a in antennas:
    for b in antennas:
        if b == a:
            continue
        if antennas[a]==antennas[b]:
            dist_x = a[0]-b[0]
            dist_y = a[1]-b[1]
            g = gcd(dist_x, dist_y)
            dist_x, dist_y = int(dist_x/g), int(dist_y/g)
            #why yes, this is hideously inefficient
            for i in range(50):
                if 0 <= a[0]+i*dist_x <= len(grid)-1 and 0 <= a[1]+i*dist_y <= len(grid[0])-1:
                    antinodes.add((a[0]+i*dist_x, a[1]+i*dist_y))
                if 0 <= b[0]-i*dist_x <= len(grid)-1 and 0 <= b[1]-i*dist_y <= len(grid[0])-1:
                    antinodes.add((b[0]-i*dist_x, b[1]-i*dist_y))
print("part 2 soln is ", len(antinodes))