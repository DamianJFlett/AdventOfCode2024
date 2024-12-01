f = open("input.txt", "r")
l1 = []
l2 = []
total = 0
for l in f:
    nums = l.split(maxsplit = 1)
    l1.append(int(nums[0]))
    l2.append(int(nums[1][:-1]))
l1.sort()
l2.sort()
for i in range(len(l1)):
    total += abs(l1[i]-l2[i])
print(total)