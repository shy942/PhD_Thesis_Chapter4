import re
import os
from Utility.ReadFile import read_file

#Checking for content type
def contentCheck(text):
    #Checking for Stack Trace (i.e., ST)
    #print('Checking for stack trace')
    #type=StackTraceChecker(text)
    #Checking for Programming Element (i.e., PE)
    type=ProgrammingElementChecker(text)
    return type

#Checking for stack trace
def StackTraceChecker(text):
    # The regular expression pattern provided
    #pattern = r'^\s*(?:at\s+)?([\w$.]+)\(([\w.]+\.:\d+|Unknown Source|Native Method)\)$'
    #print(text)
    pattern = r'''
    (?:File\s+"(.+?)",\s+line\s+(\d+),?\s+  # Matches the file and line number
    (?:in\s+(.+?)\s*                        # Matches the function name
    )?\s*                                   # Optional function name
    )?                                       # Make the preceding group optional
    (.+?)\s*                                 # Captures the actual error message
    (?:\n|\Z)                                # Ensures it ends with a newline or end of string
    '''
    pattern = r'''
    ^                                   # Start of the line
    [a-zA-Z0-9_.]+                     # Match the namespace and class (e.g., Microsoft.AspNetCore.Identity.UserClaimsPrincipalFactory<TUser>)
    \<[a-zA-Z0-9_]+\>                   # Match the type parameter (e.g., <TUser>)
    \.                                 # Match the dot before the method name
    [a-zA-Z0-9_]+                       # Match the method name (e.g., GenerateClaimsAsync)
    \(([^)]+)\)                         # Match parameters (e.g., TUser user)
    $                                   # End of the line
    '''

    
    match = re.match(pattern, text, re.VERBOSE)

    if match:
        print("Match found!")
    else:
        print("No match.")
    
    
    
    # Compile the regular expression for better performance if using multiple times
    compiled_pattern = re.compile(pattern, re.VERBOSE)
    #print(compiled_pattern)
    # Find all matches in the text
    matches = compiled_pattern.findall(text)
    #print(text)
    print('==================================')
    count_of_non_empty_matches = 0
    # Print the matches
    for match in matches:
        print(f"Matched pattern: {match}")
        non_empty_matches = [m for m in match if m]
        if non_empty_matches:
            count_of_non_empty_matches += 1
            result = non_empty_matches[0]  # extract the relevant matched pattern
            print(f"Matched pattern: {result}")
            print(count_of_non_empty_matches)


def ProgrammingElementChecker(text):
    # The regular expression pattern provided
    #pattern = r'((\w+)?\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))|([A-Z][a-z0-9]+){2,}'
    #From Masud-BLIZZARD
    pattern = r'((\\w+)?\\.[\\s\\n\\r]*[\\w]+)[\\s\\n\\r]*(?=\\(.*\\))|([A-Z][a-z0-9]+){2,}'
    # Compile the regular expression for better performance if using multiple times
    compiled_pattern = re.compile(pattern)

    # Find all matches in the text
    matches = compiled_pattern.findall(text)
    #print(matches)
    single_match_list=[]
    for match in matches:
        element=match
        if element in single_match_list:
            duplicate = 1
        else:
            single_match_list.append(element)
    #print(len(matches))
    #print('single_match_list', single_match_list)
    result=''
    if len(single_match_list)>5:
        result='PE'
    else:
        result='NL'
    #print(result)
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