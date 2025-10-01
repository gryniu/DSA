from egz2btesty import runtests
from queue import PriorityQueue
from math import inf

def tory_amos(E, A, B):
    n = max(max(x, y) for x, y, d, typ in E) + 1
    G = [[] for _ in range(n)]

    # Konwersja typu toru na liczby: 'I' = 0, 'P' = 1
    TYP = {'I': 0, 'P': 1}

    for x, y, d, typ in E:
        t = TYP[typ]
        G[x].append((y, d, t))
        G[y].append((x, d, t))

    # dist[v][t] = najkrótszy czas do stacji v z rozstawem t
    dist = [[inf] * 2 for _ in range(n)]
    q = PriorityQueue()

    # Zgodnie z treścią: pociąg rusza z A i dopasowuje się do pierwszego toru
    for u, d, typ in G[A]:
        if dist[u][typ] > d:
            dist[u][typ] = d
            q.put((d, u, typ))

    while not q.empty():
        cur_d, v, cur_typ = q.get()
        if dist[v][cur_typ] < cur_d:
            continue

        for u, d_edge, typ in G[v]:
            # Koszt przejazdu przez stację v (jeśli to nie A)
            if cur_typ != typ:
                cost_station = 20
            elif typ == 0:
                cost_station = 5
            else:
                cost_station = 10

            new_d = cur_d + cost_station + d_edge
            if new_d < dist[u][typ]:
                dist[u][typ] = new_d
                q.put((new_d, u, typ))

    return min(dist[B])

# from collections import deque
#
# from collections import defaultdict, deque
#
# def tory_amos(E, A, B):
#     # Budowa grafu: G[stacja] = lista (sąsiad, długość, typ)
#     G = defaultdict(list)
#     for u, v, d, typ in E:
#         G[u].append((v, d, typ))
#         G[v].append((u, d, typ))
#
#     # Rozstawy: 'I' = 0, 'P' = 1
#     R = {'I': 0, 'P': 1}
#     MAX_COST = 100_000  # może być większy — tu umowny limit
#
#     n = max(max(u, v) for u, v, _, _ in E) + 1
#     dist = [[float('inf')] * 2 for _ in range(n)]
#
#     buckets = [deque() for _ in range(MAX_COST + 1)]
#
#     # Startujemy z A wszystkimi możliwymi rozstawami (bo nie wiemy, który tor będzie pierwszy)
#     for v, d, typ in G[A]:
#         typ_idx = R[typ]
#         cost = d  # na start nie płacimy kosztu przejazdu przez stację
#         if dist[v][typ_idx] > cost:
#             dist[v][typ_idx] = cost
#             buckets[cost].append((v, typ_idx))
#
#     # Dial's Algorithm
#     for current_cost in range(MAX_COST + 1):
#         while buckets[current_cost]:
#             u, last_typ = buckets[current_cost].popleft()
#             if dist[u][last_typ] < current_cost:
#                 continue  # już odwiedzone taniej
#
#             for v, d, typ in G[u]:
#                 t_idx = R[typ]
#                 # koszt wejścia i wyjścia z tej stacji
#                 if last_typ == t_idx:
#                     station_cost = 5 if t_idx == R['I'] else 10
#                 else:
#                     station_cost = 20
#                 total_cost = dist[u][last_typ] + station_cost + d
#                 if dist[v][t_idx] > total_cost:
#                     dist[v][t_idx] = total_cost
#                     if total_cost <= MAX_COST:
#                         buckets[total_cost].append((v, t_idx))
#
#     return min(dist[B])
#

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(tory_amos, all_tests=True)
