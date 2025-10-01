# implementacja algorytmu Bellmana-Forda, graf jest jako reprezentacja listowa
# O(V*E)
# graf: https://www.google.com/url?sa=i&url=https%3A%2F%2Ftutorialhorizon.com%2Falgorithms%2Fweighted-graph-implementation-java%2F&psig=AOvVaw3G2gq5tlWiT25Aw43hY9Tx&ust=1745761641165000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJixjIfr9YwDFQAAAAAdAAAAABAE
def relax(v, u, w, graph, distance, parent):  # v -> u
    if distance[v] + w < distance[u]:
        distance[u] = distance[v] + w
        parent[u] = v


def bellman_ford(graph, start):
    n = len(graph)
    distance = [float('inf')] * n
    distance[start] = 0
    parent = [None] * n
    # relaksujemy KAŻDĄ krawędź |V|-1 razy czyli n-1 razy
    for _ in range(n - 1):
        for v in range(n):
            for u, w in graph[v]:
                relax(v, u, w, graph, distance, parent)
    # sprawdzenie czy jest jakiś ujemny cykl, jak tak to return None
    for v in range(n):
        for u, w in graph[v]:
            if distance[v] + w < distance[u]:
                return None

    return distance


graph = [
    [(1, 4), (2, 3)],  # wierzchołek 0 → 1 (waga 4), 0 → 2 (waga 3)
    [(3, 2), (2, 5)],   # wierzchołek 1 → 3 (waga 2), 1 → 2 (waga 5)
    [(3, 7)],           # wierzchołek 2 → 3 (waga 7)
    [(4, 2)],           # wierzchołek 3 → 4 (waga 2)
    [(0, 4), (1, 4), (5, 6)],  # wierzchołek 4 → 0 (waga 4), 4 → 1 (waga 4), 4 → 5 (waga 6)
    []                  # wierzchołek 5 nie ma krawędzi wychodzących
]
print(bellman_ford(graph,0))