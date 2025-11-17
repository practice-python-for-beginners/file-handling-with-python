#!/usr/bin/env python3
"""
read_from_file.py
GNU GPLv3 License
Demonstrates reading data from text files.
"""

def read_text_from_file(filename):
    """
    Read all text from the specified file.

    Args:
        filename (str): File to read.

    Returns:
        str: File content as a string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def read_lines_from_file(filename):
    """
    Read all lines from a file into a list.

    Args:
        filename (str)

    Returns:
        list[str]: Each line as an item in the list.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]

if __name__ == "__main__":
    text = read_text_from_file("example1.txt")
    print("File content:")
    print(text)
