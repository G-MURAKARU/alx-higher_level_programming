#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lt = len(row)
        if lt == 0:
            print()
            continue
        for element in range(lt):
            end = " " if element < (lt - 1) else "\n"
            print("{}".format(row[element]), end=end)


if __name__ == "__main__":
    print_matrix_integer(matrix=[[]])
