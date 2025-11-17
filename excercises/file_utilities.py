#!/usr/bin/env python3
"""
file_utilities.py
GNU GPLv3 License
Provides helper utilities for file operations.
"""

import os

def file_exists(filename):
    """Check if a file exists in the current directory."""
    return os.path.exists(filename)

def get_file_size(filename):
    """Return file size in bytes, or 0 if file doesn't exist."""
    return os.path.getsize(filename) if os.path.exists(filename) else 0

def delete_file(filename):
    """Delete a file if it exists."""
    if os.path.exists(filename):
        os.remove(filename)
        return True
    return False
