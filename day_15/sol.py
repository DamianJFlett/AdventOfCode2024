f = open("test.txt", "r")


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

def print_grid():
    pass
old_boxes = boxes
#move once
pos = move(directions[0], start_pos)
for dir in directions[1:]:
    pos = move(dir, pos)
print("part one solution is ", compute_total_box_coords(boxes))

#part 2
boxes = old_boxes

for dir in directions[1:]:
    pos = move(dir, pos)

print("part one solution is ", compute_total_box_coords(boxes))