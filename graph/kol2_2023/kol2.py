from kol2testy import runtests
# złożoność : O(V*E)
# wzorcówka

class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, u):  # szukamy reprezentanta u
        if self.parent[u] != u:  # u nie jest reprezentantem
            self.parent[u] = self.find(self.parent[u])  # szukamy rekurencyjnie reprezentanta
        return self.parent[u]

    def union(self, v, u):
        root_v = self.find(v)
        root_u = self.find(u)
        if root_v == root_u:
            return False  # u i v należą do tego samego componentu
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:  # ranks są takie same
            self.parent[root_u] = root_v
            self.rank[root_v] += 1
        return True


def beautree(G):
    # tu prosze wpisac wlasna implementacje
    n = len(G)
    edges = []
    # E
    for v in range(n):
        for u, waga in G[v]:
            if v < u:
                edges.append((v, u, waga))
    # ElogE
    edges = sorted(edges, key=lambda x: x[2])
    # robimy okienko
    start = 0
    end = n-1 # ilość krawedzi w mst
    while end<=len(edges):
        uf = UnionFind(n) #ilość wierzchołków
        i=start
        total=0
        while i<end:
            v,u,waga=edges[i]
            if uf.union(v,u):
                total+=waga
            else:
                break
            i+=1
        # przesuwamy okienko
        if i==end:
            return total
        end+=1
        start+=1
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(beautree, all_tests=True)
