f = open("input.txt", "r")


line_num = 0
raw_relations = []
raw_orders = []
relations = {}
orders = []
total_valid = 0
total_invalid =0
for l in f:
    line_num += 1
    if line_num <= 1176:
        raw_relations.append(l[:-1])
    elif line_num == 1177:
        continue
    else:
        raw_orders.append(l[:-1])


for rel in raw_relations:
    relations[int(rel[0:2])] = []
    relations[int(rel[3:5])] = []
for rel in raw_relations:
    relations[int(rel[0:2])].append(int(rel[3:5]))

#list comprehension is gods gift to man
orders = [[int(num) for num in order.split(",")] for order in raw_orders]


def get_middle_element(order):
    return order[len(order) // 2]

"""
Given an unordered list, returns what it would be if correctly ordered
"""
def reorder(order: list[int], rels: dict[int: int]):
    #algorithm - for each element, compare it to each other element. 
    #should this be before it? if so, move it back. Modification is inplace
    # for i in order:
    #     for j in order:
    #         for k in range(100):
    #             if i in rels[j]: #if i supposed to be before j
    #                 order.remove(i)
    #                 order.insert(order.index(j), i)
    # return order
    return bubbleSort(order)

"""
The following function taken from https://www.geeksforgeeks.org/bubble-sort-algorithm/
and modified to use relevant comparator
"""
# Optimized Python program for implementation of Bubble Sort
def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j+1] in relations[arr[j]]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break
    return arr


for order in orders:
    valid = True
    for (index, num) in enumerate(order):
        for i in range(index):
            if order[i] in relations[num]:
                valid = False
    if valid: 
        total_valid += get_middle_element(order)
    else:
        total_invalid += get_middle_element(reorder(order, relations))


print("Part one solution is", total_valid)
print("Part 2 soltution is ", total_invalid)

