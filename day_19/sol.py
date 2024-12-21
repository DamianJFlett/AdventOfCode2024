from collections import defaultdict
import math


f = open("input.txt", "r")

designs = []
for (index, l) in enumerate(f):
    if index == 0:
        towels = l.split(',')
    elif l == "\n":
        continue
    else:
        designs.append(l[:-1])



for (i, t) in enumerate(towels):
    if i ==0:
        continue
    towels[i] = towels[i][1:]
    if i == len(towels) - 1:
        towels[i] = towels[i][:-1]
max_l = max([len(t) for t in designs])
min_towel = min([len(t) for t in towels])
max_towels = math.ceil(max_l // min_towel)

#approach 2 - proud of this! basically, snip off the start of the string if it is a towel, and keep going until either you  get to an empty string
#or you've done everything you can - no snipping can be done. 
total = 0
for design in designs:
    design_ends = {design}
    while "" not in design_ends:
        updated_design_ends = set()
        added = False
        for d in design_ends:
            for t in towels:    
                if d.startswith(t):
                    l = len(t)
                    updated_design_ends.add(d[l:])
                    added = True
        if not added:
            break
        design_ends = updated_design_ends
    if ""  in design_ends:
        total += 1
print("part one solution is ", total)

#part 2 
total = 0
for design in designs:
    design_ends = defaultdict(int)
    design_ends[design] = 1
    while True:
        updated_design_ends = defaultdict(int)
        added = False
        for d in design_ends:
            for t in towels:    
                if d.startswith(t):
                    l = len(t)
                    updated_design_ends[d[l:]] += design_ends[d]
                    added = True
        if not added:
            break
        design_ends = updated_design_ends
        total += design_ends[""]
print("part 2 solution is ", total)

#build possible towels  < max length - attempt 1
"""
possible = set(towels)
while True:
        for towel1 in towels:
            progress = False
            for towel2 in possible:
                towel = towel1 + towel2
                if len(towel):
                    possible.add(towel)
                    progress = True
                
            


total = 0
for design in designs:
    if design in possible:
        total += 1
print("part one solution is total")
"""