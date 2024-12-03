import re
f = open("input.txt", "r")
text = ""
for l in f:
    text += l
i = 0
total = 0 
muls = re.findall(r'mul\(\d+,\d+\)', text)
for mul in muls:
    t1, t2 = mul.split(",")
    x, y = int(t1.split("(")[1]), int(t2.split(")")[0])
    total += x*y
print(total)