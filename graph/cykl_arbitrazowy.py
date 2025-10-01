from math import inf, log10


def arbitraz(G):
    n = len(G)
    dist = [inf] * n
    dist[0] = 0
    edges = []
    # dodawanie krawedzi zeby bylo v2 a nie v3
    for v in range(n):
        for u in range(n):
            if G[u][v]>0:
                weight = -log10(G[u][v])
                edges.append((v,u,weight))
    # Algorytm Bellmana - Forda
    for _ in range(n-1):
        for v,u,weight in edges:
            if dist[v]+weight<dist[u]: # relaksacja
                dist[u] = dist[v]+weight
    # Sprawdzanie ujemnych cykli
    for v, u, weight in edges:
        if dist[v] + weight < dist[u]:
            return True
    return False

G = [
    # PLN  USD   EUR   GBP
    [0.00, 0.23, 0.21, 0.00],  # PLN
    [4.25, 0.00, 0.91, 0.00],  # USD
    [4.75, 1.10, 0.00, 0.87],  # EUR
    [0.00, 0.00, 1.15, 0.00]  # GBP
]
print(arbitraz(G))
G = [
    # PLN  USD   EUR   GBP
    [0.00, 0.23, 0.21, 0.00],  # PLN
    [4.25, 0.00, 0.91, 0.00],  # USD
    [5.00, 1.10, 0.00, 0.87],  # EUR
    [0.00, 0.00, 1.15, 0.00]  # GBP
]
print(arbitraz(G))
G = [
    [0.00, 0.25, 0.20, 0.16],  # PLN
    [4.00, 0.00, 0.80, 0.64],  # USD
    [5.00, 1.25, 0.00, 0.80],  # EUR
    [6.25, 1.56, 1.25, 0.00]  # GBP
]
print(arbitraz(G))
