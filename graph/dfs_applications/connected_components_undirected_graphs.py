#znajdowanie spojnych skladowych w grafach skierowanych, graf w reprezentacji macierzy adjencji
def finding_connected_compontents(adj_matrix):
    n=len(adj_matrix)
    def dfs(visited,v):
        component = []
        