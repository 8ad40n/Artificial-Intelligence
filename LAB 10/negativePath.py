class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = []

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, weight):
        self.edges.append((from_node, to_node, weight))

def bellman_ford(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0

    for _ in range(len(graph.nodes) - 1):
        for from_node, to_node, weight in graph.edges:
            if distances[from_node] + weight < distances[to_node]:
                distances[to_node] = distances[from_node] + weight

    # Check for negative cycles
    for from_node, to_node, weight in graph.edges:
        if distances[from_node] + weight < distances[to_node]:
            raise ValueError("Graph contains a negative cycle")

    return distances

# Example usage:
graph = Graph()

# Add nodes
graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')

# Add edges with negative weights
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 3)
graph.add_edge('B', 'D', -7)  # Negative weight
graph.add_edge('C', 'D', 2)

start_node = 'A'

shortest_distances = bellman_ford(graph, start_node)

for node, distance in shortest_distances.items():
    print(f"Shortest distance from {start_node} to {node}: {distance}")
