#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return 0

    symbols = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

    counter = 0
    arabic = 0

    while counter < len(roman_string):
        first = symbols[roman_string[counter]]
        try:
            second = symbols[roman_string[counter+1]]
            if second > first:
                second -= first
                arabic += second
                increment = 2
                continue
            arabic += first
            increment = 1
        except IndexError:
            arabic += first
            increment = 1
        finally:
            counter += increment

    return arabic
