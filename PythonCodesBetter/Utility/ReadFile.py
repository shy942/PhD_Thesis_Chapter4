import os
import sys



# Open the file in read mode and find top-10 source codes for a given bug 
def read_file_topN(file_path, bugID, n):
    print('\n')
    print ('Ton-', n, 'files')
    list = []
    count = 0
    found = 0
    with open(file_path, 'r') as file:
    # Iterate over each line in the file
        for line in file:
            # Strip any leading or trailing whitespace from the line
            line = line.strip()
        
            # Split the line by commas
            words = line.split(',')

            if(count == 0 and found == 0):
                # Print the cleaned and split words
                if(len(words)==3 and words[0].isdigit()):
                    if(bugID==words[0] and words[1]=='extended'):
                        #print(words[0])
                        count += 1
                        found = 1
            elif (count > 0 and found == 1 and count <= n):
                # Replace backslashes with dots
                converted_file = words[0].replace("\\", ".")
                list.append(converted_file)
                count += 1
    print(list)
    print('\n')
    return list

# read file with encoding utf-8 or iso-8859-1
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