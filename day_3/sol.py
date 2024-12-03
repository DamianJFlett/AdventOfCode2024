import re
f = open("input.txt", "r")
text = ""
for l in f:
    text += l
i = 0
total = 0 
muls = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', text)
enabled = True
for mul in muls:
    if mul == "do()":
        enabled = True
        continue
    if mul == "don't()":
        enabled = False
        continue
    if enabled: # commend this and unindent for part 1
        t1, t2 = mul.split(",")
        x, y = int(t1.split("(")[1]), int(t2.split(")")[0])
        total += x*y
print(total)