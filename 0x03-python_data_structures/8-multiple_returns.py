#!/usr/bin/python3


def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        return 0, None
    return length, sentence[0]


if __name__ == "__main__":
    multiple_returns()
