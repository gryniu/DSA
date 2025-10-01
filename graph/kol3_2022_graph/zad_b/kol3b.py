from queue import PriorityQueue

from kol3btesty import runtests
from math import inf
def airports( G, A, s, t ):
    # tu prosze wpisac wlasna implementacje
    n=len(G)
    len_a=len(A)


    # DIJKSTRA
    koszt = [inf]*n # koszt[v] to finalnie będzie cena, którą trzeba wydać, żeby NAJTANIEJ znaleźć się na lotnisku v
    koszt[s] = 0 # nic nie musimy wydać, żeby być na lotnisku startowym
    q = PriorityQueue()
    q.put((0,s)) # (czas,lotnisko)
    while not q.empty():
        time,v = q.get()
        if time>koszt[v]:
            continue
        if v==t:
            return time
        # ewentualne polecenie szybowcem
        for u in range(len_a):
            if koszt[u]>A[v]+A[u]+koszt[v]: # A[v]+A[u] = koszt_odlotu + koszt_przylotu
                koszt[u] = koszt[v] + A[v] + A[u]
                q.put((koszt[u],u))
        # relaksacje normalnie lecąc
        for u,waga in G[v]:
            if koszt[u]>koszt[v]+waga:
                koszt[u] = koszt[v] + waga
                q.put((koszt[u],u))
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )