# import used libraries
import graphviz

# the graph data structure

class Graph:
    def __init__(self):
        self.nodes = {}
        self.graph = graphviz.Graph()
    
    def add_node(self,label):
        if label not in self.nodes:
            self.nodes[label] = Node(label)
        self.graph.node(label)
    
    def add_edge(self,label1,label2):
        if label1 not in self.nodes or label2 not in self.nodes:
            raise ValueError("Nodes must exist to add edge between them")
        node1 = self.nodes[label1]
        node2 = self.nodes[label2]

        node1.add_neighbor(node2)
        node2.add_neighbor(node1)
        self.graph.edge(label1, label2)
    
    def dfs(self,root):
        visited = set()
        while (len(visited) != len(self.nodes)):
            stack = [root]
            while stack:
                current_node = stack.pop()
                if current_node in visited:
                    continue
                visited.add(current_node)
                print(current_node)

                for neighbor in self.nodes[root].neighbors:
                    stack.append(neighbor.label)
            if(len(visited) == len(self.nodes)):
                break
            else:
                for label, node in self.nodes.items():
                    if(label not in visited):
                        root = label
                        break
        return visited
    def print_graph(self):
        for label, node in self.nodes.items():
            print(f"Node: {label}")
            for neighbor in node.neighbors:
                print(f"  - {neighbor.label}")
    def display_graph(self):
        self.graph.render("result",format="png", view=True)
    

class Node:
    def __init__(self, label):
        self.label = label
        self.neighbors = []

    def add_neighbor(self, neighbor):
        self.neighbors.append(neighbor)


graph = Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('E')
graph.add_node('F')
graph.add_node('G')
graph.add_node('H')


graph.add_edge('A', 'B')
graph.add_edge('B', 'C')
graph.add_edge('C', 'D')
graph.add_edge('D', 'A')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'E')
graph.add_edge('E', 'A')
graph.add_edge('F', 'G')
graph.add_edge('F', 'H')




graph.dfs('A')
graph.display_graph()