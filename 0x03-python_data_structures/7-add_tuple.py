#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):
    a = list(tuple_a)
    b = list(tuple_b)

    if len(a) > 2:
        a = a[:2]
    else:
        while len(a) < 2:
            a.append(0)
    if len(b) > 2:
        b = b[:2]
    else:
        while len(b) < 2:
            b.append(0)

    sum1 = a[0] + b[0]
    sum2 = a[1] + b[1]

    return (sum1, sum2)

if __name__ == "__main__":
    add_tuple(tuple_a=(), tuple_b=())
