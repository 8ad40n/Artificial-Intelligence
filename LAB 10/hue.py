import heapq

class HeuristicGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, cost, heuristic=0):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost, heuristic))

    def heuristic_search(self, start, goal):
        open_set = [(0 + self.graph[start][0][2], start, [])]  # f = g + h
        closed_set = set()

        while open_set:
            f, current, path = heapq.heappop(open_set)

            if current in closed_set:
                continue

            path = path + [current]

            if current == goal:
                return path

            closed_set.add(current)

            for neighbor, cost, heuristic in self.graph[current]:
                if neighbor not in closed_set:
                    heapq.heappush(open_set, (f + cost + heuristic, neighbor, path))

if __name__ == "__main__":
    graph_heuristic = HeuristicGraph()
    graph_heuristic.add_edge('A', 'B', 1, 4)
    graph_heuristic.add_edge('A', 'C', 3, 2)
    graph_heuristic.add_edge('B', 'D', 2, 4)
    graph_heuristic.add_edge('C', 'D', 1, 2)
    graph_heuristic.add_edge('D', 'E', 3, 1)

    path_heuristic = graph_heuristic.heuristic_search('A', 'E')
    print("Optimal and complete path using heuristic search:", path_heuristic)
