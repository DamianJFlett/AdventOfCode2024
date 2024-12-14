import re
f = open("input.txt", "r")
init = []
vs = []
width = 101
height = 103

def get_position_vel(s):
    match = re.search(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", s)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        num3 = int(match.group(3))
        num4 = int(match.group(4))
        return num1, num2, num3, num4

for l in f:
    x = get_position_vel(l[:-1])
    init.append((x[0], x[1]))
    vs.append((x[2], x[3]))

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def move(pos, vel):
    for i in range(100):
        pos = add(pos,vel)
    return (pos[0] % width, pos[1] % height)

finals = []
for (index, pos) in enumerate(init):
    finals.append(move(pos, vs[index]))

q1 = 0
q2 = 0
q3 = 0
q4 = 0
for pos in finals:
    if pos[0] == width // 2 or pos[1] == height // 2:
        continue
    if pos[0] < width // 2:
        if pos[1] < height // 2:
            q1 += 1
        else:
            q2 += 1
    else:
        if pos[1] < height // 2:
            q3 += 1
        else:
            q4 += 1
print(q1, q2, q3, q4, q1*q2*q3*q4)