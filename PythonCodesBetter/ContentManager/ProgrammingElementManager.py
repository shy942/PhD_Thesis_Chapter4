import re
import numpy as np
from Utility.Preprocessor import preprocess_text, preprocess_text_by_single_string
from Utility.PageRankScoreSorting import sortPageRankScore
from CoOccuranceManager.MatrixAndGraphManager import build_cooccurrence_matrix, createnpMatrixFromTextGraph
from CoOccuranceManager.TextGraphManager import create_graph_my_code
from PageRankManager.PageRank import pagerank

def collectorProgrammingElement(text):
    #print('from collectorProgrammingElement: ', text)
    # The regular expression pattern provided
    pattern = r'((\w+)?\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))|([A-Z][a-z0-9]+){2,}'
    #pattern = r'((\w+)?\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))|([A-Z][a-z0-9]+)'
    
    # Compile the regular expression for better performance if using multiple times
    compiled_pattern = re.compile(pattern)

    # Find all matches in the text
    matches = compiled_pattern.findall(text, re.VERBOSE)
    #print(matches)
    result_all=""
    # Print the matches
    for match in matches:
        print(match)
        # The match result is a tuple due to the grouping in the regex; filter for non-empty elements
        non_empty_matches = [m for m in match if m]
        if non_empty_matches:
            result = non_empty_matches[0]  # extract the relevant matched pattern
            #print(result)
            result_all = result_all + " " + result
    return result_all


def collectorProgrammingElement_group(text):
    #print('from collectorProgrammingElement: ', text)
    # The regular expression pattern provided
    pattern = r'((\w+)?\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))|([A-Z][a-z0-9]+){2,}'
    #pattern = r'((\w+)?\.[\s\n\r]*[\w]+)[\s\n\r]*(?=\(.*\))|([A-Z][a-z0-9]+)'
    
    # Compile the regular expression for better performance if using multiple times
    compiled_pattern = re.compile(pattern)

    # Find all matches in the text
    #matches = compiled_pattern.findall(text, re.VERBOSE)
    matches = re.finditer(pattern, text, re.MULTILINE)
    #print(matches)
    result_all=""
    # Print the matches
    for matchNum, match in enumerate(matches, start=1):
    
        #print("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
        result_all = result_all + ' '+match.group()
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
        
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    #print (result_all)
    #tokens = preprocess_text(result_all)
    #print (tokens)
    return result_all

def PE_Processor(text):
    # Programming element collection
    print('I am from ProgrammingElementManager.py')
    #print(type(text))
    result=[]
    result_all = collectorProgrammingElement_group(text)
    #print(result_all)
    
    # Pre-process the text (stop-word removal stemming etc)
    # tokens = preprocess_text(result_all)
    tokens = preprocess_text_by_single_string(result_all)
    print(tokens)
    
    #Create co-occurence matrix
    calls = build_cooccurrence_matrix(tokens)
    #print(len(calls))
    #for i in range(len(calls)-1):
        #print(calls[i])
    
    # create_graph(cooccurrence_matrix)
    G = create_graph_my_code(calls)
    #print(G.nodes)
   
    # convert text grpah into a matrix
    co_matrix, node_to_index  = createnpMatrixFromTextGraph (G)
    #print('co_matrix', co_matrix)
    #print('node to index', node_to_index) 

    #Call PageRank
    num_nodes=len(G.nodes)
    pagerank_score = pagerank(np.array(co_matrix), num_nodes)
    #print(pagerank_score)
    # Sort pagerank score
    result = sortPageRankScore (node_to_index, pagerank_score, 20)
    print(result)
    return result