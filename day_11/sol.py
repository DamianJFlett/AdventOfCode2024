from bit_vector import BitVector # tried this bitvector approach using my comp3506 assignment, doesn't work for a couple reasons lol. defaultdict is better
from collections import defaultdict
f = open("input.txt", "r")
nums = [41078, 18, 7, 0, 4785508, 535256, 8154, 447]

def blink_line(nums):
    l = []
    for i in nums:
        l+= blink_stone(i)
    return l

def blink_stone(num):
    if num == 0:
        return [1]
    elif not (len(str(num)) % 2):
        return [int(str(num)[:len(str(num))// 2 ]), int(str(num)[len(str(num)) // 2:])]
    else:
        return [num * 2024]
    

x = nums
for i in range(25):
    x = blink_line(x)
print("part 1 solution is ", len(x))

counts = defaultdict(int)
for i in nums:
    counts[i] += 1
# dp kinda?
for i in range(75):
    updated_counts = defaultdict(int)
    for num in counts:
        if num == 0:
            updated_counts[1] += counts[num]
        elif not (len(str(num)) % 2):
            updated_counts[int(str(num)[:len(str(num))// 2 ])] += counts[num]
            updated_counts[int(str(num)[len(str(num)) // 2:])] += counts[num]
        else:
            updated_counts[num*2024] = counts[num]
    counts = updated_counts
total2 = 0
for i in counts.values():
    total2 += i
print("part 2 soln is ", total2)

