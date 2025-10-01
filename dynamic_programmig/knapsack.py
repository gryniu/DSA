# Masz do dyspozycji n przedmiotów. Każdy przedmiot i (dla 0 ≤ i < n) ma:
# wartość P[i] — liczba całkowita dodatnia
# wagę W[i] — liczba całkowita dodatnia
# Dysponujesz plecakiem o maksymalnej pojemności B (liczba całkowita dodatnia). Celem jest wybranie takich przedmiotów, aby:
# łączna waga wybranych przedmiotów nie przekroczyła B
# łączna wartość wybranych przedmiotów była jak największa
# Każdy przedmiot można wybrać co najwyżej raz (czyli: bierzemy go w całości lub wcale).
def knapsack(B, P, W):
    n = len(P)
    F = [[0] * (B + 1) for _ in
         range(n)]  # F[i][b] maksymalna wartosc przedmiotów z zakresu 0,...,i o plecaku o maksymalnej pojemnosci b
    for b in range(W[0], B + 1):
        F[0][b] = P[0]
    for i in range(1, n):
        for b in range(B + 1):
            # nie bierzemy tej rzeczy
            F[i][b] = F[i - 1][b]
            # bierzemy tą rzecz
            if W[i] <= b:
                F[i][b] = max(F[i][b], F[i - 1][b - W[i]] + P[i])
    return F[-1][-1]


# rozwiązanie rekurencyjne z memoizacją
memo = {}  # stany to będą: (ilość miejsca w plecaku,i)


def knapsack_rec(B, P, W, i):  # i odpowieada za to ze bierzemy przedmiotu 0,...,i włącznie
    # warunki brzegowe
    if (B,i) in memo:
        return memo[(B,i)]
    res=None
    if i == 0:  # bierzemy tylko przedmiot i
        res = P[i] if W[i]<=B else 0
    elif W[i] <= B:
        res1=knapsack_rec(B - W[i], P, W, i - 1)+P[i] # bierzemy ten przedmiot - czyli to zmniejszamy przepustowosc plecaka a kasa to kasa z ..i-1 +P[i]
        res2=knapsack_rec(B, P, W, i - 1) # nie bierzemy
        res = max(res1, res2)
    else:  # nie możemy wziąć tego przedmiotu
        res =  knapsack_rec(B, P, W, i - 1)
    memo[(B,i)] = res
    return res



B = 7
P = [16, 19, 23, 28]
W = [2, 3, 4, 5]
print(knapsack(B, P, W))
print(knapsack_rec(B,P,W,len(P)-1))