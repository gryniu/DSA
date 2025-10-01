# graf jako macierz adjencji


def dfs(adjency_matrix, start):
    n = len(adjency_matrix)
    stack = [start]
    visited = [False for _ in range(n)]
    visited[start] = True
    order = []
    while stack:
        v = stack.pop()
        order.append(v)
        for u in range(n):
            if adjency_matrix[v][u] == 1 and not visited[u]:
                stack.append(u)
                visited[u] = True
    return order


adjency_matrix = [
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0]
]

print(dfs(adjency_matrix, 3))
