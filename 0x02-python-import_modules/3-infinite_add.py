#!/usr/bin/python3
import sys


def main():
    arg_sum = 0
    args = map(int, sys.argv[1:])
    for num in args:
        arg_sum += num
    print(arg_sum)


if __name__ == "__main__":
    main()
