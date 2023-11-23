def dfs_limit(tree, current, goal, max_depth, path=[]):
    stack = [(current, 0, path + [current])]  
    visited = set()

    while stack:
        node, depth, current_path = stack.pop()
        if node == goal:
            print("Goal node '{}' found at depth {}.".format(goal, depth))
            print("Path:", " -> ".join(current_path))
            return True

        if depth < max_depth:
            for child in tree[node]:
                if child not in visited:
                    stack.append((child, depth + 1, current_path + [child]))
                    visited.add(child)

    return False

def iterative_deepening_search(tree, start, goal):
    max_depth = 0
    while True:
        print("Searching at depth limit:", max_depth)
        if dfs_limit(tree, start, goal, max_depth):
            break
        max_depth += 1

# Example usage
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': ['H', 'I'],
    'F': [],
    'G': ['J'],
    'H': [],
    'I': [],
    'J': []
}

start = 'A'
goal = 'G'

iterative_deepening_search(tree, start, goal)
