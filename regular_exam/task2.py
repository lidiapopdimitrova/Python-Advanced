current_player, other_player = input().split(", ")


def is_a_trap(row, col, matrix):
    if matrix[row][col] == "T":
        return True


matrix = []
for row in range(6):
    row_elements = input().split()
    matrix.append(row_elements)

    for col in range(6):
        if row_elements[col] == "E":
            exit_row, exit_col = row, col


def is_a_wall(row, col, matrix):
    if matrix[row][col] == "W":
        return True


tom_resting = False
jerry_resting = False
raw_coordinates = input()
while True:

    current_position = list(map(int, raw_coordinates.replace("(", "").replace(")", "").split(", ")))

    if tom_resting and jerry_resting:
        tom_resting = False
        jerry_resting = False
        other_player, current_player = current_player, other_player

    elif current_player == "Tom" and tom_resting:
        other_player, current_player = current_player, other_player
        tom_resting = False

    elif current_player == "Jerry" and jerry_resting:
        other_player, current_player = current_player, other_player
        jerry_resting = False

    else:
        if current_position[0] == exit_row and current_position[1] == exit_col:
            print(f"{current_player} found the Exit and wins the game!")
            break
        elif is_a_trap(current_position[0], current_position[1], matrix):
            other_player, current_player = current_player, other_player
            print(f"{current_player} is out of the game! The winner is {other_player}.")
            break

        elif is_a_wall(current_position[0], current_position[1], matrix):
            print(f"{current_player} hits a wall and needs to rest.")
            if current_player == "Tom":
                tom_resting = True
            else:
                jerry_resting = True

        else:
            if current_player == "Tom":
                jerry_resting = False
            else:
                tom_resting = False

    other_player, current_player = current_player, other_player

    raw_coordinates = input()





