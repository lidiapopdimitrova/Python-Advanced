def sum_column(m, column):
    res = 0
    for row in m:
        if row[column] == "B" or row[column] == "В":
            continue
        res += row[column]
    return res


size_matrix = 6

prizes = {
    "Football": [100, 199],
    "Teddy Bear": [200, 299],
    "Lego Construction Set": [300, 1000]
}

matrix = []
points = 0
buckets = {}

for r in range(size_matrix):
    field = input().split()
    for c in range(size_matrix):
        if field[c] == "B" or field[c] == "В":
            buckets_col = c
            buckets[buckets_col] = [r, c]
        else:
            field[c] = int(field[c])
    matrix.append(field)

for throw in range(3):
    raw_throw = input()
    current_throw = list(map(int, raw_throw.replace("(", "").replace(")", "").split(", ")))
    a = 5

    if current_throw[0] < 0 or current_throw[0] >= size_matrix \
            or current_throw[1] < 0 or current_throw[1] >= size_matrix \
            or matrix[current_throw[0]][current_throw[1]] != "B":
        continue

    else:
        row, col = current_throw[0], current_throw[1]
        if col in buckets:
            result = sum_column(matrix, col)
            points += result
            del buckets[col]

if points < 100:
    print(f"Sorry! You need {abs(100 - points)} points more to win a prize.")
else:
    for name, points_range in prizes.items():
        if points_range[0] <= points <= points_range[1]:
            print(f"Good job! You scored {points} points, and you've won {name}.")
            break