import re
from numpy.linalg import solve
f = open("input.txt", "r")
A = []
B = []
prizes = []


def get_coords_prize(s):
    match = re.search(r"X=(\d+), Y=(\d+)", s)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        return num1, num2

def get_coords_button(s):
    match = re.search(r"X\+(\d+), Y\+(\d+)", s)
    if match:
        num1 = int(match.group(1))
        num2 = int(match.group(2))
        return num1, num2


for l in f:
    if "A" in l:
        A.append(get_coords_button(l))
    elif "Button B" in l:
        B.append(get_coords_button(l))
    elif "P" in l:
        prizes.append(get_coords_prize(l))

print(A, B, prizes)

def scalar_mul(scalar, vector: tuple[int, int]):
    return (scalar * vector[0], scalar * vector[1])

total = 0
#so basically we're solving a linear system!
for (index, prize) in enumerate(prizes):
    A1, A2 = A[index]
    B1, B2 = B[index]
    #want: x*bB+y*bA = prize
    sol = solve([[A1, B1], [A2, B2]], [prize[0], prize[1]])
    print(prize, A1, A2, B1, B2, sol)
    if abs(sol[0]-round(sol[0])) <= 0.001 and abs(sol[1]-round(sol[1])) <= 0.001:
        total += (round(sol[0])*3 + round(sol[1]))
print("part oen solution is ", total)


#part 2
total = 0
#so basically we're solving a linear system!
for (index, prize) in enumerate(prizes):
    A1, A2 = A[index]
    B1, B2 = B[index]
    #want: x*bB+y*bA = prize
    sol = solve([[A1, B1], [A2, B2]], [prize[0]+10000000000000, prize[1]+10000000000000])
    print(prize, A1, A2, B1, B2, sol)
    if abs(sol[0]-round(sol[0])) <= 0.001 and abs(sol[1]-round(sol[1])) <= 0.001:
        total += (round(sol[0])*3 + round(sol[1]))
print("part two solution is ", total)

