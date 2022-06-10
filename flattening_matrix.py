n = int(input())

matrix = []

for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)

flattened = [x for row in matrix for x in row]

print(flattened)