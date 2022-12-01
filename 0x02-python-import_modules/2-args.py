#!/usr/bin/python3
import sys


def main():
    lt = len(sys.argv) - 1

    if lt < 1:
        print("0 arguments.")
    else:
        print("1 argument:") if lt == 1 else print("{} arguments:".format(lt))
        for index, value in enumerate(sys.argv[1:], 1):
            print("{}: {}".format(index, value))


if __name__ == "__main__":
    main()
