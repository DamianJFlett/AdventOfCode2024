from collections import defaultdict
from queue import PriorityQueue
directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

f = open("test.txt", "r")
grid = []
walls = set()
for (y, l) in enumerate(f):
    grid.append(l[:-1])
    for (x, c) in enumerate(l[-1]):
        if c == "S":
            start = c
        if c == "E":
            end = c
        if c == "#":
            walls.add((x, y))
#start facing east

#consider djikstra / ucs, however nodes in some sense have to be not just the locations but encode the direction as well  ?  

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])




















""""
def build_graph(grid):
    #a graph takes the form of a dictionary mapping (x, y) -> its adjacent vertices
    graph = {}
    for (y, l) in enumerate(grid):
        for (x, c) in enumerate(l):
            for d3 in directions:
                if (x, y, d3) not in graph:
                    graph[(x, y, d3)] = []
                for d in directions:
                    if add(d, (x, y)) not in walls:
                        for d2 in directions:
                            graph[(x,y,d3)].append((x, y, d2))
    return graph


graph = build_graph(grid)
"""

