# Tarjan's algorithm O(V+E) - algorytm na znajdowanie punktów artykulacji
# Graf w postaci listy sąsiedztwa
time = 0 # deklaracja zmiennej globalnej
def find_AP(graph, v, n, visited, disc, low, parent, res):
    global time  # Używamy zmiennej globalnej time

    visited[v] = True
    disc[v] = low[v] = time
    time += 1

    child = 0
    for av in graph[v]:
        if not visited[av]:
            parent[av] = v
            child += 1
            find_AP(graph, av, n, visited, disc, low, parent, res)
            low[v] = min(low[v], low[av])

            # Warunki dla punktów artykulacji
            if parent[v] is None and child > 1:
                res.add(v)
            elif parent[v] is not None and low[av] >= disc[v]:
                res.add(v)
        elif av != parent[v]:  # back edge
            low[v] = min(low[v], disc[av])


# Reprezentacja grafu jako lista sąsiedztwa
graph = [[1, 3], [0, 2], [1, 3, 6], [0, 2, 4, 5], [3, 5], [3, 4], [2]]
n = len(graph)
visited = [False for _ in range(n)]
disc = [0 for _ in range(n)]
low = [0 for _ in range(n)]
parent = [None for _ in range(n)]
res = set()

# Wywołanie funkcji bez przekazywania `time`
find_AP(graph, 0, n, visited, disc, low, parent, res)

# Wypisanie wyników
print(sorted(res))
#UWAGA - ładniej to zrobić w klasie, class GRAPH - zrób później