import os
from Utility.ReadFile import read_file
from Utility.Preprocessor import preprocess_text
from ContentManager.ContentManager import contentCheck
from ContentManager.ContentProcessor import process_PE, process_NL

def processContentforQR(text, type, bug_report_id, result_file_path):
    process_content = []
    if 'PE' in type:
        print(type)
        process_content = process_PE(text)
    elif 'NL' in type:
        process_content = process_NL(bug_report_id, text, result_file_path)
    return process_content


def title_manager(title_path):
    title = read_file(title_path)
    #print(title)
    print('Pre-procesed Title ------------------------------------------------------')
    preprocessed_title=preprocess_text(title)
    print(preprocessed_title)

def description_manager(description_path, bug_report_id, baseline_result_file_path):
    raw_descrption= read_file(description_path)
    #print('Raw Description ----------------------------------------------------------')
    #print(raw_descrption)
    typeCheck=contentCheck(raw_descrption)
    print('Type of description is: ', typeCheck)
    #processed_description
    preprocessed_description_QR = []
    preprocessed_description_QR = processContentforQR(raw_descrption, typeCheck, bug_report_id, baseline_result_file_path)
    print(preprocessed_description_QR)
    

def image_content_manger(bug_report_path, bug_report_id, baseline_result_file_path):
    image_content_all = '';
    files = sorted(os.listdir(bug_report_path))
    for file_name in files:
        if "ImageContent.txt" in file_name:
            file_path = os.path.join(bug_report_path, file_name)
            file_content = read_file(file_path)
            image_content_all += file_content + "\n"
    #Check the Type of Image-Conent-all ST,PE or NL
    typeCheck=contentCheck(image_content_all)
    print('Type of Image Contents: ', typeCheck)
    processed_image_content_QR = []
    processed_image_content_QR = processContentforQR(image_content_all, typeCheck, bug_report_id, baseline_result_file_path)
    print(processed_image_content_QR)
    

def reformulate_bug_report_content(bug_report_path, bug_report_id, baseline_result_file_path):

    print('.............................................................................................................',bug_report_path)
    # gather bug report title and description
    title_path = os.path.join(bug_report_path, 'title.txt')
    title_manager(title_path)
    description_path = os.path.join(bug_report_path, 'description.txt')
    description_manager(description_path, bug_report_id, baseline_result_file_path)
    image_content_manger(bug_report_path,bug_report_id, baseline_result_file_path)
    
    
   
    """"reformulated_query=preprocessed_title+preprocessed_description_QR+processed_image_content_QR;
    print('reformulated_query')
    print(reformulated_query)
    print('Merged content')
    #print(marge_content(preprocessed_title, preprocessed_description_QR, processed_image_content_QR))
    Reformulated_merged_query=[]
    Reformulated_merged_query=marge_content(preprocessed_title, preprocessed_description_QR, processed_image_content_QR)
    print(Reformulated_merged_query)
    return Reformulated_merged_query"""