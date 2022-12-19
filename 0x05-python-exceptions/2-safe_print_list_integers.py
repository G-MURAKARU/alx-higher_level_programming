#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    index, printed = 0, 0

    while x > 0:
        try:
            print("{:d}".format(my_list[index]), end="")
            printed += 1
        except ValueError:
            pass
        except TypeError:
            pass
        finally:
            index += 1
            x -= 1

    print()
    return printed
