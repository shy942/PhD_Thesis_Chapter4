import sys
import os
import regex
import ast
from nltk.stem import PorterStemmer
from nltk import download
download('punkt')


def preprocess_text(text, use_stemming):
    stopwords = load_stopwords("stop_words_english.txt")
    # initialize stemmer if needed
    stemmer = PorterStemmer() if use_stemming else None

    # remove urls and the markdown link
    text = regex.sub(r'\!\[.*?\]\(https?://\S+?\)', '', text)
    text = regex.sub(r'https?://\S+|www\.\S+', '', text)
    
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
    if use_stemming:
        words = [stemmer.stem(word) for word in words]
        
        # remove any words that became a stop word after stemming
        words = [word for word in words if word not in stopwords]
    
    # remove words with fewer than 3 characters
    words = [word for word in words if len(word) >= 3]
    
    return ' '.join(words)


# read the stopwords
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return set(word.strip() for word in file)



