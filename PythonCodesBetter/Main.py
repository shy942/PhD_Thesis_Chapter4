import os
from ReformulateManager.ReformulateManager import reformulate_bug_report_content

# folder where all projects containing bug reports are stored
project_bug_reports_root = "../ExampleProjectData/ProjectBugReports/"
project_root="../ExampleProjectData/"


def mainManager(project_root, project_bug_reports_root, baseline_result_file_path):
    #Get the project ids
    projects = [name for name in os.listdir(project_bug_reports_root) if name.isdigit()]
    projects.sort(key=int)
    # iterate through projects
    for project in projects:
        project_path = os.path.join(project_bug_reports_root, project)
        
        bug_reports = [name for name in os.listdir(project_path) if name.isdigit()]
        bug_reports.sort(key=int)
        print(bug_reports)
        # iterate through bug reports
        for bug_report in bug_reports:
            bug_report_path = os.path.join(project_path, bug_report)
            print('.............................................................................................................',bug_report_path)
            bug_report_id=bug_report
            Reformulated_query=[]
            Reformulated_query=reformulate_bug_report_content(bug_report_path, bug_report_id, baseline_result_file_path)
    
if __name__ == "__main__":
    print('I am from Main.py')
    baseline_result_file_path = '../ExampleProjectData/BaseLineResults/3_search_results_no_stem.txt'
    mainManager(project_root, project_bug_reports_root, baseline_result_file_path)