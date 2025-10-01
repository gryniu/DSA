"""
mamy jezioro i liscie
na pierwszym lisciu jest zaba
sa tez jakies pozywienia ; e0,e1,e2,...,en (dodajemy do energi)
e sa liczbami naturalnymi, moze tez byc 0 to oznacza ze nie ma pozywienia
mamy koszty skosku; k0,k1,k2,...,kn
ki to ilosc energi zeby skoczyc z itego liscia
nie mozna wykonac skoku na ktory nas nie stac (mamy za malo energi)
moge skakac gdzie chce
WAZNE
jak masz e energi to mozesz przeskoczyc maxymalnie e miast ale zuzywasz tylko k[i] energi bo skaczesz z itego liscia
obojetnie gdzie skoczysz
zad.
chcemy dojsc do konca w jak najmniej skokow


nie czaje polecenia, cos pojebane
bez sensu


PRZEPISANE Z TABLICY:
e - energia po zjedzeniu
i -  lisc do ktorego chcemy skoczyc
f(i,e) - min liczba skokow zeby dostac sie do itego liscia majac energie e

f(i,e) = min dla j nalezacego 0,...,i-1 f(j,e+k[j]), jeśli e+k[j] >= i-j
"""
from math import inf
def lake(E,K,energy):
    n = len(E)
    memo = {}
    def dp(i,e):
        if (i,e) in memo.keys():
            return memo[(i,e)]
        if e<0:
            return inf
        if i==n:
            return 0
        res = inf
        for j in range(i+1,n):
            res = min(res,1+dp(j,e+E[i]-K[i]))
        return res