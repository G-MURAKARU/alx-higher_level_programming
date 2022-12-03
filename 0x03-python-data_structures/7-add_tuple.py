#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    sum1, sum2 = 0, 0

    for index in range(2):
        my_sum = 0
        try:
            my_sum += tuple_a[index]
        except IndexError:
            pass

        try:
            my_sum += tuple_b[index]
        except IndexError:
            pass

        if index == 0:
            sum1 = my_sum
            continue
        sum2 = my_sum

    return (sum1, sum2)
