# tresc nieznana
# zrob najpierw dp
# jak tankujemy to do pełna
# mamy ograniczenie baku
# nie mozemy uzywac DP
# jak dojechac do konca jak najtaniej
# zrobienie to grafami - dijkstrą, a nie dp

# do zrobienia
from math import inf
from queue import PriorityQueue
def cheapest(L,costs,posx):
    n=len(costs)
    arr = [[inf]*L for _ in range(n)]
    # wierzcholki to ile zostalo pojemnosci baku, gdzie jestem
    G = [[]*n]
    # reprezentacja listowa
    # zle
    for i in range(n):
        arr=[]
        for j in range(n):
            if i!=j:
                arr.append((j,abs(posx[i]-posx[j])))
        G.append(arr)
    return G # robie ten graf
L = 50
posx = [0,20, 40, 60, 70]
costs = [2,7, 3, 2, 5]
print(cheapest(L,costs,posx))
# rozwiazanie dynamiczne
# f(stacja, paliwo) najtaniej zeby dojechac do tej stacji z takim paliwem
memo = {}
def f(i,x):
    if (i,x) in memo.keys():
        return memo[(i,x)]

    res = min(f(i-1,x),f(i-1,x-abs(posx[i]-posx[i-1])))

# wersja zadania - mozemy tankowac max do pelna ale nie musimy do pelna - algorytm zachłanny
# znajdujemy pierwsza stacje ktora jest tansza, tankujemy zeby dojechac do niej i byc tam na 0 i jest gitara
# jak nie ma stacji ktora jest tansza to tankujemy do pełna i jedziemy jak najdalej
# O(n2) to jest
# da sie O(nlogn) za pomocą PriorityQueue