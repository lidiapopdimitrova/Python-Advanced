def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def next_pos(command, row, col):
    if command == "up":
        return row - 1, col
    elif command == "down":
        return row + 1, col
    elif command == "left":
        return row, col - 1
    elif command == "right":
        return row, col + 1


size = int(input())
matrix = []
tea_bags = 0
alice_row = 0
alice_col = 0

for row in range(size):
    row_el = input().split()
    matrix.append(row_el)
    for col in range(size):
        if row_el[col] == "A":
            alice_row = row
            alice_col = col

while True:
    command = input()
    next_row, next_col = next_pos(command, alice_row, alice_col)
    matrix[alice_row][alice_col] = '*'

    if not is_inside(next_row, next_col, size):
        break
    if matrix[next_row][next_col] == 'R':
        matrix[next_row][next_col] = '*'
        break
    if matrix[next_row][next_col].isnumeric():
        tea_bags += int(matrix[next_row][next_col])

    matrix[next_row][next_col] = '*'
    alice_col, alice_row = next_col, next_row
    if tea_bags >= 10:
        break

if tea_bags >= 10:
    print(f"She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for r in matrix:
    print(*r)

# 7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
