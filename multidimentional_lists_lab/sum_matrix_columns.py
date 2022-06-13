rows, columns = [int(x) for x in input().split(', ')]
matrix = []

for row_index in range(rows):
    new_list = [int(x) for x in input().split()]
    matrix.append(new_list)

column_sum = [0] * columns

for row_index in range(rows):

    for column_index in range(columns):
        column_sum[column_index] += matrix[row_index][column_index]

[print(x) for x in column_sum]

