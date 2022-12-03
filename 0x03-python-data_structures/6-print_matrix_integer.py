#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lt = len(row)
        if lt == 0:
            print()
            continue
        for element in range(lt):
            end = " " if element < (lt - 1) else "\n"
            print("{:d}".format(row[element]), end=end)
    return
