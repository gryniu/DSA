from zad8testy import runtests
from math import inf


def plan(T):
    # tu prosze wpisac wlasna implementacje
    m, n = len(T[0]), len(T)
    visited = set()
    plamki = [0] * m

    def dfs(i, j, visited, stala):
        for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            ni, nj = i + x, j + y
            if 0 <= ni < n and 0 <= nj < m and (ni, nj) not in visited and T[ni][nj] > 0:
                visited.add((ni, nj))
                plamki[stala] += T[ni][nj]
                dfs(ni, nj, visited, stala)

    for j in range(m):
        if T[0][j] > 0 and (0, j) not in visited:  # obchodzi nas tylo pierwszy indeks
            visited.add((0, j))
            plamki[j] = T[0][j]
            dfs(0, j, visited, j)
    memo = {}

    # for wiersz in T:
    #     print(wiersz)
    # print()
    # print(plamki)
    def dp(i, fuel):
        if (i, fuel) in memo.keys():
            return memo[(i, fuel)]
        if fuel < 0:
            res = inf
        elif i == m - 1:
            res = 0
        else:
            res = dp(i + 1, fuel - 1)
            if plamki[i] > 0:
                res = min(res, 1 + dp(i + 1, fuel + plamki[i] - 1))
        memo[(i,fuel)] = res
        return res
    return dp(0,0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
