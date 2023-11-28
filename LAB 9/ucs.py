import heapq

class Node:
    def __init__(self, state, cost, parent=None):
        self.state = state
        self.cost = cost
        self.parent = parent

    def __lt__(self, other):
        return self.cost < other.cost

def uniform_cost_search(graph, start_state, goal_state):
    visited = set()
    priority_queue = [Node(start_state, 0)]
    
    while priority_queue:
        current_node = heapq.heappop(priority_queue)
        current_state = current_node.state

        if current_state in visited:
            continue

        visited.add(current_state)

        if current_state == goal_state:
            return get_path(current_node)

        for neighbor, cost in graph[current_state].items():
            if neighbor not in visited:
                new_cost = current_node.cost + cost
                heapq.heappush(priority_queue, Node(neighbor, new_cost, current_node))

    return None  # Goal state not found

def get_path(node):
    path = []
    while node:
        path.insert(0, node.state)
        node = node.parent
    return path

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'D': 2},
    'C': {'A': 4, 'E': 5},
    'D': {'B': 2, 'F': 3},
    'E': {'C': 5, 'G': 2},
    'F': {'D': 3},
    'G': {'E': 2}
}

start_state = 'A'
goal_state = 'G'

path = uniform_cost_search(graph, start_state, goal_state)

if path:
    print(f"Uniform Cost Search Path from {start_state} to {goal_state}: {path}")
else:
    print(f"Goal state {goal_state} not reachable from {start_state}.")
