rower_row, rower_col = 0, 0

size = 6
matrix_area = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "E":
            rower_row, rower_col = row, col

    matrix_area.append(row_elements)

directions = input().split(', ')


def move_rover(direction, row, col):
    if direction == "left":
        return row, col - 1
    if direction == "right":
        return row, col + 1
    if direction == "up":
        return row - 1, col
    if direction == "down":
        return row + 1, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


def reposition_rover(row, col, size):
    if row < 0:
        return size + row, col
    if row >= size:
        return row - size, col
    if col < 0:
        return row, size + col
    if col >= size:
        return row, col - size


water_found = False
metal_found = False
concrete_found = False

for direction in directions:
    rower_row, rower_col = move_rover(direction, rower_row, rower_col)
    if is_outside(rower_row, rower_col, size):
        rower_row, rower_col = reposition_rover(rower_row, rower_col, size)

    cell_value = matrix_area[rower_row][rower_col]

    if cell_value == "W":
        water_found = True
        print(f"Water deposit found at ({rower_row}, {rower_col})")
    elif cell_value == 'C':
        concrete_found = True
        print(f"Concrete deposit found at ({rower_row}, {rower_col})")
    elif cell_value == "M":
        metal_found = True
        print(f"Metal deposit found at ({rower_row}, {rower_col})")

    elif cell_value == "R":
        print(f"Rover got broken at ({rower_row}, {rower_col})")
        break

if water_found and metal_found and concrete_found:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")


# - R - - - -
# - - - - - R
# - E - R - -
# - W - - - -
# - - - C - -
# M - - - - -
# down, right, down, right, down, left, left, left