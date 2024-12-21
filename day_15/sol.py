f = open("test_3.txt", "r")


#positions as (row, col)

walls = set()
grid = []
start_pos = (0, 0)
boxes = set()
directions = []

dirs = {"^": (-1, 0), "<": (0, -1), ">": (0, 1), "v": (1, 0)}

for (row, l) in enumerate(f):
    grid.append(l[:-1])
    if "#" in l[:-1] or "." in l[:-1] or "O" in l[:-1]:
        for (col, c) in enumerate(l):
            if c == "#":
                walls.add((row, col))
            if c == "@":
                start_pos = (row, col)
            if c == "O":
                boxes.add((row, col))
    else:
        for (col, c) in enumerate(l[:-1]):
            if c in "^v><":
                directions.append(c)
            else:
                raise ValueError()

def add(x, y):
    return (x[0] + y[0], x[1]+y[1])

def move(dir, old):
    plus = dirs[dir]
    pos = old
    pos = add(pos, plus)
    if pos in walls:
        return old
    elif pos in boxes:
        box_old = pos
        box = add(pos, plus)
        while box in boxes:
            box = add(box, plus)
        if box in walls:
            return old
        else:
            boxes.remove(box_old)
            boxes.add(box)
            return pos
    else:
        return pos

def compute_total_box_coords(boxes):
    total = 0
    for box in boxes:
        total += box[0] * 100 + box[1]
    return total


old_boxes = boxes
#move once
pos = move(directions[0], start_pos)
for dir in directions[1:]:
    pos = move(dir, pos)
print("part one solution is ", compute_total_box_coords(boxes))

#part 2


#lets just let the x coordinate be the left half of the box
boxes = old_boxes
new_walls = set()
for wall in walls:
    new_walls.add((wall[0], 2*wall[1]))
    new_walls.add((wall[0], 2*wall[1]+1))
walls = new_walls
new_boxes = set()
for box in boxes:
    new_boxes.add((box[0], 2*box[1]))
boxes = new_boxes


def get_neighbours(pos, dir):
    plus = dirs[dir]
    if dir in "^v":
        return [x for x in [add(pos, plus), add(add(pos, plus), dirs["<"])] if x in boxes]
    if dir == ">":
        return [x for x in [add(pos, plus)] if x in boxes]
    if dir == "<":
        return [x for x in [add(add(pos, plus), dirs["<"])] if x in boxes]

#solving this stupidly
def push(pos, dir):
    plus = dirs[dir]
    to_be_moved = set()
    #bfs
    queue = [pos]
    to_be_moved.add(pos)
    while queue:
        removed = queue.pop(0)
        for node in get_neighbours(removed, dir):
            if node not in to_be_moved:
                #TODO: change the logic here so that both sides of the box are always added to the queue
                if dir == ">":
                    queue.append(node)
                    to_be_moved.add(node)
                    queue.append((node[0], node[1]+1))
                    to_be_moved.add((node[0], node[1]+1))
                if dir == "<":
                    iueue.append(node)
                    queue.append((node[0], node[1]-1))
                    to_be_moved.add(node)
                    to_be_moved.add((node[0], node[1]-1))
                if dir == "v": # NOT DONE FROM HERE! DIFF DIRS AND CONSIDER CASES OF WHICH SIDE
                    queue.append(node)
                    to_be_moved.add(node)
                    if (node[0], node[1]-1) in boxes:
                        to_be_moved.add((node[0], node[1]-1))
                        queue.append((node[0], node[1]-1))
                    else:
                        to_be_moved.add((node[0], node[1]+1))
                        queue.append((node[0], node[1]+1))
                if dir == "^":
                    queue.append(node)
                    to_be_moved.add(node)
                    if (node[0], node[1]-1) in boxes:
                        to_be_moved.add((node[0], node[1]-1))
                        queue.append((node[0], node[1]-1))
                    else:
                        to_be_moved.add((node[0], node[1]+1))
                        queue.append((node[0], node[1]+1))
    return to_be_moved

def move_2(dir, old):
    plus = dirs[dir]
    pos = old
    pos = add(pos, plus)
    if pos in walls:
        return old
    pushed = push(pos, dir)
    if any([pos in walls for pos in pushed]):
        return old
    else:
        added = set()
        removed = set()
        for box in pushed:
            removed.add(box)
            added.add(add(box, plus))
        print(dir, boxes)
        boxes.difference_update(removed)
        boxes.update(added)
        print(dir, boxes)
        return pos
#for part 2
def print_grid():
    printer = ""
    for row in range(len(grid)):
        printer += "\n"
        col = 0
        while col in range(len(grid[0]) * 2):
            if (row, col) in walls:
                printer += "#"
            if (row, col) in boxes:
                printer+= "[]"
                col += 1
            if (row, col) == pos:
                printer += "@"
            else:
                printer += "."
            col += 1
    print(printer)

pos = move_2(directions[0], start_pos)
for dir in directions[1:]:
    print_grid()
    pos = move_2(dir, pos)

print("part two solution is ", compute_total_box_coords(boxes))