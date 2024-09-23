
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
    type=contentCheck(description)
    print('Description type is: ', type)
    #print(description)
    #Process Title
     
    #Check the Type of Description

    #Process Accordingly
    #ST
    #PE
    #NL

    #Check the Type of Image Content (s)

    #Process Accordingly
    #ST
    #PE
    #NL
    print('Main Manager')


if __name__ == "__main__":
    mainManager(project_bug_reports_root)