# graf w postaci macierzowej
# jak zlinearizować tablice
#zadanie
#napisac funkcje czy istnieje cykl Eulera
def cyklEulera(G):
    n = len(G)
    index=[0]*n
    def dfsvisit(G,u):
        while index[u]<n:
            v=index[u]
            index[u]=v+1
            if G[u][v]:
                G[u][v]=G[v][u]=0




