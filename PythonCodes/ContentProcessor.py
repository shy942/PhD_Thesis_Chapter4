from ProgrammingElementManager import PE_Processor
from NatruralLanguageManager import NL_Processor

def process_ST():
    print('Process Stack Trace')

def process_PE(text):
    print('Process Programming Element')
    result=PE_Processor(text)
    return result


def process_NL(text):
    print('Process Natural Language Text')
    result=NL_Processor(text)
    return result

def main_processor(type):
    print('Main from ContentProcessor')