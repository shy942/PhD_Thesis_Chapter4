
import os
from ReadFile import read_file
from Preprocessor import preprocess_text
from ContentTypeChecker import contentCheck

# folder where all projects containing bug reports are stored
project_bug_reports_root = "./ExampleProjectData/ProjectBugReports/"

def checkType(Text):
    print('Check Type')

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
            print(bug_report_path)
            collectType(bug_report_path)

def collectType(bug_report_path):
     # gather bug report title and description
    title_path = os.path.join(bug_report_path, 'title.txt')
    description_path = os.path.join(bug_report_path, 'description.txt')
    title = read_file(title_path)
    #print(title)
    print('Pre-procesed Title ------------------------------------------------------')
    preprocessed_title=preprocess_text(title, False)
    print(preprocessed_title)
    description = read_file(description_path)
    #Check the Type of Description ST,PE or NL
    type=contentCheck(description)
    print('Type of description is: ', type)
    #print(description)
    
    #Image Content
    image_content_all = '';
    files = sorted(os.listdir(bug_report_path))
    for file_name in files:
        if "ImageContent.txt" in file_name:
            file_path = os.path.join(bug_report_path, file_name)
            file_content = read_file(file_path)
            image_content_all += file_content + "\n"
    #print(image_content_all)
    #Check the Type of Image-Conent-all ST,PE or NL
    type=contentCheck(image_content_all)
    print('Type of Image Contents: ', type)

if __name__ == "__main__":
    mainManager(project_bug_reports_root)