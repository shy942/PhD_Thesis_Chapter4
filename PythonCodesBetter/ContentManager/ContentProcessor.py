from ContentManager.ProgrammingElementManager import PE_Processor
from ContentManager.NatruralLanguageManager import NL_Processor

def process_ST():
    print('Process Stack Trace')

def process_PE(text):
    result=[]
    print('Let us process Programming Element')
    result=PE_Processor(text)
    return result


def process_NL(bug_report_id, result_file_path):
    result=[]
    print('Process Natural Language Text')
    result=NL_Processor(bug_report_id, result_file_path)
    return result

def main_processor(type):
    print('Main from ContentProcessor')