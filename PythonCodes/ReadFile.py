import os
import sys

# read file with backup encoding if utf-8 fails
def read_file(file_path, encoding='utf-8'):
    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except UnicodeDecodeError:
        # Try a different encoding if UTF-8 fails
        with open(file_path, 'r', encoding='iso-8859-1') as file:
            return file.read()

if __name__ == "__main__":
    read_file()