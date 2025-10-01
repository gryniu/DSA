from math import inf
from queue import PriorityQueue


def cheapest_decreasing_way(G, a, b):
    n=max(max(v,u) for v,u,_ in G) + 1
    graph = [[]*n for _ in range(n)]
    for v,u,w in G:
        graph[v].append((u,w))
        graph[u].append((v,w))
    stany = max(w for _,_,w in G) + 1
    dist =[[inf]*stany for _ in range(n)]
    dist[a][stany-1] = 0
    q = PriorityQueue()
    q.put((0,a,stany-1)) # stany-1 to max_weight
    while not q.empty():
        cost,v,waga = q.get()
        if cost > dist[v][waga]:
            continue
        if v==b:
            return cost
        for u,w in graph[v]:
            if (w<waga or waga==stany-1) and dist[u][w]>cost + w:
                dist[u][w] = cost + w
                q.put((cost + w,u,w))


# Graf w formie listy krawędzi (v, u, w) - (wierzcholek początkowy, wierzcholek końcowy, waga krawędzi)
G = [
    (0, 1, 10),  # krawędź 0-1 o wadze 10
    (0, 2, 8),  # krawędź 0-2 o wadze 8
    (1, 2, 5),  # krawędź 1-2 o wadze 5
    (1, 3, 4),  # krawędź 1-3 o wadze 4
    (2, 3, 7),  # krawędź 2-3 o wadze 7
    (2, 4, 3),  # krawędź 2-4 o wadze 3
    (3, 4, 6)  # krawędź 3-4 o wadze 6
]

# Testowanie algorytmu warrior_decreasing_edges
a = 0  # wierzchołek początkowy
b = 4  # wierzchołek docelowy

result = cheapest_decreasing_way(G, a, b)
print(result)
