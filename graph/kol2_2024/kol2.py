from queue import PriorityQueue
from kol2testy import runtests
from math import inf


def warrior(G, s, t):
    # tu prosze wpisac wlasna implementacje
    n = max(max(v, u) for v, u, _ in G)+1
    graph = [[] * n for _ in range(n)]
    for v, u, waga in G:
        graph[v].append((u, waga))
        graph[u].append((v, waga))
    dist = [[inf] * 17 for _ in
            range(n)]  # do danego wierzcholka mozna dojsc w 17 stanach albo byc wypoczatey albo teired (1,16)
    dist[s][0] = 0
    q = PriorityQueue()
    q.put((0, s, 0))  # (czas całkowity, miasteczko, ilość godzin bez odpoczynku - tired)
    while not q.empty():
        time, v, tired = q.get()
        if time > dist[v][tired]:
            continue
        if v == t:
            return time
        if tired > 0 and dist[v][0]>time +8:
            dist[v][0] = time + 8
            q.put((time+8,v,0))
        for u, waga in graph[v]:
            if waga + tired <= 16 and dist[u][waga + tired] > time + waga:
                dist[u][waga + tired] = time + waga
                q.put((time + waga, u, waga + tired))

    return inf  # nie da się dotrzeć


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(warrior, all_tests=True)
