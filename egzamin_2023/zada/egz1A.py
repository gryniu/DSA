from queue import PriorityQueue
from math import inf
from egz1Atesty import runtests

def gold(G,V,s,t,r):
  # tu prosze wpisac wlasna implementacje
  n=len(G) # ilość zamków
  dist = [[inf] * 2 for _ in range(n)]
  dist[s][0] = 0
  dist[s][1] = -V[s]
  q=PriorityQueue()
  q.put((0,s, 0)) # (cost,castle,theft)
  q.put((-V[s],s,1 ))# (cost,castle,theft)
  while not q.empty():
    cost,castle,theft = q.get()
    if dist[castle][theft]<cost:
      continue
    for sasiad,edge_cost  in G[castle]:
      if theft==0:
        # nie kradniemy
        newcost = edge_cost +dist[castle][0]
        if dist[sasiad][0]>newcost:
          dist[sasiad][0] = newcost
          q.put((newcost,sasiad,0))
        #kradniemy
        robb = 2*edge_cost +r+dist[castle][0] - V[castle]
        if dist[sasiad][1]>robb:
          dist[sasiad][1] = robb
          q.put((robb,sasiad,1))
      else:
        newcost = 2*edge_cost +r+dist[castle][1]
        if newcost<dist[sasiad][1]:
          dist[sasiad][1] = newcost
          q.put((newcost,sasiad,1))
  return min(dist[t])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
