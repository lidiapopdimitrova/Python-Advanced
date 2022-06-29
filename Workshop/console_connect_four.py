def get_initial_field(rows_count, columns_count):
    return [[None] * columns_count for _ in range(rows_count)]


def get_cell_value(cell):
    return cell if cell else 0


def print_field(field):
    [print([get_cell_value(x) for x in row]) for row in field]


def print_winner(player):
    print(f"Player {player} wins!")


def get_player_move(player):

    player_move_str = input(f"Player {player}, please choose a column ")
    player_move = int(player_move_str)

    return player_move - 1


def apply_player_move_gen(max_row, columns_count):
    free_bottom_row_indices = [max_row - 1] * columns_count

    def apply_player_move_internal(player, player_move, field):
        player_row = free_bottom_row_indices[player_move]
        field[player_row][player_move] = player
        free_bottom_row_indices[player_move] -= 1

    return apply_player_move_internal


def is_win_condition(player, player_row, player_column, field):

    def normalize_player_position_in_direction(field, row, column, direction):
        row_delta, column_delta = direction
        rows_boundary = min(len(field - 1), row + 4 * row_delta)
        columns_boundary = min(len(field[0]), column + 4 * column_delta)

    def is_win_condition_in_direction(field, row, column, direction):
        row_delta, column_delta = direction
        rows_boundary = min(len(field - 1), row + 4 * row_delta)
        columns_boundary = min(len(field[0]), column + 4 * column_delta)
        counter = 0
        is_row_included = rows_boundary == row
        is_column_included = columns_boundary == column
        while (row != rows_boundary or is_row_included) and (column != columns_boundary or is_column_included) and \
                player == field[row][column]:
            counter += 1
            row += row_delta
            column += column_delta

        return counter == 4
    directions = [(0, 1),  # horizontal
                  (1, 0),  # vertical
                  (1, 1),  # main diagonal
                  (-1, 1)  # secondary diagonal
    ]
    return any(is_win_condition_in_direction((field, player_row, player_column, direction) for direction in directions))


def play(field):
    rows_count = len(field)
    columns_count = len(field[0])
    apply_player_move = apply_player_move_gen(rows_count, columns_count)
    player_one = 1
    player_two = 2

    while True:
        player_move = get_player_move(player_one)
        apply_player_move(player_one, player_move, field)
        if is_win_condition(field):

            break
        else:
            player_one, player_two = player_two, player_one
        print_field(field)
    print_winner(player_one)


field = get_initial_field(6, 7)
play(field)
# print(
#     True,
#     is_win_condition(
#         [
#             [0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0]
#             [0, 0, 0, 0, 0, 0, 0]
#         ]
#     )
# )