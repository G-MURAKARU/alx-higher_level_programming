#!/usr/bin/python3
def roman_to_int(roman_string):
    symbols = {'I': 1,
               'V': 5,
               'X': 10,
               'L': 50,
               'C': 100,
               'D': 500,
               'M': 1000}

    roman_list = list(roman_string)

    counter = 0
    arabic = 0

    while counter < len(roman_list):
        first = symbols[roman_list[counter]]
        try:
            second = symbols[roman_list[counter+1]]
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
