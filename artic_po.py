import networkx as nx
import matplotlib.pyplot as plt
def articulation_points(graph):
    """
    Find articulation points in an undirected graph using DFS.
    
    Parameters:
    - graph: NetworkX graph object
    
    Returns:
    - List of articulation points
    """
    def dfs(node, parent, visited, disc, low, ap):
        nonlocal time
        children = 0
        visited[node] = True
        disc[node] = time
        low[node] = time
        time += 1

        for neighbor in graph.neighbors(node):
            if not visited[neighbor]:
                children += 1
                dfs(neighbor, node, visited, disc, low, ap)
                low[node] = min(low[node], low[neighbor])

                if low[neighbor] >= disc[node] and parent is not None:
                    ap[node] = True

                if low[neighbor] > disc[node] and parent is None:
                    ap[neighbor] = True

            elif neighbor != parent:
                low[node] = min(low[node], disc[neighbor])

    visited = {node: False for node in graph.nodes}
    disc = {node: float('inf') for node in graph.nodes}
    low = {node: float('inf') for node in graph.nodes}
    ap = {node: False for node in graph.nodes}
    time = 0

    for node in graph.nodes:
        if not visited[node]:
            dfs(node, None, visited, disc, low, ap)

    return [node for node in ap if ap[node]]


# Example usage:
# Create an example graph using NetworkX
G = nx.Graph()
G.add_edges_from([(0, 1),(0,2),(0,3)])
print("Articulation Points:", articulation_points(G))
ap = articulation_points(G)
# Draw the graph
pos = nx.spring_layout(G)  # Set layout for better visualization
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=10, font_color='black', edge_color='gray', linewidths=1, alpha=0.7)
nx.draw_networkx_nodes(G,pos,node_size=700, node_color='red',nodelist=ap)
# Display the graph
plt.show()
