#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    lt = len(sys.argv)

    if lt != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    calc = {"+": add, "-": sub, "*": mul, "/": div}
    a, operator, b = sys.argv[1:]
    a, b = int(a), int(b)

    for sign, func in calc.items():
        if sign == operator:
            print("{} {} {} = {}".format(a, operator, b, func(a, b)))
            break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)


if __name__ == "__main__":
    main()
