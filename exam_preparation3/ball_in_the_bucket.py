matrix_area = []
total_points = 0

for row in range(6):
    row_elements = input().split()
    matrix_area.append(row_elements)

for i in range(3):
    command = input()

    if len(command) == 6:
        row = int(command[1])
        col = int(command[4])

        hit = matrix_area[row][col]
        if hit == "B":
            for rows in range(6):
                if matrix_area[rows][col] != "B":
                    total_points += int(matrix_area[rows][col])
            matrix_area[row][col] = "0"
        elif hit != "B":
            if 0 <= row <= 5 and 0 <= col <= 5:
                total_points += int(matrix_area[row][col])
    else:
        continue

if 100 <= total_points <= 199:
    prize = "Football"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
elif 200 <= total_points <= 299:
    prize = "Teddy Bear"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
elif 300 <= total_points:
    prize = "Lego Construction Set"
    print(f"Good job! You scored {total_points} points, and you've won {prize}.")
else:
    print(f"Sorry! You need {100 - total_points} points more to win a prize.")
