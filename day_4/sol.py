import re
f = open("input.txt", "r")
# method - create matrices to search through with a regex, these should be the matrix originally
# rotated 45 degrees (so that something like [[1,2], [3,4]] would be [[1]. [2,3], [4]]) and the transpose
# to search every direction. Storage inefficient but the search is sufficiently small. 
ws = []
for l in f:
    ws.append(l[:-1])
ws_transpose = [""] * len(ws[0])
for (lindex, l) in enumerate(ws):
    for (cindex, c) in enumerate(l):
        ws_transpose[cindex] = ws_transpose[cindex] + c

# to construct these, lets notice something about this diagonal matrix in n dimensions - 
# nth row has all the a_ij s.t. i+j=n+1. Easy here since matrix is square. To see this, notice that moving along a diagonal 
# subtracts 1 from the row and adds 1 to the column. 

#note - I'm sure there's a way to do this that directly accessess the necessary matrix elements, maybe come back and do it!
ws_diagonal = [""] * (2*len(ws)-1)
for n in range(2 * len(ws) - 1):  #rows of diagonal
    for i in range(len(ws)):  # rows of original
        for j in range(len(ws[0])):  # columns of original
            if i + j == n: 
                ws_diagonal[n] += str(ws[i][j]) 


ws_diagonal2 = [""] * (2 * len(ws) - 1)
for n in range(2 * len(ws) - 1):  # rows of diagonal
    for i in range(len(ws)):  # rows of original
        for j in range(len(ws[0])):  # columns of original
            if j - i == n - (len(ws) - 1):  #this check is different for the other diagonal
                ws_diagonal2[n] += str(ws[i][j])

total_xmas = 0
for row in ws:
    total_xmas += len(re.findall(r'XMAS', row))
    total_xmas += len(re.findall(r'SAMX', row))
for row in ws_transpose:
    total_xmas += len(re.findall(r'XMAS', row))
    total_xmas += len(re.findall(r'SAMX', row))
for row in ws_diagonal:
    total_xmas += len(re.findall(r'XMAS', row))
    total_xmas += len(re.findall(r'SAMX', row))
for row in ws_diagonal2:
    total_xmas += len(re.findall(r'XMAS', row))
    total_xmas += len(re.findall(r'SAMX', row))
print("part 1 soln is ", total_xmas)

#part 2


# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 
# THROW ALL OF THIS IN THE BIN WE OUT EHRE DOING BRUTE FORCE 




# """ 
# """ #reference to chatgpt for this one, struggled a lot with this method. 
# # https://chatgpt.com/share/6750e381-ff90-8005-a328-fd82817264d3
# def rotated_to_unrotated(n, k, num_rows, num_cols):
#     """
#     Converts diagonal coordinates (n, k) from the rotated matrix representation
#     back to the original matrix coordinates (i, j).

#     Parameters:
#     - n: Index of the diagonal in the rotated representation.
#     - k: Position along the diagonal (0-indexed).
#     - num_rows: Number of rows in the original matrix.
#     - num_cols: Number of columns in the original matrix.

#     Returns:
#     - (i, j): Coordinates in the original unrotated matrix.
#     """
#     # Find the first valid row index for diagonal n
#     first_i = max(0, n - (num_cols - 1))  # Start of the diagonal within row bounds
#     i = first_i + k  # Move k steps along the diagonal
    
#     # Compute column index
#     j = n - i
    
#     # Validate indices
#     if 0 <= i < num_rows and 0 <= j < num_cols:
#         return i, j
#     return None  # Return None if out of bounds

# #method - search for mas, retrive original coordinates in ws with logic 
# # since first element of rows of diagonal matrix is first element of columns of ws
# # then search directly for ms at antidiagonals of a and add if theyre there
# total_x_mas = 0

# for (index, row) in enumerate(ws_diagonal):
#     masses = re.finditer(r'MAS|SAM', row)
#     for match in masses:
#         Ax, Ay = rotated_to_unrotated(index, match.start() + 1, len(ws), len(ws))
#         if (ws[Ax+1][Ay+1] == "S" and ws[Ax-1][Ay-1] == "M") or (ws[Ax-1][Ay-1] == "S" and ws[Ax+1][Ay+1] == "M"):
#             total_x_mas += 1



# print("part 2 soln is ", total_x_mas) """ """

total_x_mas = 0
for (x, row) in enumerate(ws):
    for (y, c) in enumerate(row):
        if 1 <= x <= len(ws)-2 and 1 <= y <= len(ws) - 2:          
            if c == "A" and ws[x-1][y-1] == "M" and ws[x-1][y+1] == "M" and ws[x+1][y-1] == "S" and ws[x+1][y+1] == "S":
                total_x_mas += 1
            elif c == "A" and ws[x-1][y-1] == "M" and ws[x-1][y+1] == "S" and ws[x+1][y-1] == "M" and ws[x+1][y+1] == "S":
                total_x_mas += 1 
            elif c == "A" and ws[x-1][y-1] == "S" and ws[x-1][y+1] == "M" and ws[x+1][y-1] == "S" and ws[x+1][y+1] == "M":
                total_x_mas += 1 
            elif c == "A" and ws[x-1][y-1] == "S" and ws[x-1][y+1] == "S" and ws[x+1][y-1] == "M" and ws[x+1][y+1] == "M":
                total_x_mas += 1 
print(total_x_mas)