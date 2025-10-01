from collections import deque
from egz3atesty import runtests


def mykoryza(G, T, d):
    # tu prosze wpisac wlasna implementacje
    k = len(T)  # ilosc skarzonych drzew
    n = len(G)  # ilosc drzew
    q = deque()  # (time,idx)
    visited = [False for _ in range(n)]
    for i in range(k):
        q.append((T[i],i))  # (time,idx)
        visited[T[i]] = True
    res = 1
    while q:
        v,tree = q.popleft()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                q.append((u,tree))
                if tree==d:
                    res+=1

    return res


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(mykoryza, all_tests=True)
