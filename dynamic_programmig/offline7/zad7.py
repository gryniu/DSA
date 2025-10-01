from zad7testy import runtests
from math import inf

def orchard(T, m):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    memo = {}
    def dp(i,cur_sum): # (gdzie jesteśmy, ile mamy jabłek)
        if (i,cur_sum) in memo.keys():
            return memo[(i,cur_sum)]
        if i==n:
            return 0 if cur_sum%m==0 else inf
        res = min(1+dp(i+1,cur_sum),dp(i+1,(cur_sum+T[i])%m)) # (wycinamy, nie wycinamy)
        memo[(i,cur_sum)] = res
        return res

    return dp(0,0)
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True) 