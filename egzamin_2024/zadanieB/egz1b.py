from egz1btesty import runtests
from math import inf


def kstrong(T, k):
    # tu prosze wpisac wlasna implementacje
    n = len(T)
    memo = {}

    # started == 0, nie wystartowaliśmy, started == 1 wystartowalimsy, started == 2 zakonczylismy juz nasz podciąg - nie mozna wystartowac jeszcze raz
    def dp(i, started, k_local):
        if (i, started, k_local) in memo:
            return memo[(i, started, k_local)]
        # warunki brzegowe
        res = -inf
        if i == n and started == 1:
            res = 0
        elif i == n and started == 0:
            res = -inf
        elif started == 2:
            return 0
        elif started == 0:  # nie zaczelismy naszego podciagu
            res = max(res, T[i] + dp(i + 1, 1, 0)) # zaczynamy podciąg
            res=max(res,dp(i+1,0,0))# nie zaczynamy

        elif started == 1: # podciag wystartowany
            res = max(res, T[i] + dp(i + 1, 1, k_local))  # kontynuacja
            if k_local < k:
                res = max(res, dp(i + 1, 1,
                                  k_local + 1))  # usuniecie danego elementu (k_local+=1) ale dalje kontyunowanie podciągu
            res = max(res, dp(i+1,2,k_local))  # przerwanie naszego podciągu
        memo[(i,started,k_local)] = res
        return res

    return dp(0,0,0)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)
