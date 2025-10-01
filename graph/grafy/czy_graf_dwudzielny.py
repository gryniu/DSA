#sprawdzic czy graf jest dwudzielny
#macierz sasiedztwa, adjency matrix
from collections import deque
def czydwudzielny_ja(adjency_matrix):
    def bfs_iter(s,adjency_matrix,colors):
        Q=deque([s])
        while Q:
            v=Q.popleft()
            for neighbour,is_connected in enumerate(adjency_matrix[v]):
                if is_connected==1:
                    if colors[neighbour]==colors[v]:
                        return False
                    colors[neighbour]=3-colors[v]
        return True

    n=len(adjency_matrix)
    colors = [-1 for _ in range(n)] #kolory pozniej beda ustawione na 1, 2
    colors[0] = 1
    for i in range(n):
        if colors[i]==-1:
            if not bfs_iter(i,adjency_matrix,colors):
                return False
    return True






"""
def czyDwudzielny(graf): #graf jest w postaci list sąsiadów, mozna visited
    #jest to BFS
    color=[-1 for _ in range(len(graf))] #kolory potem beda 1 i 2
    visited=[False for _ in range(len(graf))]
    visited[0]=True
    color[0]=0
    Q=deque()
    Q.append(0)
    while Q:
        v=Q.popleft()
        for n in graf[v]:#iterujemy po sasidach
            if color[n]==color[v]:
                return False
            if visited[n]==False:
                visited[n]=True
                color[n]=1-color[n]
                Q.append(v)
    return True
"""