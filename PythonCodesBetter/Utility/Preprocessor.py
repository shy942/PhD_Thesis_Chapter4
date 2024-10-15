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

def preprocess_text_by_single_string(text):
    stopwords = load_stopwords("stop_words_english.txt")
    text = text.split()
    final_text = ''
    for str in text:
        oldStr=str
        #print(oldStr)
        # remove urls and the markdown link
        str = regex.sub(r'\!\[.*?\]\(https?://\S+?\)', '', str) 
        str = regex.sub(r'https?://\S+|www\.\S+', '', str) 
        # split camelCase and snake_case while keeping acronyms
        str = regex.sub(r'([a-z0-9])([A-Z])', r'\1 \2', str)
        str = regex.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', str)
        str = str.replace('_', ' ')
        # convert to lowercase and split for list comprehensions
        words = str.lower()
        words_list=words.split()
        
        # remove stopwords 
        words_list = [word for word in words_list if word not in stopwords]
        #print(words_list)
        
        #Part#1 word itself
        part1=''
        if '.' in oldStr:
            #splitDotWord(str)
            part1=''
        else:
            part1=oldStr.lower()
        #Part#2 the processed words

        part2=''
        for word in words_list:
            newword = ''
            if '.' in word:
                newword =  splitDotWord(word)
            else:
                newword = word   
            part2 = part2 + ' ' + newword  
        #print(type(part1))
        #print(type(part2))
        final_str= part1+ ' ' + part2
        #print (final_str)
        final_text = final_text + ' ' + final_str
    #print(final_text.split())
    return final_text.split()

def splitDotWord(word):
    #print('I am from splitDotWord')
    splitedList = []
    splitedList = word.split('.')
    str2return = ' '
    for eachword in splitedList:
        str2return= str2return + ' ' + eachword
    #print(word.split('.'))
    return str2return

def preprocess_text(text):
    
    stopwords = load_stopwords("stop_words_english.txt")
    # initialize stemmer if needed
    #stemmer = PorterStemmer() if use_stemming else Nonecd 

    # remove urls and the markdown link
    text = regex.sub(r'\!\[.*?\]\(https?://\S+?\)', '', text) 
    text = regex.sub(r'https?://\S+|www\.\S+', '', text) 
    
    # split camelCase and snake_case while keeping acronyms
    #text = regex.sub(r'([a-z0-9])([A-Z])', r'\1', text)
    #text = regex.sub(r'([A-Z]+)([A-Z][a-z])', r'\1', text)
    #text = text.replace('_', ' ')

    # split camelCase and snake_case while keeping acronyms
    text = regex.sub(r'([a-z0-9])([A-Z])', r'\1 \2', text)
    text = regex.sub(r'([A-Z]+)([A-Z][a-z])', r'\1 \2', text)
    text = text.replace('_', ' ')

    # convert to lowercase and split for list comprehensions
    words = text.lower().split()
    
    # remove stopwords 
    words = [word for word in words if word not in stopwords]
    
    # remove whitespace, punctuation, numbers
    text = ' '.join(words)
    text = regex.sub(r"[\s]+|[^\w\s]|[\d]+", " ", text)
    words = text.split()
    
    # remove stopwords again to catch any that were connected to punctuation
    words = [word for word in words if word not in stopwords]
    
    # perform optional stemming
    #if use_stemming:
     #   words = [stemmer.stem(word) for word in words]
        
    # remove any words that became a stop word after stemming
    words = [word for word in words if word not in stopwords]
    
    # remove words with fewer than 3 characters
    words = [word for word in words if len(word) >= 3]
    
    return words
    #return ' '.join(words)

# Function to preprocess text
'''def preprocess_text(text):
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

    return tokens'''


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

