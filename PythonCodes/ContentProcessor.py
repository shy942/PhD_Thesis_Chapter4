from ProgrammingElementManager import PE_Processor

def process_ST():
    print('Process Stack Trace')

def process_PE(text):
    print('Process Programming Element')
    PE_Processor(text)


def process_NL():
    print('Process Natural Language Text')

def main_processor(type):
    print('Main from ContentProcessor')