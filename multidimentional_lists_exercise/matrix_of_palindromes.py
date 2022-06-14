import string

rows, cols = [int(x) for x in input().split()]
matrix = []
for row_index in range(rows):
    matrix.append([])
    for col_index in range(cols):
        matrix[row_index].append(string.ascii_lowercase[row_index] + string.ascii_lowercase[row_index + col_index] +
                                 string.ascii_lowercase[row_index])

for i in range(rows):
    print(' '.join(x for x in matrix[i]))