
## fix thsi 
with open("input.txt", "r") as f:
    s = "".join(line.strip() for line in f)

pos = 0
free = False
cur_id = 0
s2 = []

for c in s:
    if free:
        s2.extend(['.'] * int(c))
    else:
        s2.extend([str(cur_id)] * int(c))
        cur_id += 1
    free = not free

n = len(s2)
# idea : write a dictionary mapping lengths of runs of . onto a list of places
#  where that index starts, this can be modified in place as we run through

free_spaces = {}
index = 0
while index < n:
    c = s2[index]
    if c == '.':
        cur_char = c
        old = index
        while cur_char == '.':
            if index == n-1:
                index += 1
                break
            cur_char = s2[index]
            index = index + 1
        rl = index - old -1
        if rl in free_spaces:
            free_spaces[rl].append(old)
        else:
            free_spaces[rl] = [old]
        continue
    index += 1
for i in range(1, 10):
    if i not in free_spaces:
        free_spaces[i] = []


#now, lets build up a dictionary from this such that each runlength has all the spaces  > that as well

keys = sorted(free_spaces.keys(), reverse = 1)
earliest = {}
seen = set()
for key in keys:
    seen.update(free_spaces[key])
    earliest[key] = sorted(seen)


#idea - do the same thing but for the run lengths of ids. this will help us to only traverse the list once.... maybe
rls = {}
index = 0
while index < n:
    c = s2[index]
    if c != '.':
        cur_char = c
        old = index
        while cur_char == c:
            if index == n:
                index += 1 
                break
            cur_char = s2[index]
            index = index + 1
        rl = index - old -1 
        #this will not work if s2 ends in .
        if c == s2[-1]:
            rls[c] = (index - old, old-1)
        else:
            rls[c] = (rl, old) 
        continue
    index += 1

def update_earliest(x):
    mod = 0
    free_spaces = {}
    index = 0
    while index < n:
        c = s2[index]
        if c == '.':
            cur_char = c
            old = index
            while index < n and cur_char == '.':
                cur_char = s2[index]
                index = index + 1
            rl = index - old -1
            if index == n:
                if rl+1 in free_spaces:
                    free_spaces[rl+1].append(old)
                else:
                    free_spaces[rl+1] = [old]
            else:
                if rl in free_spaces:
                    free_spaces[rl].append(old)
                else:
                    free_spaces[rl] = [old]
            continue
        index += 1
    for i in range(1, 10):
        if i not in free_spaces:
            free_spaces[i] = []


    #now, lets build up a dictionary from this such that each runlength has all the spaces  > that as well

    keys = sorted(free_spaces.keys(), reverse = 1)
    x = {}
    seen = set()
    for key in keys:
        seen.update(free_spaces[key])
        x[key] = sorted(seen)
    return x
# manipulate s2 finally
for c in sorted(rls.keys(), reverse = True):
    rl, old = rls[c]
    if len(earliest[rl]) == 0:
        continue
    place = earliest[rl][0]
    if place >= old:
        continue
    for i in range(rl):
        s2[old+i], s2[place +i] = s2[place + i],  s2[old+i]
    earliest = update_earliest(earliest) 

print(s2)
total = 0
for index, c in enumerate(s2):
    if c == '.':
        continue
    total += index * int(c)

print("part 2 solution is", total)

# some learnings/notes from this as I've done it. In terms of optimisation, this looks like a math problem. I have avaiable info I've simply chosen not to use in 
# part 1 - after s2 is generated, the runs fo ids are in ascending order and unique. 
# also write this in separate functions you ape