def get_primary_diagonal(matrix1):
    primary_diagonal = []
    for row_index in range(len(matrix1)):
        for column_index in range(len(matrix1)):
            if row_index == column_index:
                primary_diagonal.append(matrix1[row_index][column_index])
    return primary_diagonal


def get_secondary_diagonal(matrix1):
    secondary_diagonal = []
    for row_index in range(len(matrix1)):
        for column_index in range(len(matrix1)):
            if row_index == len(matrix1) - column_index - 1:
                secondary_diagonal.append(matrix1[row_index][column_index])
    return secondary_diagonal


num = int(input())
matrix = []
for _ in range(num):
    element = [int(x) for x in input().split(', ')]
    matrix.append(element)

print(f"Primary diagonal: {', '.join(str(x) for x in get_primary_diagonal(matrix))}. Sum:"
      f" {sum(x for x in get_primary_diagonal(matrix))}")
print(f"Secondary diagonal: {', '.join(str(x) for x in get_secondary_diagonal(matrix))}. Sum:"
      f" {sum(x for x in get_secondary_diagonal(matrix))}")











