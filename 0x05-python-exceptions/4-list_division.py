#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    index = 0
    results = []

    while list_length > 0:
        try:
            result = my_list_1[index] / my_list_2[index]
        except ZeroDivisionError:
            print("division by 0")
            result = 0
        except ValueError:
            print("wrong type")
            result = 0
        except TypeError:
            print("wrong type")
            result = 0
        except IndexError:
            print("out of range")
            result = 0
        finally:
            results.append(result)
            index += 1
            list_length -= 1

    return results
