#!/usr/bin/python3
"""
    A module that contains the text_indentation function
"""


def text_indentation(text):
    """
        A function that prints a text with 2 new lines
        after each of . ? : charachters

        Args:
            text (string): The text the indent

        Raises:
            TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    text = text.replace('.', '.\n\n')
    text = text.replace(':', ':\n\n')
    text = text.replace('?', '?\n\n')
    text = text.split("\n\n")
    stripped_text = [line.strip() for line in text]
    for line in stripped_text:
        if line == stripped_text[len(stripped_text) - 1]:
            print(line.replace('\n', ''), end="")
            break
        print(line + "\n\n", end="")
