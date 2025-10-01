# sortowanie topologiczne za pomocą DFS
# graf podany jako macierz adjencji
# O(V+E)
def dfs(i, order, adj_matrix, visited, v):  # i to na jakie miejsce dajemy w order
    visited[v] = True
    for u in range(len(adj_matrix)):
        if adjency_matrix[v][u] == 1 and not visited[u]:
            i = dfs(i, order, adj_matrix, visited, u)
    order[i] = v
    return i - 1


def topology_sort(adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    order = [None] * n
    j = n - 1
    for v in range(n):
        if not visited[v]:
            j = dfs(j, order, adj_matrix, visited, v)
    return order

adjency_matrix = [
    [0, 1, 1, 0, 0, 0],  # 0 → 1, 2
    [0, 0, 0, 1, 1, 0],  # 1 → 3, 4
    [0, 0, 0, 1, 0, 0],  # 2 → 3
    [0, 0, 0, 0, 0, 1],  # 3 → 5
    [0, 0, 0, 0, 0, 1],  # 4 → 5
    [0, 0, 0, 0, 0, 0],  # 5 → (koniec)
]
print(topology_sort(adjency_matrix))
