#!/usr/bin/env python3
"""
append_to_file.py
GNU GPLv3 License
Shows how to append text to an existing file.
"""

def append_text_to_file(filename, content):
    """
    Append text content to an existing file (creates a new one if needed).

    Args:
        filename (str)
        content (str)
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(content + "\n")
    return True

if __name__ == "__main__":
    append_text_to_file("example1.txt", "New line appended!")
    print("Content appended successfully.")
