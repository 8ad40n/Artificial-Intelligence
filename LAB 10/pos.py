import heapq

class PositiveGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))

    def dijkstra(self, start):
        distance = {vertex: float('infinity') for vertex in self.graph}
        distance[start] = 0
        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distance[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex]:
                distance_through_current = current_distance + weight

                if distance_through_current < distance[neighbor]:
                    distance[neighbor] = distance_through_current
                    heapq.heappush(priority_queue, (distance_through_current, neighbor))

        return distance

if __name__ == "__main__":
    graph_positive = PositiveGraph()
    graph_positive.add_edge('A', 'B', 2)
    graph_positive.add_edge('A', 'C', 1)
    graph_positive.add_edge('B', 'D', 4)
    graph_positive.add_edge('C', 'D', 3)
    graph_positive.add_edge('D', 'E', 5)

    distance_positive = graph_positive.dijkstra('A')
    print("Shortest path in a graph with positive edge values:", distance_positive)
