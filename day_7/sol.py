f = open("input.txt", "r")
results = []
nums = []
calib = 0
calib_2 = 0
for l in f:
    x = l.split(":")
    results.append(int(x[0]))
    nums.append([int(k) for k in x[1][:-1].split(" ")[1:]])

def reachable(nums, goal):
    reachable = {0}
    for (idx, k) in enumerate(nums):
        reachable_k = set()
        for result in reachable:
                if (k+result == goal or k * result == goal) and idx == len(nums)-1:
                    return True
                else:
                    reachable_k.add(k+result)
                    reachable_k.add(k*result)
        reachable = reachable_k
    return False
 
def reachable_with_concat(nums, goal):
    reachable = {0}
    for (idx, k) in enumerate(nums):
        reachable_k = set()
        for result in reachable:
                if ((k+result == goal) or (k * result == goal) or (int(str(result) + str(k)) == goal)) and idx == len(nums)-1:
                    return True
                else:
                    reachable_k.add(k+result)
                    reachable_k.add(k*result)
                    reachable_k.add(int(str(result) + str(k)))
        reachable = reachable_k
    return False

for (index, l) in enumerate(nums):
    if reachable(l, results[index]):
        calib += results[index]
print("part 1 result is ", calib)

for (index, l) in enumerate(nums):
    if reachable_with_concat(l, results[index]):
        calib_2 += results[index]
print("part 2 result is ", calib_2)
print("highest possible total is ", sum(results))