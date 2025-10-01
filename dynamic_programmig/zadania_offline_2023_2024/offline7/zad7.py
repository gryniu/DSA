from zad7testy import runtests
from math import inf


def maze(L):
    n = len(L)
    directions = [(1, 0), (-1, 0), (0, 1)]

    #             dol   gora   prawo
    memo = {}

    def f(i, j, fromm):
        if not (0 <= i < n and 0 <= j < n) or L[i][j] == '#':
            return -inf
        if (i, j, fromm) in memo:
            return memo[(i, j, fromm)]
        if i==n-1 and j==n-1:return 0
        res = -inf
        for idx, dir in enumerate(directions):
            if (fromm==1 and idx==0) or (fromm==0 and idx==1):
                continue
            new_i, new_j = i + dir[0], j + dir[1]
            res = max(res, 1+f(new_i, new_j, idx))
        memo[(i, j, fromm)] = res
        return res



    global_res = f(0,0,2)
    return global_res if global_res>0 else -1
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maze, all_tests=True)
