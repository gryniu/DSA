#bfs
#zadanie ile skladowych spojnych w grafie
#kup ksiazke cormmen
from collections import deque
def liczspojne_ja(graf):#graf to MACIERZ ADJACENNCJI adjency matrix
    def bfs(start,visited,graf):
        nonlocal visited
        Q = deque([start])
        visited[start]=True
        while Q:
            v = Q.popleft()
            for neighbour,is_connected in enumerate(graf):
                if is_connected==1:
                    visited[neighbour]=True
                    Q.append(neighbour)

    n=len(graf)
    counter = 0
    visited = [False for _ in range(n)]
    for i in range(n):
        if not visited[i]:
            bfs(i,visited,graf)
            counter += 1
