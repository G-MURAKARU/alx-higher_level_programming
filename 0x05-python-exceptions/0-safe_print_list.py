#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    index = 0
    while x > 0:
        try:
            print(my_list[index], end="")
            index += 1
            x -= 1
            continue
        except IndexError as e:
            break
    print()
    return index
