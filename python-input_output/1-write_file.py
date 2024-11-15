#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads the contents of a UTF-8 encoded text file and prints it to stdout.

    Args:
        filename (str): The name of the file to read. Defaults to an empty string.

    If the file does not exist or is empty, no output is printed.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(file.read(), end="")
    except FileNotFoundError:
        pass  # If the file doesn't exist, do nothing
    except IOError:
        pass  # Handles other I/O errors (e.g., permission issues), although not required to handle in this case

