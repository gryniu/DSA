from kol2testy import runtests
from math import inf
from collections import deque


def warrior(G, s, t):
    n = 0
    for u, v, _ in G:
        n = max(n, u, v)
    n += 1

    graph = [[] for _ in range(n)]
    for u, v, w in G:
        graph[u].append((v, w))
        graph[v].append((u, w))
    dist = [[inf] * 17 for _ in range(n)]
    dist[s][0] = 0
    q = deque([(s, 0)])  # (miasto, tired)
    while q:
        v, tired = q.popleft()
        cur_time = dist[v][tired]
        if v != 0 and v != n - 1 and tired > 0:  # jest sens odpoczywac
            if dist[v][0] > cur_time + 8:
                dist[v][0] = cur_time + 8
                q.append((v, 0))
        for u, czas in graph[v]:
            if czas + tired <= 16 and dist[u][czas + tired] > cur_time + czas:
                dist[u][czas + tired] = cur_time + czas
                q.append((u,czas+tired))
    return min(dist[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)
