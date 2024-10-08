import numpy as np

def pagerank(adj_matrix,num_nodes, num_iterations=100, d=0.85):
    """
    Computes PageRank for a directed graph.

    Parameters:
    adj_matrix : 2D numpy array
        The adjacency matrix representing the graph where adj_matrix[i][j] indicates a link from node j to node i.
    num_iterations : int
        Number of iterations to run the algorithm.
    d : float
        Damping factor, typically set to 0.85.

    Returns:
    numpy array
        PageRank scores for each node.
    """
    #print(np.array(adj_matrix))
    #num_nodes = adj_matrix.shape[0]

    # Initialize pagerank scores
    pagerank_scores = np.ones(num_nodes) / num_nodes
    #print(pagerank_scores)

    # Normalize the adjacency matrix by outgoing links
    outbound_sums = adj_matrix.sum(axis=0)
    #print(outbound_sums)
    norm_adj_matrix = np.divide(adj_matrix, outbound_sums, where=outbound_sums!=0)

    for _ in range(num_iterations):
        pagerank_scores = (1 - d) / num_nodes + d * norm_adj_matrix.dot(pagerank_scores)

    return pagerank_scores
    
    #print(pagerank_scores)



if __name__ == "__main__":
    # Example usage:
    adj_matrix = np.array([[0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 
    0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0], [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])

    pagerank_scores = pagerank(adj_matrix,11)
    print("PageRank Scores:", pagerank_scores)