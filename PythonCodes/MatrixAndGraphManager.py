import numpy as np
from collections import defaultdict
from itertools import islice


# Function to covert text graph into an adjacency matrix
def createnpMatrixFromTextGraph(G):
    edges_with_strings = G.edges
    # List of unique nodes
    nodes = sorted(list(set(node for edge in G.edges for node in edge)))
    # Define directed edges in the graph
    # Mapping from node name to index
    node_to_index = {node: index for index, node in enumerate(nodes)}

    # Initialize adjacency matrix   
    num_nodes = len(nodes)
    adj_matrix = np.zeros((num_nodes, num_nodes), dtype=int)

    # Populate the adjacency matrix
    for (start, end) in edges_with_strings:
        i, j = node_to_index[start], node_to_index[end]
        adj_matrix[i][j] = 1

    print(type(adj_matrix))
 

    # Output the adjacency matrix
    print("Adjacency Matrix:")
    print(np.array(adj_matrix))
    #print_matrix_with_commas_and_braces(adj_matrix, num_nodes)

    # Optional: Print node mapping to index
    print("\nNode to Index Mapping:")
    print(node_to_index)

    #pagerank_score = pagerank(np.array(adj_matrix), num_nodes)
    #print(pagerank_score)
    return adj_matrix, node_to_index



# Function to build a co-occurrence matrix
def build_cooccurrence_matrix(tokens, window_size=2):
    cooccurrence_matrix = defaultdict(lambda: defaultdict(int))
    calls = []
    #tokens=tokens.split();
    #print(tokens)
    #print(type(tokens))
    for i, token in enumerate(tokens):
        #print(token)
        #print(i)
        ## Get the context window around the current token
        #context = list(islice(tokens, i-window_size, i)) + list(islice(tokens, i+1, i+window_size+1))
        start_index = max(0, i - window_size)
        #print("Start_index", start_index)
        end_index = min(len(tokens), i + window_size + 1)
        #print("End_index", end_index)
        context = list(islice(tokens, start_index, i)) + list(islice(tokens, i + 1, end_index))
        #print(context)

        for context_word in context:
            #cooccurrence_matrix[token][context_word] += 1
            #My version
            if (token!= context_word):
                calls.append((token, context_word))
        
    return calls

if __name__ == "__main__":
    tokens=""
    cooccurrence_matrix = build_cooccurrence_matrix('Your text data goes here. I may be misunderstanding the model here, but preVisit and postVisit seem to be  called incorrectly.')
    #for token, context in cooccurrence_matrix.items():
        #print(f"{token}: {dict(context)}")
    