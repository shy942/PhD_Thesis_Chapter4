import networkx as nx
import matplotlib.pyplot as plt

# Function to create a graph from the co-occurrence matrix (My code)
def create_graph_my_code(calls):
    G = nx.DiGraph()
    
    for i in range(len(calls)-1):
        #print(i)
        # Top and Bottom (Class)
        callee = f"{calls[i][0]}"
        caller = f"{calls[i][1]}"
        if(callee!=caller):
            G.add_edge(caller, callee)
    
    #return G
    #print(G.nodes)
    #print(G.edges)
    #G = create_graph(cooccurrence_matrix)

    # Draw the graph
    #plt.figure(figsize=(10, 6))
    #pos = nx.spring_layout(G)
    #nx.draw(G, pos, with_labels=True, arrows=True, node_size=3000, node_color="lightblue", font_size=10, font_weight='bold')
    #plt.title('Graph')
    #plt.show()
    return G




# Function to create a graph from the co-occurrence matrix for dictonary
def create_graph_wight(cooccurrence_matrix):
    G = nx.Graph()
    
    for token, context in cooccurrence_matrix.items():
        for context_word, weight in context.items():
            if weight > 0:
                G.add_edge(token, context_word, weight=weight)
    
    #return G

    #G = create_graph(cooccurrence_matrix)

    # Draw the graph
    pos = nx.spring_layout(G)
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos, with_labels=True, node_size=5000, node_color="skyblue", font_size=15, font_weight="bold", edge_color="gray")
    plt.title("Word Co-occurrence Graph")
    plt.show()
