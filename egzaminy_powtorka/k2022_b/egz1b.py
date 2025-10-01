from egz1btesty import runtests


def get_lvl(node, cur):
    node.x = (cur, -1)
    if node.right:
        get_lvl(node.right, cur + 1)
    if node.left:
        get_lvl(node.left, cur + 1)


def get_max_depth(node):
    if not node:
        return 0
    lvl = node.x[0]
    res = 1 + max(get_max_depth(node.right), get_max_depth(node.left))
    node.x=(lvl,res-1)
    return res


class Node:
    def __init__(self):
        self.left = None  # lewe poddrzewo
        self.right = None  # prawe poddrzewo
        self.x = None  # (poziom, ile mozna zejsc jeszcze na dół)


def wideentall(T):
    # tu prosze wpisac wlasna implementacje
    get_lvl(T, 0)
    get_max_depth(T)
    counter_lvls = [0]*(T.x[1] + 1) # T.x[1] + 1 to ilość lvl-ów
    def counting(node):
        counter_lvls[node.x[0]]+=1
        if node.left:
            counting(node.left)
        if node.right:
            counting(node.right)
    counting(T)
    # lvl ktory bedzie ostatnim
    maxi = max(counter_lvls)
    last_lvl = -1
    for i in range(T.x[1],-1,-1):
        if counter_lvls[i]==maxi:
            last_lvl = i
            break
    def canceling_edges(node):
        res = 0
        if node.x[0]<last_lvl:
            if node.x[1]+node.x[0]<last_lvl:
                res+=1
            else:
                if node.left:
                    res+=canceling_edges(node.left)
                if node.right:
                    res+=canceling_edges(node.right)
        elif node.x[0]==last_lvl:
            if node.left:
                res+=1
            if node.right:
                res+=1
        return res
    return canceling_edges(T)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(wideentall, all_tests=True)