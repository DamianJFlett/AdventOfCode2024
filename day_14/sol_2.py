import re
import matplotlib.pyplot as plt 
from time import sleep
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
    pos = add(pos,vel)
    return (pos[0] % width, pos[1] % height)

def move_all(pos):
    new = []
    for (index, x) in enumerate(pos):
        new.append(move(x, vs[index]))
    return new



def print_positions_console(pos):
    printer = "" 
    for y in range(height):
        printer+= "\n"
        for x in range(width):
            if (x, y) in init:
                printer += "#"
            else:
                printer += "."
    printer += "\n"
    for x in range(width):
        printer += "_"
    print(printer)
def print_positions(pos):
    x = [a[0] for a in pos]
    y = [a[1] for a in pos]
    plt.scatter(x, y)
    plt.show(block = False)
    plt.close()

time = 0
while True:
    if len(set(init))== len(init):
        print_positions_console(init)
        print(time)
    time += 1
    init = move_all(init)
    