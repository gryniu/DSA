from egz3btesty import runtests
from math import inf


# def is_cool(i1, j1, i2, j2):
#     if i1 >= i2 and j1 <= j2: return True  # 1 zawiera się w dwa
#     if i2 >= i1 and j2 <= j1: return True  # 2 zawiera się w dwa
#     if j1<i2 or j2<i1: return True # nie zawierają się wgl
#     return False # są nie cool
#

def uncool(P):
    indexed = list(enumerate(P))
    # Sortujemy po początku przedziału
    indexed.sort(key=lambda x: (x[1][0], -x[1][1]))  # sortujemy po a rosnąco, b malejąco

    max_b = indexed[0][1][1]
    max_b_index = indexed[0][0]

    for i in range(1,len(P)):
        idx,(a,b)=indexed[i]
        if a<=max_b: # przecinaja sie
            if b>max_b:
                return (max_b_index,idx)
        else:
            max_b_index=idx
            max_b=b
    return (-1,-1)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(uncool, all_tests=True)
