from queue import PriorityQueue

from egz1atesty import runtests
from math import inf


def dijkstra(graph, n, start):
    dist = [inf for _ in range(n)]
    dist[start] = 0
    q = PriorityQueue()
    q.put((0, start))
    while not q.empty():
        d, v = q.get()
        if d > dist[v]:
            continue
        for u, waga in graph[v]:
            if dist[u] > dist[v] + waga:  # relaksacja
                dist[u] = dist[v] + waga
                q.put((dist[u], u))
    return dist


def armstrong(B, G, s, t):
    # tu prosze wpisac wlasna implementacje
    n = max(max(i, j) for i, j, _ in G) + 1

    rowery = [inf] * n  # inf oznacza ze nie ma roweru
    for i, p, q in B:
        if p < q:
            rowery[i] = min(rowery[i], p / q)
    graph = [[] for _ in range(n)]
    for u, v, waga in G:
        graph[u].append((v, waga))
        graph[v].append((u, waga))
    from_s = dijkstra(graph, n, s)
    from_t = dijkstra(graph, n, t)
    res = from_s[t] # przebiegniecie duathlonu bez roweru
    for v in range(n):
      if rowery[v]<1:
        res=min(res,from_s[v]+rowery[v]*from_t[v])

    return int(res)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
