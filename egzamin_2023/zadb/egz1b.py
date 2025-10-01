from egz1btesty import runtests
from math import inf


def planets(D, C, T, E):
    # tu prosze wpisac wlasna implementacje
    n = len(D)  # ilosc planet
    f = [[inf] * (E + 1) for _ in
         range(n)]  # f[i][b] = minimalny koszt ZNALEZIENIA SIE na planecie i mając b ton paliwa
    for b in range(E + 1):
        f[0][b] = b * C[0]
    if T[0][0] != 0:
        f[T[0][0]][0] = T[0][1]
    for i in range(1, n):
        distance = D[i] - D[i - 1]
        for b in range(E + 1 - distance):
            f[i][b] = min(f[i][b], f[i - 1][b + distance])
        # tankowanie
        for b in range(1, E + 1):
            f[i][b] = min(f[i][b], f[i][b - 1] + C[i])
        if T[i][0] != i:
            f[T[i][0]][0] = min(f[T[i][0]][0],f[i][0] + T[i][1])

    return min(f[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(planets, all_tests=True)
