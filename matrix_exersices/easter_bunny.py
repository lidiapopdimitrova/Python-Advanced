import sys

size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0

for row in range(size):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(size):
        if row_elements[col] == "B":
            bunny_row, bunny_col = row, col

directions = {'right': lambda r, c: (r, c + 1),
              'left': lambda r, c: (r, c - 1),
              'up': lambda r, c: (r - 1, c),
              'down': lambda r, c: (r + 1, c)
              }

best_direction = ''
best_score = -sys.maxsize
best_path = []
for direction, step in directions.items():
    current_row, current_col = bunny_row, bunny_col
    current_score = 0
    path = []

    while True:
        current_row, current_col = step(current_row, current_col)

        if current_row < 0 or current_col < 0 or current_row >= size or current_col >= size:
            break
        if matrix[current_row][current_col] == 'X':
            break
        path.append([current_row, current_col])
        current_score += (int(matrix[current_row][current_col]))

    if current_score >= best_score and path:     # така проверяваме дали сме минали през
        best_score = current_score
        best_direction = direction
        best_path = path


print(best_direction)
for path in best_path:
    print(path)
print(best_score)

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0