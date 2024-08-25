import os

def list_directory_contents():
    """
    Lists the contents of the current working directory.

    Returns:
        list: A list of files and directories in the current working directory.

    Example:
        >>> list_directory_contents()
        ['file1.txt', 'file2.txt', 'dir1', 'dir2']
    """
    return os.listdir()

print(list_directory_contents())

import time

def sleep(seconds):
    """
    Pauses the execution of the program for a specified number of seconds.

    Args:
        seconds (int): The number of seconds to sleep.

    Returns:
        None

    Example:
        >>> sleep(2)
        # program pauses for 2 seconds
    """
    time.sleep(seconds)

sleep(2)

def find_whitespace(string):
    """
    Finds the index of the first occurrence of a whitespace character in a string.

    Args:
        string (str): The string to search for whitespace.

    Returns:
        int: The index of the first whitespace character, or -1 if not found.

    Example:
        >>> find_whitespace("Hello  World!")
        6
    """
    return string.find("  ")

name = "Hello  World!"
print(find_whitespace(name))

def replace_whitespace(string):
    """
    Replaces all occurrences of whitespace characters in a string with a single space.

    Args:
        string (str): The string to replace whitespace in.

    Returns:
        str: The modified string with single spaces.

    Example:
        >>> replace_whitespace("Hello  World!")
        'Hello World!'
    """
    return string.replace("  ", " ")

print(replace_whitespace(name))