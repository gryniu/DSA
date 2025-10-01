def pathh(parent,k):
    path=[k]
    while parent[k]!=None:
        path.append(parent[k])
        k=parent[k]
    return parent[::-1]