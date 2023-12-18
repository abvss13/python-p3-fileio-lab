# lib/file_io.py

def write_file(file_name, file_content):
    """
    Write the given content to a file.

    Args:
    - file_name (str): The name of the file (without extension).
    - file_content (str): The content to write to the file.
    """
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Append the given content to an existing file.

    Args:
    - file_name (str): The name of the file (without extension).
    - append_content (str): The content to append to the file.
    """
    with open(f"{file_name}.txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    """
    Read the content of a file.

    Args:
    - file_name (str): The name of the file (without extension).

    Returns:
    - str: The content of the file.
    """
    with open(f"{file_name}.txt", "r") as file:
        return file.read()
