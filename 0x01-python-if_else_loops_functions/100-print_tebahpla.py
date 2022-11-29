#!/usr/bin/python3
char = 90
for i in range(26):
    if i % 2 == 0:
        print_char = chr(char + 32)
    else:
        print_char = chr(char)
    print("{}".format(print_char), end="")
    char -= 1
