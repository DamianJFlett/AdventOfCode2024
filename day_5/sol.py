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

for order in orders:
    valid = True
    for (index, num) in enumerate(order):
        for i in range(index):
            if order[i] in relations[num]:
                valid = False
    if valid: 
        total_valid += get_middle_element(order)
print("Part one solution is", total_valid)
