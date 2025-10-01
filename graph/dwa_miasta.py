from math import inf
from queue import PriorityQueue

"""
zadanie 6
mamy jakies miasto s i t
sa tam jakies krawedzie i wierzcholki, wagi krawedzie to ilosc kilometrow
w kazdym miejscu jest stacja paliwowa, i w miescie sa ceny za paliwo
samochod pali 1l/1km, pojemnosc baku D
interesuje nas najtansza trasa z s do t
tankujemy ile chcemy ale nie wiecej niz pojemnosc baku
"""


# zadanie 6 MIASTA
# algo dijkstra
def najtansza_trasa(G, s, t, D, ceny):
    n = len(G)
    koszt = [[inf] * (D + 1) for _ in range(
        n)]  # koszt[v][ilosc_paliwa], to jest najtańszy koszt na dojechanie do miasta v z taką ilośćią paliwa
    koszt[s][0] = 0
    q = PriorityQueue()
    q.put((0, s, 0))  # (cena,miasto,ilosc_paliwa)
    while not q.empty():
        c, v, paliwo = q.get()
        if v == t:
            return c  # zwracamy ile trzeba najmniej kasy wydać, żeby dojechać
        if c > koszt[v][paliwo]:
            continue
        # 1 - Tankowanie
        for i in range(1, D - paliwo + 1):
            nowy_koszt = c + i * ceny[v]
            if nowy_koszt < koszt[v][paliwo + i]:
                koszt[v][paliwo + i] = nowy_koszt
                q.put((nowy_koszt,v,paliwo+i))

        # 2 - Przemieszczanie się do innych miast
        for u, km in G[v]:
            if paliwo >= km:
                if c < koszt[u][paliwo - km]:
                    koszt[u][paliwo - km] = c
                    q.put((c, u, paliwo - km))

    return -1  # nie da się dojechać


G = [
    [(1, 4), (2, 6)],  # miasto 0
    [(0, 4), (2, 1)],  # miasto 1
    [(0, 6), (1, 1)]  # miasto 2
]
ceny = [5, 2, 4]
D = 5
s = 0
t = 2

print(najtansza_trasa(G, s, t, D, ceny))
