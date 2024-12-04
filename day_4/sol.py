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


#method - search for mas, retrive original coordinates in ws with logic 
# since first element of rows of diagonal matrix is first element of columns of ws
# then search directly for ms at antidiagonals of a and add if theyre there
total_x_mas = 0
for (index, row) in enumerate(ws_diagonal):
    masses = re.finditer(r'MAS', row)
    for match in masses:
        x, y = match.start(), match.start()
def diagonal_to_coordinates(diagonal_matrix, original_shape):
    """
    Generate a mapping from diagonal matrix indices to original matrix coordinates.
    
    Args:
        diagonal_matrix: A list of lists, representing the diagonals of the original matrix.
        original_shape: A tuple (rows, cols) representing the dimensions of the original matrix.

    Returns:
        A dictionary where keys are (d_idx, elem_idx) indices in the diagonal matrix, 
        and values are (row, col) coordinates in the original matrix.
    """
    mapping = {}
    rows, cols = original_shape

    for d_idx, diagonal in enumerate(diagonal_matrix):
        for elem_idx, value in enumerate(diagonal):
            # Recover the original matrix coordinates
            # Diagonal index (d_idx) is the sum of row and column indices (i + j)
            # Column index is `elem_idx`
            row = elem_idx
            col = d_idx - row
            # Ensure indices are valid for the original matrix dimensions
            mapping[(d_idx, elem_idx)] = (row, col)

    return mapping

# Example usage
diagonal_matrix = [[1], [4,2], [7,5,3],[8,6],[9]]  # Diagonal representation
original_shape = (3,3)  # Shape of the original matrix

coordinate_mapping = diagonal_to_coordinates(diagonal_matrix, original_shape)
print(coordinate_mapping)