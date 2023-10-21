from collections import deque

def bfs_search(graph, start, goal):
    visited = set()
    queue = deque()

    queue.append(start)
    visited.add(start)

    while queue:
        current_node = queue.popleft()
        if current_node == goal:
            return current_node

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

    return None  # Goal node not found

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'

result = bfs_search(graph, start_node, goal_node)

if result:
    print(f"Goal node {goal_node} found!")
else:
    print(f"Goal node {goal_node} not found.")
