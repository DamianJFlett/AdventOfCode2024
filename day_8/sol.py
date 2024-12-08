f = open("input.txt", "r")


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
            if 0 <= a[0]+dist_x <= len(grid)-1 and 0 <= a[1]+dist_y <= len(grid[0])-1:
                antinodes.add((a[0]+dist_x, a[1]+dist_y))
            if 0 <= b[0]-dist_x <= len(grid)-1 and 0 <= b[1]-dist_y <= len(grid[0])-1:
                antinodes.add((b[0]-dist_x, b[1]-dist_y))
print("part 1 soln is ", len(antinodes))