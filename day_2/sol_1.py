f = open("input.txt", "r")
safe_total = 0

for l in f:
    nums = [int(i) for i in l.split(" ")]
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
    safe_total += safe
print(safe_total)