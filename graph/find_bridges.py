#znajdz most w grafie, reprezentacja listy sasiedztwa
def find_bridges(graph):
    n=len(graph)
    visited=[False]*n
    parent=[None]*n
    disc=[0]*n
    low=[0]*n
    res=set()
    time=0
    def dfs(v):
        nonlocal time
        visited[v]=True
        disc[v]=low[v]=time
        time+=1
        for av in graph[v]:
            if not visited[av]:
                parent[av]=v
                dfs(av)
                low[v]=min(low[v],low[av])
                if low[av] > disc[v]:
                    res.add((min(v, av), max(v, av)))  # Dodajemy most w uporządkowanej formie
            elif parent[v]!=av:
                low[v]=min(low[v],disc[av])
    for i in range(n):
        if not visited[i]:
            dfs(i)
    return res

