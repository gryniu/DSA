#Bartosz Gryń
# na początku zamieniam tą reprezentacje na reprezentacje listy sąsiedztw, po pierwsze
# żeby było mi prościej a po 2, żebym mógł skorzystać z kopca (żeby mieć lepszą złożoność)
# następnie dodaje krawędzie o wadze 1, dla każdego wierzchołka z S (krawędzie nieskierowane)
# po tym przygotowaniu sobie danych, odpalam standardowy algorytm dijkstra
# zatem złożoność algorytmu to (V+E)logV,
# chyba podchodzi to pod złożoność prawie wzorcową O(V+ElogV)
from zad4testy import runtests
import heapq

def relax(u,v,w,graph,distance,heap):# u -> v
    if distance[u] +w <distance[v]:
        distance[v] = distance[u] + w
        heapq.heappush(heap,(distance[v],v))

def dijkstra(n, graph, a, b):
    visited = [False] * n
    distance = [float('inf')] * n
    distance[a] = 0
    heap = [(0, a)]
    while heap:
        dist_u,u=heapq.heappop(heap)
        if visited[u]:
            continue
        for v,w in graph[u]:
            relax(u,v,w,graph,distance,heap)

    if distance[b]==float('inf'):
        return None
    return distance[b]


def spacetravel(n, E, S, a, b):
    # tu prosze wpisac wlasna implementacje
    # przerabiam tą nieprzyjemna reprezentacje grafu na listę sąsiedztwa
    graph = [[] for _ in range(n)]
    for u, v, w in E:
        graph[u].append((v, w))
        graph[v].append((u, w))
    # dodajemy zerowe krawedzi (zmiana czasoprzestrzeni)
    for i in range(len(S)):
        for j in range(i + 1, len(S)):
            graph[S[i]].append((S[j], 0))
            graph[S[j]].append((S[i], 0))
    return dijkstra(n,graph,a,b)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(spacetravel, all_tests=True)
