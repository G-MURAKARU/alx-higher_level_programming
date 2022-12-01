#!/usr/bin/python3
import sys


l = len(sys.argv) - 1

if l < 1:
    print("0 arguments.")
else:
    print("1 argument:") if l == 1 else print("{} arguments:".format(l))
    for index, value in enumerate(sys.argv[1:], 1):
        print("{}: {}".format(index, value))
