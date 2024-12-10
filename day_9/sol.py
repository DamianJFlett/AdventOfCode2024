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
def check_valid(s):
    first_dot = s.index('.')
    return all(c != '.' for c in s[:first_dot]) and all(c == '.' for c in s[first_dot:])

n = len(s2)
total = 0
for end_index in range(n - 1, -1, -1):
    if s2[end_index] != '.':
        for start_index in range(n):
            if s2[start_index] == '.':
                s2[start_index], s2[end_index] = s2[end_index], '.'
                break
    if check_valid(s2):
        break
for index, c in enumerate(s2):
    if c == '.':
        break
    total += index * int(c)

print("part 1 solution is", total)