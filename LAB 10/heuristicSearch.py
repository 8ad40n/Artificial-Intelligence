import heapq

class GreedyBestFirstSearchWithPath:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, cost, heuristic=0):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost, heuristic))

    def greedy_best_first_search(self, start, goal):
        open_set = [(0, start, [start])]
        closed_set = set()

        while open_set:
            _, current, path = heapq.heappop(open_set)

            if current in closed_set:
                continue

            if current == goal:
                return path

            closed_set.add(current)

            for neighbor, _, heuristic in sorted(self.graph[current], key=lambda x: x[2]):
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (heuristic, neighbor, path + [neighbor]))

        return []

if __name__ == "__main__":
    graph_greedy = GreedyBestFirstSearchWithPath()
    graph_greedy.add_edge('A', 'B', 1, 4)
    graph_greedy.add_edge('A', 'C', 3, 2)
    graph_greedy.add_edge('B', 'D', 2, 4)
    graph_greedy.add_edge('C', 'D', 1, 2)
    graph_greedy.add_edge('D', 'E', 3, 1)

    path_greedy = graph_greedy.greedy_best_first_search('A', 'E')

    if path_greedy:
        print("Path found using Greedy Best-First Search:", path_greedy)
    else:
        print("No path found using Greedy Best-First Search.")
