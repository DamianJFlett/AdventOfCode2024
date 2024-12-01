f = open("input.txt", "r")
l1 = []
l2 = []
distance = 0
sim = 0
counts = {}
for l in f:
    nums = l.split(maxsplit = 1)
    l1.append(int(nums[0]))
    l2.append(int(nums[1][:-1]))
l1.sort()
l2.sort()
for i in range(len(l1)):
    if not counts.get(l2[i]):
        counts[l2[i]] = 1
    else:
        counts[l2[i]] += 1
    distance += abs(l1[i]-l2[i])
#find similarity
for i in l1:
    if counts.get(i):
        sim += i * counts[i]
print("distance is ", distance)
print("similarity is ", sim)