# O(mn)
from zad6testy import runtests
from math import inf


def parking(X, Y):
    # tu prosze wpisac wlasna implementacje
    n = len(X) # ilość wierzowców
    m = len(Y) # ilość dostępnych parkingów
    memo={}
    def f(i,j):
        if (i,j) in memo.keys():
            return memo[(i,j)]
        if i==0 and j == 0:
            res = abs(X[0]-Y[0])
        elif i>=0 and j<0: # nie mamy zadnego parkingu do przydzielenie
            res = inf
        elif i<0 and j >= 0:
            res = 0
        else:
            # (wybieramy ten wierzowiec, nie wybieramy tego wierzowca)
            res = min(f(i-1,j-1)+abs(X[i]-Y[j]),f(i,j-1))
        memo[(i,j)] = res
        return res

    return f(n-1,m-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(parking, all_tests=True)