#sprawdzenie cyklu Eulera dla grafu NIESKIEROWANEGO
from collections import deque


def czy_spojny(adjency_matrix):
    n = len(adjency_matrix)
    if n == 0:
        return True
    Q = deque([0])
    visited = [False] * n
    visited[0] = True
    while Q:
        v = Q.popleft()
        for u in range(n):
            if adjency_matrix[v][u] == 1 and not visited[u]:
                Q.append(u)
                visited[u] = True
    return sum(visited) == n


def has_even_degree(adjency_matrix):
    spr = [sum(row) for row in adjency_matrix]
    return not all(deg % 2 for deg in spr)  # zwraca True jeżeli nie ma żadnych nieparzystych wierzchołków


def has_euler_cycle(adjency_matrix):
    n = len(adjency_matrix)
    # sprawdzenie czy graf spojny + sprawdzenie czy kazdy wierzcholek ma parzysty stopien
    if not czy_spojny(adjency_matrix) or not has_even_degree(adjency_matrix):
        return False
    tmp_matrix = [row[:] for row in adjency_matrix]
    path = []
    def dfs(v):
        for u in range(n):
            if tmp_matrix[v][u] == 1:
                tmp_matrix[v][u] -= 1
                tmp_matrix[u][v] -= 1
                dfs(u)
        path.append(v)
    dfs(0)
    return path
adj_matrix = [
    # 0  1  2  3  4  5
    [0, 1, 1, 0, 0, 0],  # Wierzchołek 0
    [1, 0, 1, 1, 1, 0],  # Wierzchołek 1
    [1, 1, 0, 1, 1, 0],  # Wierzchołek 2
    [0, 1, 1, 0, 1, 1],  # Wierzchołek 3
    [0, 1, 1, 1, 0, 1],  # Wierzchołek 4
    [0, 0, 0, 1, 1, 0]   # Wierzchołek 5
]
print(has_euler_cycle(adj_matrix))