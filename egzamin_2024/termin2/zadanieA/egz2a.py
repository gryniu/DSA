from egz2atesty import runtests
from math import inf

def wired(T):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    memo = {}

    def f(l,r):
        if (l,r) in memo:
            return memo[(l,r)]
        res = inf
        if l>=r:
            res=0
        elif r-l==1:
            res=1+abs(T[l]-T[r])
        else:
            for i in range(l+1,r+1,2):
                res=min(res,f(l+1,i-1)+1+abs(T[l]-T[i])+f(i+1,r))
        memo[(l,r)] = res
        return res


    return f(0,n-1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wired, all_tests=True)
