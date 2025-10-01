def dfs_recursive(adjency_matrix,v,visited,order):
    visited[v] = True
    order.append(v)
    for u in range(len(adjency_matrix)):
        if adjency_matrix[v][u] == 1 and not visited[u]:
            dfs_recursive(adjency_matrix,u,visited,order)

adjency_matrix = [
    [0, 0, 1, 0, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0]
]
visited=[False for _ in range(len(adjency_matrix))]
order=[]
dfs_recursive(adjency_matrix,3,visited,order)
print(order)
