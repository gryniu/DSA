# sprawdzanie cyklu eulera graf SKIEROWANY, macierz adjencji


def in_out(adj_matrix):
    n = len(adj_matrix)
    stack = [0]
    in_counter = [0] * n
    out_counter = [0] * n
    visited = [False]*n
    visited[0]=True
    while stack:
        v=stack.pop()
        for u in range(n):
            if adj_matrix[v][u]==1 and not visited[u]:
                out_counter[v]+=1
                in_counter[u]+=1
                stack.append(u)
                visited[u]=True
    print(in_counter)
    print(out_counter)
    for i in range(n):
        if in_counter[i]!=out_counter[i]:
            return False
    return True
def finding_euler_cycle(adj_matrix):
    n=len(adj_matrix)
    # if not in_out(adj_matrix) or n==0:
    #     return None
    tmp_matrix=[row[:] for row in adj_matrix]
    path=[]
    visited=[False]*n
    def dfs(tmp_matrix,v):
        visited[v]=True
        for u in range(n):
            if tmp_matrix[v][u]==1:
                tmp_matrix[v][u]-=1
                dfs(tmp_matrix,u)
        path.append(v)
    dfs(tmp_matrix,0)
    return path
adj = [
    [0, 1, 1, 0],  # 0 → 1, 0 → 2
    [0, 0, 1, 1],  # 1 → 2, 1 → 3
    [1, 0, 0, 1],  # 2 → 0, 2 → 3
    [1, 1, 0, 0]   # 3 → 0, 3 → 1
]
print(finding_euler_cycle(adj))
#zle zrobione