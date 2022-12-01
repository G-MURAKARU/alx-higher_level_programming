#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    funcs = [add, sub, mul, div]
    signs = ['+', '-', '*', '/']

    for func, sign in zip(funcs, signs):
        print("{} {} {} = {}".format(a, sign, b, func(a, b)))


if __name__ == "__main__":
    main()
