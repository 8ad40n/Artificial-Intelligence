class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

def depth_limited_search(node, goal, depth_limit):
    return recursive_dls(node, goal, depth_limit)

def recursive_dls(node, goal, depth_limit):
    if node.data == goal:
        return [node.data]
    elif depth_limit == 0:
        return None
    else:
        cutoff_occurred = False
        for child in node.children:
            result = recursive_dls(child, goal, depth_limit - 1)
            if result is None or result == "cutoff":
                cutoff_occurred = True
            elif result != "cutoff":
                return [node.data] + result
        if cutoff_occurred:
            return "cutoff"
        else:
            return None

"""
          A
        / | \
       B  C  D
      / \   / \
     E   F G   H
"""
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')
node_g = Node('G')
node_h = Node('H')

node_a.add_child(node_b)
node_a.add_child(node_c)
node_a.add_child(node_d)
node_b.add_child(node_e)
node_b.add_child(node_f)
node_d.add_child(node_g)
node_d.add_child(node_h)

result_path = depth_limited_search(node_a, 'G', 3)
if result_path:
    print("Goal node found. Path:", " -> ".join(result_path))
else:
    print("Goal node not found within depth limit")
