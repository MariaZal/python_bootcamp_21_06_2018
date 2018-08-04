def add_matrices(a, b,):

    matrix = []
    i = 0

    for row in a:
        j = 0
        new_row = []
        for col in row:
            new_row.append(col + b[i][j])
            j+=1
        i+=1
        matrix.append(new_row)

    print(matrix)
    return matrix






def sub_matrices(a,b):
    matrix = []
    i = 0

    for row in a:
        j = 0
        new_row = []
        for col in row:
            new_row.append(col - b[i][j])
            j += 1
        i += 1
        matrix.append(new_row)

    print(matrix)
    return matrix


x = [[1, 2, 3], [1, 2, 3]]
y = [[2, 3, 4], [2, 3, 4]]

print()
add_matrices(x, y)
sub_matrices(x, y)