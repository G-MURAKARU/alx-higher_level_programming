#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main():
    a = 10
    b = 5
    calc = {'+': add, '-': sub, '*': mul, '/': div}

    for sign, func in calc.items():
        print("{} {} {} = {}".format(a, sign, b, func(a, b)))


if __name__ == "__main__":
    main()
