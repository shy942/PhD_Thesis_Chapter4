# This function sorts the PageRank scores
def sortPageRankScore (node_to_index, pagerank_score, topN):
    print ('I am from sorPageRankScore function')
    node_to_index_2D_array = list (node_to_index.items())
    pagerank_score_merged=[]
    for i in range(0, len(node_to_index), 1):
        #print('i',i , '', node_to_index_2D_array[i][0])
        pagerank_score_merged.append((node_to_index_2D_array[i][0], pagerank_score[i]))

    # Sort the pagerank score
    sorted_pagerank_score_merged = sorted (pagerank_score_merged, key= lambda x: x[1], reverse = True)
    #print(sorted_pagerank_score_merged)
    
    sorted_result=[] #This list will contain the tokens only
    # print top-N results
    if(len(sorted_pagerank_score_merged)<topN):
        for i in range(0, len(sorted_pagerank_score_merged), 1):
            #print(sorted_pagerank_score_merged[i][0], end = ' ')
            sorted_result.append(sorted_pagerank_score_merged[i][0])
    else:
        for i in range(0, topN , 1):
            #print(sorted_pagerank_score_merged[i][0], end = ' ')
            sorted_result.append(sorted_pagerank_score_merged[i][0])
    return sorted_result
