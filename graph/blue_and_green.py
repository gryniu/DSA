from math import inf


def floyd_warshall(G, n):
    dist = [row[:] for row in G]
    for i in range(n):
        dist[i][i] = 0
        for j in range(n):
            if i != j and dist[i][j] == 0:
                dist[i][j] = inf
    for k in range(n):
        for v in range(n):
            for u in range(n):
                if dist[v][k]+dist[k][u]<dist[v][u]:
                    dist[v][u] = dist[v][k]+dist[k][u]
    return dist
def BlueAndGreen(T,K,D):
    n = len(T)
    dist = floyd_warshall(T,n)
    print(dist)

T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ['B' ,'B', 'G', 'G', 'B']
D = 2
print(BlueAndGreen(T,K,D))