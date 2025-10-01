"""tu sa tylko napisane polecenia"""
from queue import PriorityQueue

"""algo dijstry"""
"""odtwarzanie najkrotszej sciezki za pomoca tablicy parent"""
"""znalezienie najkrotszej sciezki w dagu"""
"""dlugoscia sciezki jest iloczyn jej wag
zaproponowac jak najlepszy algorytm znajdujacy najszybsze sciezki
kom
trzeba zamienic te wagi na logarytmy zeby nas nie wyjebalo poza zakres inta
i robimy dijkstre
a jak wagi ujemne to bellman ford"""

"""zadanie 5
przewodnik turystyczny
jest graf gdzie jest wyznaczone sa miast s i t 
sa krawedzie odpowaidajace liniami autobusowymi miedzy mieastami, wagi to ile oosb mozna przewiezc z miast a do b
zadanie to przewiezc jak najwiecej osob z s do t

najwieksza minimalna waga

rozwiazanie
MAKSYMALNE DRZEWO ROZPINAJACE
1. umieszczamy w kolejce prioryteteowej typu max(sortujemy krawedzie)
2. union find - procedura
3. sciagamy maksymalna krawedz
umax vmax
waga maksymalna jest pamietana

2 sposob
dijkstra tylko odwrotnie updatujemy
"""
"""
zadanie 6
mamy jakies miasto s i t
sa tam jakies krawedzie i wierzcholki, wagi krawedzie to ilosc kilometrow
w kazdym miejscu jest stacja paliwowa, i w miescie sa ceny za paliwo
samochod pali 1l/1km, pojemnosc baku D
interesuje nas najtansza trasa z s do t
tankujemy ile chcemy ale nie wiecej niz pojemnosc baku
"""
"""
zadanie 7
zadanie dwoch kierowncow (A i B, Alicja i Bob)
jedziemy z miasta s do miasta t, sa jakies odleglosci miedzy mieastami, jako waga grafu
bob chce jechac jak najmniej
zamieniaja sie co kazda stacje
"""
"""
zadanie 8
chcemy znalezc najkrotsza sciezke przebiegajaca po 
krawedziach o malejacych wagach
"""


# zadanie 6 MIASTA
# algo dijkstra
def najtansza_trasa(graph, s, t, D, ceny):
    n = len(graph)

    return -1  # nie da się dojechać

graf = [
    [(1, 4), (2, 6)],  # miasto 0
    [(0, 4), (2, 1)],  # miasto 1
    [(0, 6), (1, 1)]   # miasto 2
]
ceny = [5, 2, 4]
D = 5
s = 0
t = 2

print(najtansza_trasa(graf, s, t, D, ceny))  # Oczekiwany wynik: 22
