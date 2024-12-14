from collections import defaultdict
f = open("test.txt", "r")


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


#get connected components, adjacency defined by cardinally adjacent & same letter
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

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

# def valid_ver(comp, side):
#     if not len(side) == 1:
#         return True
#     directions = [(0, -1),(0, 1)]
#     [l] = side
#     for d in directions:
#         if add(l, d) in comp:
#             return True
#     return False

# def construct_side_vert(comp, point):
#     side = set()
#     p = point
#     while p in comp:
#         side.add(p)
#         if (p[0]-1, p[1]) in comp or (p[0]+1, p[1]) in comp:
#             break
#         p = (p[0], p[1]+1)
#     p = point
#     while p in comp:
#         side.add(p)
#         if (p[0]-1, p[1]) in comp or (p[0]+1, p[1]) in comp:
#             break
#         p = (p[0], p[0]-1)
#     return side


# def valid_hor(comp, side):
#     if not len(side) == 1:
#         return True
#     directions = [(-1, 0),(1, 0)]
#     [l] = side
#     for d in directions:
#         if add(l, d) in comp:
#             return True
#     return False

# def construct_side_hor(comp, point):
#     side = set()
#     p = point
#     while p in comp:
#         side.add(p)
#         if (p[0], p[1]-1) in comp or (p[0], p[1]+1) in comp:
#             break
#         p = (p[0]+1, p[1])
#     p = point
#     while p in comp:
#         side.add(p)
#         if (p[0], p[1]-1) in comp or (p[0], p[1]+1) in comp:
#             break
#         p = (p[0]-1, p[0])
#     return side


# def s(comp):
#     sides = []
#     for point in comp:
#         hor = construct_side_hor(comp, point)
#         ver = construct_side_vert(comp, point)
#         if not hor in sides and valid_hor(comp, hor):
#             sides.append(hor)
#         if not ver in sides and valid_ver(comp, ver):
#             sides.append(ver)
#     return len(sides)


#another approach to sidefinding - find the boundary, in order and count right angles? 


#maybe inplace with bfs?

"""
return (area, sides, whole component)
"""
def bfs_count_sides(row, col):
    row = int(row)
    col = int(col)
    queue = [(row, col)]
    seen = set()
    seen.add((row, col))
    sides = 0
    boundary = [] #to check - if we look around and find somewhere not inside, we're a boundary

    while len(queue) > 0:
        removed = queue.pop(0)
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        for d in directions:
            p = add(d, removed)
            if not (0 <= p[0] < len(grid)) or not (0 <= p[1] < len(grid[1])): # not enough
                boundary.append(removed)
        for node in get_neighbours(removed[0], removed[1]):
            if node not in seen:
                queue.append(node)
                seen.add(node)  
    while boundary:
        print(boundary.pop(0))
    return (sides, seen)


print(bfs_count_sides(0, 0))
for (row, l) in enumerate(grid):
    for (col, c) in enumerate(l):
        pass

# total = 0
# for comp in comps:
#     area = len(comp)
#     sides = s(comp)
#     print(comp, area, sides)
#     total += sides * area

# print("part 2 solution is ", total)










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

