def main(N):
    matrix = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if (i + j) < (N - 1):
                matrix[i][j] = 1
            elif (i + j) > (N - 1):
                matrix[i][j] = -1
            else:
                matrix[i][j] = 0
    return matrix


def printMatrix(matrix):
    for row in matrix:
        print(str(row) + '\n')

printMatrix(main(5))
