#!/usr/bin/python3
i = 0
while i < 8:
    j = i + 1
    while j < 10:
        if i == j:
            j += 1
            continue
        print("{}{}".format(i, j), end=", ")
        j += 1
    i += 1
print("{}".format(89))
