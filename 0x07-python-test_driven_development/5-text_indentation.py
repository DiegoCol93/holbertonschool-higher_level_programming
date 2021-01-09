#!/usr/bin/python3
""" Module: for text manipulation. """


def text_indentation(text):
    """ Prints with indentation the given text removing extra spaces.

        Args:
            text (str): The given text.

        Raises:
            TypeError: if not a str.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    letter = 0
    text = text.strip(' ')

    while letter < len(text):

        print(text[letter], end='')

        if text[letter] in (".", "?", ":"):

            if (letter + 1) < len(text):
                while text[letter + 1] == ' ':
                    letter += 1

            print("\n")

        letter += 1
