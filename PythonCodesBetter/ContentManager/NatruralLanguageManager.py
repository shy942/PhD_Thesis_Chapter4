
import os
from Utility.ReadFile import read_file_topN, read_file
from ContentManager.ProgrammingElementManager import PE_Processor, collectorProgrammingElement

# folder where all projects source codes are contained
source_codes_root = "../ExampleProjectData/SourceCodes/Project3/"

# Function to collect source code content if the source code is in file_content_list
def collect_code_content(file_content_list, converted_relative_path, file_path):
    content = ''
    for file in file_content_list:
        
        check=0;
        extention_length=file_extension_check(file)
        if(file == converted_relative_path and extention_length <= 3 and check<=0):
            #print('found')
            #print(file, converted_relative_path)
            content = read_file(file_path)
            #Apply PE_Process
            collectorProgrammingElement(content)
            check = 1
    return content

def file_extension_check(fileName):
    name, extention = os.path.splitext(fileName)
    #print(len(extention))
    return len(extention)

# collect Top-N (N=10) source documents from a software project
def collect_source_document_contents(directory, file_content_list):
    #print(directory)
    print(file_content_list)
 
    content = ''
    for root, dirs, files in os.walk(directory):
    
        # filter out hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if not file.startswith('.'): # filter out hidden files
                if not file.endswith('.exe'): 
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, os.path.join(directory, "."))
                    # Replace backslashes with dots
                    converted_relative_path = relative_path.replace("\\", ".")
                    #print(converted_relative_path)

                    #Collect source code content if the source code is in file_content_list
                    content = content + '\n' + collect_code_content(file_content_list, converted_relative_path, file_path)
                    
    return content
#return source_documents

def collect_content(file_content_list):
    #print(file_content_list)
    print(source_codes_root)
    source_code_content=collect_source_document_contents(source_codes_root, file_content_list)
    return source_code_content

#Parameters are bugID, preprocessed bug report conetnt, result path
def NL_Processor(bug_report_id, text, result_file_path):
    # Collect contents from the top-10 source codes
    file_content_list=[]
    file_content_list=read_file_topN(result_file_path, bug_report_id, 10)
    source_codes_content=collect_content(file_content_list)
    #Apply PE_Process
    result = PE_Processor(source_codes_content)
    return result
if __name__ == "__main__":
    NL_Processor('2295','','./ExampleProjectData/Results/3_search_results_no_stem.txt')