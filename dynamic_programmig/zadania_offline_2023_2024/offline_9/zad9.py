from zad9testy import runtests
from math import inf
def trip(M):
  # tu prosze wpisac wlasna implementacje
  m=len(M[0])
  n=len(M)
  memo = {}
  directins=[(1,0),(-1,0),(0,1),(0,-1)]
  def f(i,j):
    if (i,j) in memo.keys():
      return memo[(i,j)]

    res=1
    for x,y in directins:
      ni,nj=i+x,j+y
      if 0<=ni<n and 0<=nj<m and M[ni][nj]>M[i][j]:
        res=max(res,1+f(ni,nj))
    memo[(i,j)] = res
    return res
  res_global=-inf
  for i in range(n):
    for j in range(m):
      res_global=max(res_global,f(i,j))
  return res_global
# M = [ [7,6,5,12],
# [8,3,4,11],
# [9,1,2,10] ]
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( trip, all_tests = True )
# print(trip(M))