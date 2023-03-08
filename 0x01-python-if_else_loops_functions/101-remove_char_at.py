#!/usr/bin/python3
def remove_char_at(string, n):
    """
    Returns a copy of the string with the character at index n removed.
    """
    if n < 0 or n >= len(string):
        return string
    else:
        return string[:n] + string[n+1:]
