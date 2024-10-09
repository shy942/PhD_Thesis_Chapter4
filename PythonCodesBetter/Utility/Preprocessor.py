import sys
import os
import regex
import ast
from nltk.stem import PorterStemmer
from nltk import download
download('punkt')


# read the stopwords
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file)
    

# Function to preprocess text
def preprocess_text(text):
    stopwords = load_stopwords("stop_words_english.txt")
    # split camelCase and snake_case while keeping acronyms
    text = regex.sub(r'([a-z0-9])([A-Z])', r'\1 \2', text)
    text = regex.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)
    text = text.replace('_', ' ')

    # remove urls and the markdown link
    text = regex.sub(r'\!\[.*?\]\(https?://\S+?\)', '', text)
    text = regex.sub(r'https?://\S+|www\.\S+', '', text)
    text = regex.sub(r"[\s]+|[^\w\s]|[\d]+", " ", text)

    # convert to lowercase and split for list comprehensions
    tokens = text.lower().split()

    # Remove stopwords
    tokens = [token for token in tokens if token not in stopwords]

    # remove words with fewer than 3 characters
    tokens = [word for word in tokens if len(word) >= 3]
    
    print('Type of tokens inside Preprocessor.py')
    print(tokens)
    print(type(tokens))

    return tokens


def marge_content(list1, list2, list3):
    #merged_list=[]
    # Remove duplicates while preserving order
    unique_list = []
    seen = set()
    for item in list1:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    
    
    for item in list2:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    
    
    for item in list3:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    
    return unique_list

