#!/usr/bin/env python3
"""
write_to_file.py
GNU GPLv3 License
Shows how to write data to text files in Python.
"""

def write_text_to_file(filename, content):
    """
    Write text content to the specified file (overwrites if exists).

    Args:
        filename (str): Target file name or path.
        content (str): Text to write.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    return True

if __name__ == "__main__":
    write_text_to_file("example1.txt", "Hello, world! Python file handling example.")
    print("File written successfully.")
