# sum of subset
# mamy jakiś ciag A0, A1, A2, A3,....,An-2,An-1
# dzielimy ten ciąg na k zwartych podciągów o randomowych długościach
# sumujemy elementy w tych podciągach
# wartością tego podziału jest najmniejsza suma jakiegos pododizalu
# to ma byc najwieksze

# algorytm dynamiczny
# definiujemy stan
# tutaj jest stanem
# gdzie dzielimy - start, koniec i na ile dzielimy
# funkcja
# minmax(k,i,j) - wartosc najlepszego podzialu przedzialu (i,j) na k podciągów


# ZAIMPLEMENTOWAĆ W DOMU !!!
def minmax(A, k):
    n = len(A)
    memo={}
    prefix=[0]*(n+1)
    for i in range(n):
        prefix[i+1] =prefix[i]+A[i]
    def sum_range(i,j):
        return prefix[j+1]-prefix[i]
    def dp(i,k):
        if (i,k) in memo:
            return memo[(i,k)]
        if k==1:
            return sum_range(i,n-1)
        maxi = -1
        for j in range(i,n-k+1):
            cur_przedzial = sum_range(i,j)
            best_przedzial_dalej = dp(j+1,k-1)
            mini=min(cur_przedzial,best_przedzial_dalej)
            maxi=max(maxi,mini)
        return maxi
    return dp(0,k)
A = [3,7,9,8,2,6,1,3,5]
print(minmax(A,5))
# ZADANIE DODATKOWE - ZROB TABLICE PARENT, ZE W WYNIKU TEZ MA BYC TABLICA TUPLI (i,j) I MIEDZY TYMI INDEXAMI MAMY DAC KRESKE ZEBY PODZIELIC TĄ TABLICE