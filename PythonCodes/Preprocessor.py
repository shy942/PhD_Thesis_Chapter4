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

    return tokens


# This function sorts the PageRank scores
def sortPageRankScore (node_to_index, pagerank_score):
    print ('I am from sorPageRankScore function')
    #print (type (node_to_index))
    #print (type (pagerank_score))
    #Conver the dict into 2D array
    node_to_index_2D_array = list (node_to_index.items())
    #print (node_to_index_2D_array)
    pagerank_score_merged=[]
    for i in range(0, len(node_to_index), 1):
        #print('i',i , '', node_to_index_2D_array[i][0])
        pagerank_score_merged.append((node_to_index_2D_array[i][0], pagerank_score[i]))
    #print('new array ', pagerank_score_merged)
    #print(type(pagerank_score_merged))
    # Sort the pagerank score
    sorted_pagerank_score_merged = sorted (pagerank_score_merged, key= lambda x: x[1], reverse = True)
    print(sorted_pagerank_score_merged)
    sorted_result=[]
    # print top-10 results
    if(len(sorted_pagerank_score_merged)<20):
        for i in range(0, len(sorted_pagerank_score_merged), 1):
            print(sorted_pagerank_score_merged[i][0], end = ' ')
            sorted_result.append(sorted_pagerank_score_merged[i][0])
    else:
        for i in range(0, 20 , 1):
            print(sorted_pagerank_score_merged[i][0], end = ' ')
            sorted_result.append(sorted_pagerank_score_merged[i][0])
    return sorted_result



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

