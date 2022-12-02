#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def not_found():
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)


def main():
    lt = len(sys.argv)

    if lt != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    calc = {"+": add, "-": sub, "*": mul, "/": div}
    a, operator, b = sys.argv[1:]
    a, b = int(a), int(b)

    result = calc.get(operator, not_found)
    if result == not_found:
        result()
    print("{} {} {} = {}".format(a, operator, b, result(a, b)))


if __name__ == "__main__":
    main()
