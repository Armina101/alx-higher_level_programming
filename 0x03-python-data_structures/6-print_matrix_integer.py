#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for b in range(len(matrix[i])):
            if b != 0:
                print(' {:d}'.format(matrix[a][b]), end='')
            else:
                print('{:d}'.format(matrix[a][b]), end='')
        print()