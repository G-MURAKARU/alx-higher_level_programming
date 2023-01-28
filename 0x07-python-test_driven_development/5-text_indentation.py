#!/usr/bin/python3

"""
    this is the ```5-text_indentation``` module.
    this module provides one function, text_indentation(text: str)
"""


def text_indentation(text: str) -> None:
    """
    text_indentation prints text with two new lines after each '.', '?'
    and ':'.

    Args:
        text (str): the text to print
    """

    def validate_text() -> None:
        """
        validate_text validates that input [text] is a string

        Raises:
            TypeError: if input is not a string
        """

        if not isinstance(text, str):
            raise TypeError("text must be a string")

    validate_text()

    char_index: int = 0
    len_text: int = len(text)

    # avoid leading whitespaces
    while char_index < len_text and text[char_index] == " ":
        char_index += 1

    while char_index < len_text:
        print(text[char_index], end="")
        if text[char_index] in [".", "?", ":", "\n"]:
            if text[char_index] in ".?:":
                print("\n")
            char_index += 1
            while char_index < len_text and text[char_index] == " ":
                char_index += 1
            continue
        char_index += 1
