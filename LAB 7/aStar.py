import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(graph, start, goal):
    open_list = [Node(start, None, 0, graph[start]['heuristic'])]
    closed_set = set()

    while open_list:
        current_node = heapq.heappop(open_list)

        if current_node.state == goal:
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]

        if current_node.state in closed_set:
            continue

        closed_set.add(current_node.state)

        for neighbor, cost in graph[current_node.state]['neighbors'].items():
            if neighbor in closed_set:
                continue

            cost_to_neighbor = current_node.cost + cost
            heuristic_to_goal = graph[neighbor]['heuristic']
            neighbor_node = Node(neighbor, current_node, cost_to_neighbor, heuristic_to_goal)

            heapq.heappush(open_list, neighbor_node)

    return None

graph = {
    'A': {'heuristic': 5, 'neighbors': {'B': 1, 'C': 2}},
    'B': {'heuristic': 3, 'neighbors': {'D': 3, 'E': 1}},
    'C': {'heuristic': 2, 'neighbors': {'F': 2}},
    'D': {'heuristic': 1, 'neighbors': {'G': 4}},
    'E': {'heuristic': 2, 'neighbors': {'G': 1}},
    'F': {'heuristic': 1, 'neighbors': {'G': 3}},
    'G': {'heuristic': 0, 'neighbors': {}}
}

start_state = 'A'
goal_state = 'G'

path = astar_search(graph, start_state, goal_state)

if path:
    print("Path:", path)
else:
    print("No path found")
