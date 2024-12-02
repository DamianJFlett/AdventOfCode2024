
def check_valid(nums):
    i = 0
    inc = True if nums[0] < nums[1] else False
    safe = True

    while i < len(nums)-1:
        if inc and  -3 <= nums[i] - nums[i+1] < 0:
            i += 1
        elif not inc and 0 < nums[i] - nums[i+1] <= 3:
            i += 1
        else:
            safe = False
            break
    return (safe, i)

f = open("input.txt", "r")

safe_total = 0


# historians are calling this the hackiest solution ever
for l in f:
    nums = [int(i) for i in l.split(" ")]
    x = check_valid(nums)
    a = nums.copy()
    a.pop(x[1])
    y = check_valid(a)

    z = [False]
    if x[1] - 1 >=  0:
        b = nums.copy()
        b.pop(x[1]-1)
        z = check_valid(b)
    
    w = [False]
    if x[1] + 1 < len(nums):
        c = nums.copy()
        c.pop(x[1]+1)
        w = check_valid(c)

    safe = x[0] or y[0] or z[0] or w[0]
    safe_total += safe
print(safe_total)
