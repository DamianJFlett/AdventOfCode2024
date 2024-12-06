f = open("input.txt", "r")
grid = []
walls = []
visited = set()

for (y, l) in enumerate(f):
    for (x, c) in enumerate(l):
        if c == "^":
            starting_pos = (x, y)
        if c == "#":
            walls.append((x,y))
    grid.append(l[:-1])


x, y = starting_pos
dir = 1
""" 
      1
      ^
 4<- dir -> 2
      v
      3

"""
visited.add((x,y))
while (0 <= y <= len(grid)-1) and (0 <= x <= len(grid[0])-1):
    visited.add((x,y))
    if dir  == 1:
        if (x, y-1) in walls:
            dir = 2
            x += 1
        else:
            y -= 1
    elif dir == 2:
        if (x+1, y) in walls:
            dir = 3
            y += 1
        else:
            x += 1
    elif dir == 3:
        if (x, y+1) in walls:
            dir = 4
            x -= 1
        else:
            y += 1
    elif dir == 4:
        if (x-1, y) in walls:
            dir = 1
            y -= 1
        else:
            x -= 1
    print(x, y)
print(visited)
print("part 1 solution is ", len(visited))
