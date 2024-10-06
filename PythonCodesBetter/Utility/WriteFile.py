import os
# Write file with encoding 'utf-8' or iso-8859-1
def write_file(file_path, ReformulatedQuery, encoding='utf-8'):
    try:
        with open(file_path, 'w', encoding=encoding) as file:
            return file.write(ReformulatedQuery)
    except UnicodeDecodeError:
        # Try a different encoding if UTF-8 fails
        with open(file_path, 'w', encoding='iso-8859-1') as file:
            return file.write(ReformulatedQuery)