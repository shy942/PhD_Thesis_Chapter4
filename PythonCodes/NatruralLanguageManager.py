
import os
from ReadFile import read_file_list, read_file
# folder where all projects source codes are contained
source_codes_root = "./ExampleProjectData/SourceCodes/Project3/"

def collect_code_content(file_content_list, converted_relative_path, file_path):
    content = ''
    for file in file_content_list:
        #print(file, converted_relative_path)
        if(file == converted_relative_path):
            print('found')
            print(file, converted_relative_path)
            content = read_file(file_path)
            #print(content)
    return content

# collect all source documents from a software project
def find_source_documents(directory, file_content_list):
    #print(directory)
    print(file_content_list)
    source_documents = []
    base_directory = os.path.basename(os.path.normpath(directory))
    count = 0
    content = ''
    for root, dirs, files in os.walk(directory):
    
        # filter out hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if not file.startswith('.'): # filter out hidden files
                
                    file_path = os.path.join(root, file)
                    relative_path = os.path.relpath(file_path, os.path.join(directory, "."))
                    # Replace backslashes with dots
                    converted_relative_path = relative_path.replace("\\", ".")
                    #print(converted_relative_path)
                    count += 1
                    content = content + '\n' + collect_code_content(file_content_list, converted_relative_path, file_path)
                    
    #print(len(source_documents)) 
    print("------------------------------------------------------------------------------------------------------")      
    print(content)  
#return source_documents

def collect_content(file_content_list):
    #print(file_content_list)
    print(source_codes_root)
    find_source_documents(source_codes_root, file_content_list)

#Parameters are bugID, preprocessed bug report conetnt, result path
def NL_Processor(bugID, text, result_file_path):
    #Collect top-10 results
    file_content_list=[]
    file_content_list=read_file_list(result_file_path,bugID)
    print(type(file_content_list))
    
    #for file in file_content_list:
        #print(file)
    collect_content(file_content_list)
    # Collect contents from the top-10 source codes

    #Apply PE_Process

if __name__ == "__main__":
    NL_Processor('2295','','./ExampleProjectData/Results/3_search_results_no_stem.txt')