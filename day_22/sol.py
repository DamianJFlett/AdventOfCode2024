con = 2 ** 24 - 1
f = open("input.txt", "r")
nums = []
for l in f:
    nums.append(int(l[:-1]))

def prune(num):
    return num & con

def mix(num1, num2):
    return num1 ^ num2

def evolve(num, times):
    for i in range(times):
        num = mix(num << 6, num)
        num = prune(num)
        num = mix(num >> 5, num)
        num = prune(num)
        num = mix(num << 11, num)
        num = prune(num)
    return num

print(sum(evolve(num, 2000) for num in nums))

#part 2