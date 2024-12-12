from collections import defaultdict
f = open("input.txt", "r")


grid = []
for l in f:
    grid.append(l[:-1])

def get_neighbours(row, col):
    x = []
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for d in directions:
        if 0 <= row+d[0] <= len(grid[0]) - 1 and 0 <= col+d[1] <= len(grid) - 1:
            if grid[row+d[0]][col+d[1]] == grid[row][col]:
                x.append((row+d[0],col+d[1]))
    return x



areas = defaultdict(int)

def bfs(row, col):
    row = int(row)
    col = int(col)
    queue = [(row, col)]
    seen = set()
    seen.add((row, col))
    while len(queue) > 0:
        removed = queue.pop(0)
        for node in get_neighbours(removed[0], removed[1]):
            if node not in seen:
                queue.append(node)
                seen.add(node)
    return seen

comps = []
for row, l in enumerate(grid):
    for col, c in enumerate(grid):
        if not any([((row, col) in comp) for comp in comps]):
            comps.append(bfs(row, col))

def per(comp):
    p = 0
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    for point in comp:
        for d in directions:
            if (point[0]+d[0], point[1]+d[1]) not in comp:
                p += 1
    return p

total = 0
for comp in comps:
    area = len(comp)
    perimeter = per(comp)
    total += perimeter * area

print("part 1 solution is, ",  total)


def sides(comp):
    sides = set()
    for side in comp:
        if side in sides

def same_side(comp, p1, p2):
    pass

total = 0
for comp in comps:
    area = len(comp)
    perimeter = sides(comp)
    total += perimeter * area

# #grid is square
# for l in grid:
#     for c in l:
#         areas[c] += 1

# #idea for perimeters - iterate through rows, putting perimeter where it changes and later identify these perimeters, then through columns

# # handle l -> r changes here
# perimeters = defaultdict(int)
# for (row, l) in enumerate(grid):
#     cur = grid[row][0]
#     for (col, c) in enumerate(l):
#         if c != cur:
#             perimeters[c] += 1
#             perimeters[cur] += 1
#         if row == 0 or row == len(grid) - 1:
#             perimeters[c] += 1
#         if col == 0 or col == len(grid[0]) - 1:
#             perimeters[c] += 1
#         cur = c

# #handle up -> down changes here

# for j in range(len(grid[0])):
#     cur = grid[0][j]
#     for i in range(len(grid)):
#         if grid[i][j] != cur:
#             perimeters[grid[i][j]] += 1
#             perimeters[cur] += 1
#         cur = grid[i][j]
# print(perimeters, areas)

