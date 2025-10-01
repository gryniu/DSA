class UnionFind:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0] * n

    def find(self, u):  # znajdowanie reprezentanta
        if self.parent[u] != u:  # u nie jest reprezentantem
            self.parent[u] = self.find(self.parent[u])  # kompresja ścieżki
        return self.parent[u]

    def union(self, v, u):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u == root_v:  # to są te same zbiory, nie łączymy żęby nie było cyklu
            return False
        if self.rank[root_v] < self.rank[root_u]:
            self.parent[root_v] = root_u
        elif self.rank[root_v] > self.rank[root_u]:
            self.parent[root_u] = root_v
        else:  # mają takie same rangi
            self.parent[root_v] = root_u  # obojętnie tak czy na odwrót
            self.rank[root_u] += 1
        return True


def kruskal(G):  # graf w postaci listy sąsiedztwa
    n = len(G)
    uf = UnionFind(n)
    edges = []
    for v in range(n):
        for u, waga in G[v]:
            if v < u:
                edges.append((v, u, waga))
    edges = sorted(edges, key=lambda x: x[2])  # sortujemy po wagach
    total_cost = 0
    mst = []
    for v, u, waga in edges:
        if uf.union(v, u):
            mst.append((v, u, waga))
            total_cost += waga
    return mst, total_cost
