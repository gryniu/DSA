from kol3testy import runtests
from math import inf

def orchard(T, m):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    cur_sum = sum(T)
    memo = {}
    # rekurencja z memoizacją
    def f(i,cur_sum):
        if (i,cur_sum) in memo.keys():
            return memo[(i,cur_sum)]
        # warunki brzegowe
        if cur_sum%m==0:
            res = 0
        elif i==0 and cur_sum%m!=0:
            res = inf
        else:
            res = min(f(i-1,(cur_sum-T[i])%m)+1,f(i-1,cur_sum%m))
        memo[(i,cur_sum)] = res
        return res
    return f(n-1,cur_sum%m)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)