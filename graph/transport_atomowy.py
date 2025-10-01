from collections import deque

INF = float('inf')

# Funkcja Floyda-Warshalla do obliczenia najkrótszych odległości
def warshall(G):
    n = len(G)
    dist = [[INF] * n for _ in range(n)]  # Inicjalizujemy macierz odległości

    # Ustawiamy odległości do siebie samych na 0
    for i in range(n):
        dist[i][i] = 0

    # Wypełniamy macierz odległości na podstawie grafu
    for u in range(n):
        for v, w in G[u]:
            dist[u][v] = w  # waga krawędzi między u a v

    # Algorytm Floyda-Warshalla
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist


def transport_atomowy(G, s, t, d):
    n = len(G)
    dist = warshall(G)  # Uzyskujemy najkrótsze odległości między wszystkimi parami wierzchołków

    visited_A = [False] * n  # Mapa odwiedzonych wierzchołków przez A
    visited_B = [False] * n  # Mapa odwiedzonych wierzchołków przez B

    # Kolejka BFS zawierająca pary (A, B)
    queue = deque()
    queue.append((s, t))  # Początkowe pary: (A, B)

    visited_A[s] = True
    visited_B[t] = True

    while queue:
        a, b = queue.popleft()

        # Jeżeli dotarliśmy do stanu (t, s), zwróć sukces
        if a == t and b == s:
            return True  # Sukces

        # A porusza się do swoich sąsiadów, z zachowaniem odległości
        for na, _ in G[a]:
            for nb,_ in G[b]:
                if (not visited_A[na] and not visited_B[b]) and dist[na][b]>=d:# ruszamy A zostawiamy B
                    queue.append((na,b))
                if (not visited_A[a] and not visited_B[nb]) and dist[a][nb]>=d:# ruszamy B zostawiamy A
                    queue.append((a,nb))
                if (not visited_A[na] and not visited_B[nb]) and dist[na][nb]>=d:# ruszamy A ruszamy B
                    queue.append((na,nb))
    return False  # Nie da się

# Testowy graf
d = 4
G = [
    [(1, 3), (2, 4)],  # wierzchołek 0: sąsiedzi 1 (waga 3) i 2 (waga 4)
    [(0, 3), (2, 8), (3, 3)],  # wierzchołek 1: sąsiedzi 0 (waga 3), 2 (waga 8) i 3 (waga 3)
    [(0, 4), (1, 8), (3, 5)],  # wierzchołek 2: sąsiedzi 0 (waga 4), 1 (waga 8) i 3 (waga 5)
    [(1, 3), (2, 5), (4, 1)],  # wierzchołek 3: sąsiedzi 1 (waga 3), 2 (waga 5) i 4 (waga 1)
    [(3, 1)]  # wierzchołek 4: sąsiedź 3 (waga 1)
]

print(transport_atomowy(G, 0, 4, d))  # Powinno wypisać: True
