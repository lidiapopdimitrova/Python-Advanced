def get_matrix():
    matrix = []
    for _ in range(8):
        matrix.append(input().split())
    return matrix


def find_player_position(matrix, player):
    for (row_index, row) in enumerate(matrix):
        if player in row:
            return row_index, row.index(player)

    return None, None


def matrix_mapping(row, col):
    rows = [8, 7, 6, 5, 4, 3, 2, 1]
    cols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return f"{cols[col]}{rows[row]}"


matrix = get_matrix()
current_player = "w"
other_player = "b"
current_player_position = find_player_position(matrix, "w")
other_player_position = find_player_position(matrix, "b")
current_delta = -1
other_delta = +1

is_capture = False
is_queen = False

while not is_queen and not is_capture:
    (current_player_row, current_player_column) = current_player_position
    (other_player_row, other_player_column) = other_player_position
    # next row =
    current_player_row += current_delta
    current_player_position = (current_player_row, current_player_column)
    if current_player_row == other_player_row and abs(current_player_column - other_player_column) == 1:
        current_player_row, current_player_column = current_player_row, other_player_column
        is_capture = True

        # capture at...
    elif current_player_row in (0, 8 - 1):
        # queen at (next_row, current_player_column)
        is_queen = True
    else:
        current_player_position, other_player_position = other_player_position, current_player_position
        current_delta, other_delta = other_delta, current_delta
        current_player, other_player = other_player, current_player


if is_queen:
    if current_player == 'w':
        player = 'White'
    else:
        player = 'Black'
    print(f"Game over! {player} pawn is promoted to a queen at "
          f"{matrix_mapping(current_player_row, current_player_column)}.")

if is_capture:
    if current_player == 'w':
        player = 'White'
    else:
        player = 'Black'
    print(f"Game over! {player} win, capture on "
          f"{matrix_mapping(current_player_row, current_player_column)}.")


