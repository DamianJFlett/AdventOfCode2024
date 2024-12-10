import itertools
f = open("input.txt", "r")

grid = []

for (row, l) in enumerate(f):
    grid.append(l[:-1])


def get_neighbours(row, col):
    row = int(row)
    col = int(col)
    x = []
    for coords in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
        if 0 <= coords[0] <= len(grid[0]) - 1 and 0 <= coords[1] <= len(grid) - 1:
            if int(grid[coords[0]][coords[1]]) == int(grid[row][col])  + 1:
                x.append((coords[0], coords[1]))
    return x


def bfs(row, col, goal):
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
    found = 0
    for i in seen:
        if int(grid[i[0]][i[1]]) == 9:
            found += 1
    return found

def get_permutations(items):
    return list(itertools.permutations(items))

#part 2 idea - look instead at all permutations of get_neighbours somehow. Recrusive version makes sense?
def bfs_super(row, col, goal):
    found = 0
    row = int(row)
    col = int(col)
    queue = [(row, col)]
    seen = set()
    seen.add((row, col))
    while len(queue) > 0:
        removed = queue.pop(0)
        for node in get_neighbours(removed[0], removed[1]):
            queue.append(node)
            seen.add(node)
            if int(grid[node[0]][node[1]]) == 9:
                found += 1
    return found


total = 0
for (row, l) in enumerate(grid):
    for (col, c) in enumerate(l):
        if c == '0':
            total += bfs(row, col, 9)

print("Part 1 solution is ", total)
total2 = 0
for (row, l) in enumerate(grid):
    for (col, c) in enumerate(l):
        if c == '0':
            total2 += bfs_super(row, col, 9)
print("part 2 solution is ", total2)