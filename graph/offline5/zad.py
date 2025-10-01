from zadtesty import runtests
from math import inf
from collections import deque


def goodknight(G, s, t):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    dist = [[inf] * 17 for _ in range(n)]
    dist[s][0] = 0
    q = deque([(s, 0)])
    while q:
        v, tired = q.popleft()
        cur_time = dist[v][tired]
        if v != 0 and v != n - 1 and tired > 0:  # jest sens odpoczywać
            if dist[v][0] > cur_time + 8:
                dist[v][0] = cur_time + 8
                q.append((v,0))
        for u in range(n):
            if G[v][u]!=-1 and tired + G[v][u]<=16 and G[v][u]+cur_time<dist[u][tired+G[v][u]]:
                dist[u][tired + G[v][u]] = G[v][u]+cur_time
                q.append((u,tired+G[v][u]))
    return min(dist[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)
