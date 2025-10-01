from math import inf
from kol2btesty import runtests


def min_cost(O, C, T, L):
    # Dodajemy miasta A i B jako parkingi z kosztem 0
    O.append(0)
    C.append(0)
    O.append(L)
    C.append(0)

    parkings = sorted(zip(O, C), key=lambda x: x[0])
    n = len(parkings)
    dp =[[inf]*2 for _ in range(n)] # dp[i][j] najmniejszy mozliwy koszt do przejechania do miasta i j t czy byl wyjatek czynie
    dp[0][0] = 0 # z A koszt jest  0
    for i in range(n):
        for j in range(i+1,n): #  probujemy dojechac jak najdalej z miejsca i
            distance = parkings[j][0]-parkings[i][0]
            cost_j = parkings[j][1]
            if distance<=T:
                dp[j][0]=min(dp[j][0],dp[i][0]+cost_j) # parkujemy w j zawsze
                dp[j][1] = min(dp[j][1], dp[i][1] + cost_j)
            elif distance<=2*T:
                dp[j][1] = min(dp[j][1], dp[i][0] + cost_j)
            else:
                break


    return min(dp[n - 1][0], dp[n - 1][1])
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(min_cost, all_tests=True)
