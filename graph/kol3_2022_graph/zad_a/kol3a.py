# złożoność ElogV
# czyli złożoność wzorcowa

from queue import PriorityQueue
from kol3atesty import runtests
from math import inf


def spacetravel(n, E, S, a, b):
    # tu prosze wpisac wlasna implementacje
    # tworzę listę sąsiedztwa
    G = [[] for _ in range(n)]
    for v, u, waga in E:
        G[v].append((u, waga))
        G[u].append((v, waga))
    for i in range(len(S)):
        for j in range(i+1,len(S)):
            G[S[i]].append((S[j],0))
            G[S[j]].append((S[i],0))

    dist = [inf] * n
    dist[a] = 0
    q = PriorityQueue()
    q.put((0, a))  # (czas,planeta)
    while not q.empty():
        t, v = q.get()
        if t > dist[v]:
            continue
        if v==b:
            return t
        # relaksacja
        for u, waga in G[v]:
            if dist[u] > dist[v] + waga:
                dist[u] = dist[v] + waga
                q.put((dist[u],u))

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
