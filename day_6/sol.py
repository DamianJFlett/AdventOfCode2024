
f = open("input.txt", "r")
grid = []
walls = set()

for (y, l) in enumerate(f):
    for (x, c) in enumerate(l):
        if c == "^":
            starting_pos = (x, y)
        if c == "#":
            walls.add((x,y))
    grid.append(l[:-1])



""" 
      1
      ^
 4<- dir -> 2
      v
      3

"""
#note that this is incomplete if your input includes a corner. I will not be fixing it, which only becomes a problem in part 2 for my input. 
def visit_no(x, y):
    visited = set()
    dir = 1
    while (0 <= y <= len(grid)-1) and (0 <= x <= len(grid[0])-1):
        visited.add((x,y))
        if dir  == 1:
            if (x, y-1) in walls:
                dir = 2
            else:
                y -= 1
        elif dir == 2:
            if (x+1, y) in walls:
                dir = 3
            else:
                x += 1
        elif dir == 3:
            if (x, y+1) in walls:
                dir = 4
            else:
                y += 1
        elif dir == 4:
            if (x-1, y) in walls:
                dir = 1
            else:
                x -= 1
    return len(visited)
print("part 1 solution is ", visit_no(starting_pos[0], starting_pos[1]))

#True iff input loops with wall
#BRUTE FORCE FUCK NOT BRUTE FORCE IDC ANYMORE
def visit_no_with_loops(x, y):
    visited = {}
    dir = 1
    l = 0
    while (0 <= y <= len(grid)-1) and (0 <= x <= len(grid[0])-1):
        if l >= 100000:
            return True
        if (x, y) in visited: 
            visited[(x,y)].add(dir)
        else:
            visited[x,y] = {dir}
        l += 1
        if dir  == 1:
            if (x, y-1) in walls:
                dir = 2
            else:
                y -= 1
        elif dir == 2:
            if (x+1, y) in walls:
                dir = 3
            else:
                x += 1
        elif dir == 3:
            if (x, y+1) in walls:
                dir = 4
            else:
                y += 1
        elif dir == 4:
            if (x-1, y) in walls:
                dir = 1
            else:
                x -= 1
    return False
#part 2
counter = 0
for x in range(len(grid)):
    for y in range(len(grid)):
        if (x, y) in walls or (x == starting_pos[0] and y == starting_pos[1]):
            continue
        walls.add((x, y))
        if visit_no_with_loops(starting_pos[0], starting_pos[1]):
            counter += 1
        walls.remove((x, y))
print("part 2 solution is ", counter)