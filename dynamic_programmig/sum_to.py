# czy da sie posumowac tak jakies liczby korzystajca z kazdej tylko raz do sumy t
from math import inf
mem = dict()
def s_sum_rec(t,i,A):
    if (t,i) in mem:
        return mem[(t,i)]
    result = None
    if t==0:
        result = True
    elif t>0 and i<0:
        result = False
    elif t<0:
        result = False
    else:
        result = s_sum_rec(t-A[i],i-1,A) or s_sum_rec(t,i-1,A) # najpierwsz korzystamy z tej liczby, czyli t się zmniejsza or nie korzystamy z tej liczby
    mem[(t,i)] =result
    return result
def s_sum_iter(A,T):
    n = len(A)
    dp = [[False]*n for _ in range(T+1)]
    for i in range(n):
        dp[0][i]=True
    for t in range(1,T+1):
        for i in range(1,n):
            dp[t][i] = dp[t][i-1] or (dp[t-A[i][i-1] if t-A[i]>=0 else False])
A = [8,7,9,1,16,31,5]
T=22
print(s_sum(A,T))