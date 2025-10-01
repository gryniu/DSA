from queue import PriorityQueue

from egz3atesty import runtests
from math import inf


def goodknight(G, s, t):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    dist = [[inf] * 17 for _ in range(n)]
    graph =[[] for _ in range(n)]
    dist[s][0] = 0
    q = PriorityQueue()
    q.put((0, s, 0))

    while not q.empty():
        d, v, time = q.get() # czas ogolny, miasto, czas bez odpoczynku
        if d > dist[v][time]:
            continue
        for u in range(n):
            weight = G[v][u]
            if weight==-1:
                continue
            if weight + time <= 16:
                if dist[u][time + weight] > weight + dist[v][time]:
                    dist[u][time + weight] = weight + dist[v][time]
                    q.put((dist[u][time + weight], u, time + weight))
            if dist[u][weight] > weight + dist[v][time] + 8:
                dist[u][weight] = weight + dist[v][time] + 8
                q.put((dist[u][weight], u, weight))
    return min(dist[t])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(goodknight, all_tests=True)
