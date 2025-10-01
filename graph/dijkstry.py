# implementacja algorytmy Dijkstra, graf w reprezentacji macierzowej
from graph.dfs_applications.dfs_recursive import visited


# O(V^2)
def relax(u, v, visited, parent, distance, graph):  # u -> v
    if not visited[v] and graph[u][v] > 0 and distance[u] + graph[u][v] < distance[v]:
        distance[v] = distance[u] + graph[u][v]
        parent[v] = u


def dijktra(graph, start):
    n = len(graph)
    visited = [False] * n
    parent = [None] * n
    distance = [float('inf')] * n
    distance[start] = 0
    for _ in range(n):
        # szukanie nieodwiedzonego wierzcholka z najmniejszym distance
        min_dist, u = float('inf'), -1
        for i in range(n):
            if not visited[i] and distance[i] < min_dist:
                u = i
                min_dist = distance[i]

        if u == -1:  # nie ma juz zadnych wierzcholkwo do odwiedzenia
            break

        visited[u] = True # wybieramy ten wierzchołek

        for v in range(n):
            relax(u, v, visited, parent, distance, graph)
    return distance


adj_matrix = [
    # 0   1    2    3 4
    [0, 5, 4, 20, 0],  # 0
    [5, 0, 1, 0, 0],  # 1
    [4, 1, 0, 3, 0],  # 2
    [2, 0, 3, 0, 6],  # 3
    [0, 0, 0, 6, 0]  # 4
]
# print(dijktra(adj_matrix,0))
dijktra(adj_matrix, 0)
# implementacja algorytmy Dijkstra, graf w reprezentacji listy sąsiedztwa
# O((V+E)⋅logV) czyli mniej wiecej vlogv
import heapq

def relax_z_heapem(u, v, weight, distance, parent, heap, visited):
    if not visited[v] and distance[u] + weight < distance[v]:
        distance[v] = distance[u] + weight
        parent[v] = u
        heapq.heappush(heap, (distance[v], v))


def dijkstra(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    parent = [None] * n
    visited = [False] * n
    distance[start] = 0
    heap = [(0, start)]  # (dystans, wierzchołek)

    while heap:
        dist_u, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True

        for v, weight in graph[u]:
            relax_z_heapem(u, v, weight, distance, parent, heap, visited)

    return distance, parent
