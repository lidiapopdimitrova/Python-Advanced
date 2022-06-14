rows, cols = [int(x) for x in input(). split()]
# we are searching for the maximal sum in a 3x3 square in a matrix
maximal_sum = 0
start_row = 0
start_col = 0
matrix = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])

for row_index in range(rows - 2):
    for col_index in range(cols - 2):
        current_sum = matrix[row_index][col_index] + matrix[row_index][col_index + 1] +\
                      matrix[row_index][col_index + 2] + \
                      matrix[row_index + 1][col_index] + matrix[row_index + 1][col_index + 1] + \
                      matrix[row_index + 1][col_index + 2] + matrix[row_index + 2][col_index] + \
                      matrix[row_index + 2][col_index + 1] + matrix[row_index + 2][col_index + 2]
        if current_sum > maximal_sum:
            start_row = row_index
            start_col = col_index
            maximal_sum = current_sum


print(f"Sum = {maximal_sum}")
print(f"{matrix[start_row][start_col]} {matrix[start_row][start_col + 1]} {matrix[start_row][start_col + 2]}")
print(f"{matrix[start_row + 1][start_col]} {matrix[start_row + 1][start_col + 1]} {matrix[start_row + 1][start_col+2]}")
print(f"{matrix[start_row + 2][start_col]} {matrix[start_row + 2][start_col + 1]} {matrix[start_row + 2][start_col+2]}")

