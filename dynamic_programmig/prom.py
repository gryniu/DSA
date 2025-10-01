# zadanie
# mamy sobie  prom
# prom ma dwa pasy


# pasy maja dlugosc l (oba)
# pojazdy tez maja jakas dlugosc a1,a2,a3,a4
# kazdy pojaz moze jechac na prawy pas albo na lewy
# n to liczba pojazdów
# l jest naturalne
# a1,a2,a3,a4 tez jest naturalne

# zdefinijmy funkcję
# l - piersze l metrow lewego pasa
# p - pieerwsz p metrow prawego pasa
# k - pierwsze k pojazdow
# f(l,p,k) -  czy da sie upakowac pierwsze k pojazdow, tak aby
# zajac <= l na lewym pasie i <= p na prawym pasie
# wynik zadania to argmax o k nalezace 0,1,...,n f(L,L,k) = True
# zaimplementuj: (kty pojazd wjezdza pierwszy, dziwne bo od konca ale nie ma to znaczenia)
# f(l,p,k)=f(l-ak,p,k-1) or f(l,p-ak,k-1)
# f(l,p,k) = False gdy l<0 or p<0
# f(l,p,0) = True gdy l>=0 i p>=0
def ferry(A,L): # A to tablica z dlugosciami pojazdow a L to jest długość promu
    n = len(A) # ilość aut
    memo = dict()
    def dp(l,p,k): # czy da się pomieścić upakowac k pierwszych pojazdow tak aby zajac <= l na lewym pasie i <= p na prawym pasie
        if (l,p,k) in memo.keys():
            return memo[(l,p,k)]
        if l<0 or p<0:
            res = False
        elif k==-1:# and l>=0 and p>=0
            res = True
        else:
            # jako pierwsze jedzie auto ostatnie, ale to nie ma znaczenia, bo pytanie jest czy upchamy k peirwsszych aut
            res = dp(l-A[k],p,k-1) or dp(l,p-A[k],k-1)# mamy miejsce w lewym lub prawym pasie i mamy auta do upakowania
        memo[(l,p,k)] = res
        return res

    for i in range(n-1,-1,-1):
        if dp(L,L,i):
            return True
    return False
A = [2, 3, 4]
L = 5
print(ferry(A,L))