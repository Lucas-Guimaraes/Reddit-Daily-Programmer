# https://www.reddit.com/r/dailyprogrammer/comments/s2no2/4102012_challenge_38_easy/

import heapq


def dijkstra(graph, starting_vertex):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[starting_vertex] = 0

    pq = [(0, starting_vertex)]

    while len(pq) > 0:
        c_distance, c_vertex = heapq.heappop(pq)

        if c_distance > distances[c_vertex]:
            continue

        for neighbor, weight in graph[c_vertex].items():
            distance = c_distance + weight


            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


ex_graph = {
    'U': {'V': 2, 'W': 5, 'X': 1},
    'V': {'U': 2, 'X': 2, 'W': 3},
    'W': {'V': 3, 'U': 5, 'X': 3, 'Y': 1, 'Z': 5},
    'X': {'U': 1, 'V': 2, 'W': 3, 'Y': 1},
    'Y': {'X': 1, 'W': 1, 'Z': 1},
    'Z': {'W': 5, 'Y': 1},
}
print(dijkstra(ex_graph, 'X'))
raw_input()