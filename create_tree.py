import networkx as nx
import random

def generate_random_tree(num_vertices):
    G = nx.Graph()

    for i in range(2, num_vertices + 1):
        parent = random.randint(1, i - 1)
        G.add_edge(parent, i)

    # Ensure the graph is connected (a single tree)
    while not nx.is_connected(G):
        # If not connected, add a random edge to connect components
        u = random.randint(1, num_vertices)
        v = random.randint(1, num_vertices)
        G.add_edge(u, v)

    return G

def write_graph_to_file(graph, filename):
    with open(filename, 'w') as file:
        # Write the first line: number of nodes, edges, and directed/undirected (0 for undirected)
        file.write(f"{graph.number_of_nodes()} {graph.number_of_edges()} 0\n")
        
        # Write the adjacency list
        for node in graph.nodes():
            neighbors = list(graph.neighbors(node))
            line = ' '.join(map(str, neighbors))
            file.write(f"{line}\n")

# Set the number of vertices
num_vertices = 300

# Generate a random tree (or forest)
tree = generate_random_tree(num_vertices)

# Write the graph to a .graph file
write_graph_to_file(tree, 'random_tree.graph')
