# Bartosz Gryń
from zad3testy import runtests
from collections import deque


def longer(G, s, t):
    n = len(G)
    dist_s = [-1] * n
    Q = deque([s])
    visited = [False] * n
    dist_s[s] = 0
    visited[s]=True
    count_s=[0]*n
    count_s[s]=1
    while Q:  # BFS
        v = Q.popleft()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                Q.append(u)
                dist_s[u] = dist_s[v] + 1
                count_s[u]=count_s[v]
            elif dist_s[u]==dist_s[v]+1:
                count_s[u]+=count_s[v]
    if dist_s[t]==-1:
        return None
    dist_t =[-1]*n
    Q = deque([t])
    visited = [False] * n
    visited[t]=True
    dist_t [t] = 0
    count_t = [0] * n
    count_t[t] = 1
    while Q:  # BFS
        v = Q.popleft()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                Q.append(u)
                dist_t [u] = dist_t [v] + 1
                count_t[u] = count_t[v]
            elif dist_t [u]==dist_t [v]+1:
                count_t[u]+=count_t[v]

    shortest_path_counter = count_s[t]
    shortest_path=dist_s[t]
    Q=deque([s])
    visited=[False]*n
    visited[s]=True
    while Q:
        v=Q.popleft()
        for u in G[v]:
            if not visited[u]:
                if dist_s[v]+dist_t [u]+1==shortest_path and count_s[v]*count_t[u]==shortest_path_counter:
                    return (v,u)
                if dist_s[u] + dist_t [v] + 1 == shortest_path and count_s[u] * count_t[v] == shortest_path_counter:
                    return (u, v)
                Q.append(u)
                visited[u]=True
    return None
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
# G=[[1,2],[0,3],[0,3],[1,2,4],[3]]
# s=0
# t=4
# print(longer(G,s,t))