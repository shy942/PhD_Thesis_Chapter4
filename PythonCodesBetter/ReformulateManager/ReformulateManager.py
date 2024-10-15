import os
from Utility.ReadFile import read_file
from Utility.Preprocessor import preprocess_text
from ContentManager.ContentManager import contentCheck
from ContentManager.ContentProcessor import process_PE, process_NL
from Utility.Preprocessor import marge_content

description_type=''
image_typr=''


def reformulateBasedOnType(type_description, type_image_content, raw_description, image_content, bug_report_id, result_file_path):
    process_content = []
    preprocessed_description_QR = []
    processed_image_content_QR = []
    if 'NL' in type_description and 'NL' in type_image_content:
        print('Both are NL types so process only once ')
        preprocessed_description_QR = [] 
        processed_image_content_QR = process_NL(bug_report_id, result_file_path)
    elif 'NL' in type_description and 'PE' in type_image_content:
        preprocessed_description_QR = process_NL (bug_report_id, result_file_path) 
        processed_image_content_QR = process_PE(image_content)
    elif 'PE' in type_description and 'NL' in type_image_content:
        preprocessed_description_QR = process_PE (raw_description) 
        processed_image_content_QR = process_NL(bug_report_id,result_file_path)
    elif 'PE' in type_description and 'PE' in type_image_content:
        preprocessed_description_QR = process_PE (raw_description) 
        processed_image_content_QR = process_PE(image_content)

    return preprocessed_description_QR, processed_image_content_QR

def title_manager(title_path):
    preprocessed_title = []
    title = read_file(title_path)
    #print(title)
    print('Pre-procesed Title ------------------------------------------------------')
    preprocessed_title=preprocess_text(title)
    #print(type(preprocessed_title))
    return preprocessed_title
    
def type_check_description_image(raw_descrption, image_content_all):
    type_Description=contentCheck(raw_descrption)
    type_image_content=contentCheck(image_content_all)
    return type_Description, type_image_content

def get_image_content(bug_report_path):
    image_content_all = '';
    files = sorted(os.listdir(bug_report_path))
    for file_name in files:
        if "ImageContent.txt" in file_name:
            file_path = os.path.join(bug_report_path, file_name)
            file_content = read_file(file_path)
            image_content_all += file_content + "\n"
    return image_content_all;

def get_description_content(description_path):
    raw_descrption= read_file(description_path)
    return raw_descrption

def reformulate_bug_report_content(bug_report_path, bug_report_id, baseline_result_file_path):
    #print('.............................................................................................................',bug_report_path)
    # gather bug report title and description
    title_path = os.path.join(bug_report_path, 'title.txt')
    preprocessed_title= []
    preprocessed_title=title_manager(title_path)
    print('preprocessed title type: ', (preprocessed_title))
    description_path = os.path.join(bug_report_path, 'description.txt')
    raw_description='';
    raw_description=get_description_content(description_path)
    #print(raw_description)
    image_content_all = '';
    image_content_all=get_image_content(bug_report_path)
    #print(image_content_all)
    type_description, type_image=type_check_description_image(raw_description, image_content_all)
    print('Description type: ',type_description)
    print('Image Content type: ',type_image)
    process_content = []
    preprocessed_description_QR,  processed_image_content_QR= reformulateBasedOnType(type_description, type_image, raw_description, image_content_all, bug_report_id, baseline_result_file_path)
    print('preprocessed_description_QR: ',preprocessed_description_QR)
    print('processed_image_content_QR: ',processed_image_content_QR)
    #print(type(preprocessed_title))
    #print(type(preprocessed_description_QR))

    print('Merged content')
    #print(marge_content(preprocessed_title, preprocessed_description_QR, processed_image_content_QR))
    Reformulated_merged_query=[]
    Reformulated_merged_query=marge_content(preprocessed_title, preprocessed_description_QR, processed_image_content_QR)
    print(Reformulated_merged_query)
    return Reformulated_merged_query