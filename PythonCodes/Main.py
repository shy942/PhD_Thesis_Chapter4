
import os
from ReadFile import read_file
from Preprocessor import preprocess_text
from ContentTypeChecker import contentCheck
from ContentProcessor import process_PE, process_NL

# folder where all projects containing bug reports are stored
project_bug_reports_root = "./ExampleProjectData/ProjectBugReports/"

def checkType(Text):
    print('Check Type')

def processContentforQR(text, type):
    final_content = []
    if 'PE' in type:
        print(type)
        final_content=process_PE(text)
    elif 'NL' in type:
        final_content = process_NL(text)
    return final_content

def mainManager(projects_root):
    #Get the project ids
    projects = [name for name in os.listdir(projects_root) if name.isdigit()]
    projects.sort(key=int)
    # iterate through projects
    for project in projects:
        project_path = os.path.join(projects_root, project)
        
        bug_reports = [name for name in os.listdir(project_path) if name.isdigit()]
        bug_reports.sort(key=int)
        print(bug_reports)
        # iterate through bug reports
        for bug_report in bug_reports:
            bug_report_path = os.path.join(project_path, bug_report)
            print('.............................................................................................................',bug_report_path)
            collectType(bug_report_path)

def collectType(bug_report_path):
    print('.............................................................................................................',bug_report_path)
     # gather bug report title and description
    title_path = os.path.join(bug_report_path, 'title.txt')
    description_path = os.path.join(bug_report_path, 'description.txt')
    title = read_file(title_path)
    #print(title)
    print('Pre-procesed Title ------------------------------------------------------')
    preprocessed_title=preprocess_text(title)
    print(preprocessed_title)
    description = read_file(description_path)
    #print(description)
      #processed_description
    processed_description=preprocess_text(description)
    #print(processed_description)
    #Check the Type of Description ST,PE or NL
    typeCheck=contentCheck(description)
    print('Type of description is: ', typeCheck)
    #processed_description
    preprocessed_description_QR = []
    preprocessed_description_QR = processContentforQR(description, typeCheck)
    print(preprocessed_description_QR)
    
    #Image Content
    image_content_all = '';
    files = sorted(os.listdir(bug_report_path))
    for file_name in files:
        if "ImageContent.txt" in file_name:
            file_path = os.path.join(bug_report_path, file_name)
            file_content = read_file(file_path)
            #print(file_content)
            image_content_all += file_content + "\n"
    #print(image_content_all)
    #Check the Type of Image-Conent-all ST,PE or NL
    typeCheck=contentCheck(image_content_all)
    print('Type of Image Contents: ', typeCheck)
    processed_image_content=preprocess_text(image_content_all)
    print(processed_image_content)
    #processed_image_content
    processed_image_content_QR = []
    processed_image_content_QR = processContentforQR(image_content_all, typeCheck)
    
    print('\n',type(preprocessed_title))
    print(type(preprocessed_description_QR))
    print(type(processed_image_content_QR))
    reformulated_query=preprocessed_title+preprocessed_description_QR.split()+processed_image_content_QR.split();
    #print('reformulated_query')
    #print(reformulated_query)

if __name__ == "__main__":
    mainManager(project_bug_reports_root)