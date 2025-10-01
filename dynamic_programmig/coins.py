# wydaj najmniejsza ilosc monet
# musimy wydać t
# mamy zakres M monet
# lm_rec(t) = min lm_rec(t-m)+1
#
from math import inf

memory = dict()


# roziązanie rekurencyjne z memoizacją
def lm_rec(t, M):
    # warunki brzegowe
    if t in memory.keys():
        return memory[t]  # mamy już zapisane ile w najmniej monet można wydać t kasy
    res = None
    if t < 0:
        res = inf  # przekroczyliśmy limit
    elif t == 0:  # żeby wydać 0 pieniedzy trzeba minimalnie dac 0 monet
        res = 0
    else: # t>0
        res = inf
        for m in M:
            res = min(res,lm_rec(t-m,M) + 1) # sprawdzamy wydanie tej monety z aktualnym res
    memory[t] = res
    return res


def lm_iter(t, M):
    n = t + 1
    min_monet = [inf] * n  # [0,1,1,1,1]
    min_monet[0] = 0
    for i in range(1, n):
        for m in M:
            if i - m >= 0:  # chcemy wydac i monet, takze jak i -m >=0 to mozemy uzyc m
                if min_monet[i] > min_monet[i - m] + 1:
                    min_monet[i] = min_monet[i - m] + 1
    return min_monet[t]


t = 12
M = [1, 4, 5]
print(lm_rec(t, M))
