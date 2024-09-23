import re
import os
from ReadFile import read_file
def contentCheck(text):
    #Checking for Stack Trace (i.e., ST)
    print('Checking for stack trace')
    type=StackTraceChecker(text)
    #Checking for Programming Element (i.e., PE)
    type=ProgrammingElementChecker(text)
    return type


def StackTraceChecker(text):
    # The regular expression pattern provided
    pattern = r'^\s*(?:at\s+)?([\w$.]+)\(([\w.]+\.:\d+|Unknown Source|Native Method)\)$'

    # Compile the regular expression for better performance if using multiple times
    compiled_pattern = re.compile(pattern, re.MULTILINE)
    #print(compiled_pattern)
    # Find all matches in the text
    matches = compiled_pattern.findall(text)
    #print(text)
    print('==================================')
    count_of_non_empty_matches = 0
    # Print the matches
    for match in matches:
        #print(f"Matched pattern: {match}")
        non_empty_matches = [m for m in match if m]
        if non_empty_matches:
            count_of_non_empty_matches += 1
            result = non_empty_matches[0]  # extract the relevant matched pattern
            #print(f"Matched pattern: {result}")
            print(count_of_non_empty_matches)


def ProgrammingElementChecker(text):
    # The regular expression pattern provided
    pattern = r'((\w+)?\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))|([A-Z][a-z0-9]+){2,}'
    # Compile the regular expression for better performance if using multiple times
    compiled_pattern = re.compile(pattern)

    # Find all matches in the text
    matches = compiled_pattern.findall(text)
    #print(matches)
    #print(len(matches))
    result=''
    if len(matches)>0:
        result='PE'
    else:
        result='Not PE'
    print(result)
    return result

if __name__ == "__main__":
    file_path='C:/Users/mukta/OneDrive/Documents/PhD/Study-4/QueryReformulation/Projects/Test/'
    file_path_all=os.path.join(file_path, 'STTest.txt')
    text=read_file(file_path_all)
    print(text)
    StackTraceChecker(text)
    #print(tokens)
    # Example text simulating Java stack trace entries
    text = """
    at com.example.MyClass.method
    at com.example.AnotherClass.otherMethod
    at com.example.SomeClass.nativeMethod
    """
    StackTraceChecker(text)