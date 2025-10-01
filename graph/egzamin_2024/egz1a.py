from queue import PriorityQueue

from egz1atesty import runtests
from math import inf, floor

from graph.articulation_points import visited


def armstrong(B, G, s, t):
    # tu prosze wpisac wlasna implementacje
    ilosc_rowerow = len(B)
    n = 0
    for v, u, _ in G:
        n = max(n, v, u)
    n += 1
    graph = [[] for _ in range(n)]
    for v, u, waga in G:
        graph[v].append((u, waga))
        graph[u].append((v, waga))
    bb = [[] for _ in range(n)]
    k = 0
    for i, p, q in B:
        if p < q:
            bb[i].append((p / q, k+1))
            k += 1
    dist = [[inf] * (ilosc_rowerow + 1) for _ in range(n)]
    dist[s][0] = 0
    q = PriorityQueue()
    q.put((0, s, -1, 0))
    while not q.empty():
        time, v, speed, ktory = q.get()
        if time >dist[v][ktory]:
            continue
        if v == t:
            return floor(time)
        if ktory == 0:  # wsiadamy na rowery
            for nowy_speed, nowy_ktory in bb[v]:
                if time < dist[v][nowy_ktory]:
                    dist[v][nowy_ktory] = time
                    q.put((time, v, nowy_speed, nowy_ktory))
        for u, waga in graph[v]:
            if ktory == 0:
                if dist[u][0] > dist[v][0] + waga:
                    dist[u][0] = dist[v][0] + waga
                    q.put((dist[u][0], u, -1,0))
            else:
                if dist[u][ktory] > dist[v][ktory] + waga * speed:
                    dist[u][ktory] = dist[v][ktory] + waga * speed
                    q.put((dist[u][ktory],u,speed,ktory))

    # ewentualne pojechanie rowerem
    return -1


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(armstrong, all_tests=True)
