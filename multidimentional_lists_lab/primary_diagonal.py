def get_primary_diagonal(matrix):
    the_sum = 0
    n = len(matrix)
    for r in range(n):
        the_sum += matrix[r][r]
    return the_sum


num = int(input())
matrix1 = []

for _ in range(num):
    matrix1.append([int(x) for x in input().split()])

print(get_primary_diagonal(matrix1))
