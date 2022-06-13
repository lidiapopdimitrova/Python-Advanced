def read_matrix():
    lines, columns = [int(x) for x in input().split(', ')]
    matrix = []
    matrix_sum = 0
    for _ in range(lines):
        row = [int(x) for x in input().split(', ')]
        matrix_sum += sum(row)
        matrix.append(row)
    print(matrix_sum)
    return matrix

    
final_matrix = read_matrix()
print(final_matrix)