from egz2btesty import runtests
from math import inf
def parking(X,Y):
  # tu prosze wpisac wlasna implementacje
  n, m = len(X), len(Y)
  memo = {}
  def f(i,j): # minimalna suma odleglosc biurowcow X[0],...,X[i] do przydzielonych im działek przy założeniu że biurowiec z pozycj X[i] ma przydzilona działke z pozycji Y[j]
    if (i,j) in memo:
      return memo[(i,j)]
    res=inf
    if i>j:
      res = inf
    elif i == 0 and j ==0:
      res= abs(X[0]-Y[0])
    elif i == -1:
      res = 0
    else:
      res=min(abs(X[i]-Y[j])+f(i-1,j-1),f(i,j-1))
    memo[(i,j)] = res
    return res

  return f(n-1,m-1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
