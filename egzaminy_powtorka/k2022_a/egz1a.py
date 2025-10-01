from egz1atesty import runtests
def snow( S ):
    # tu prosze wpisac wlasna implementacje
    memo={}
    n = len(S)
    def dp(i,j,time):
        if (i,j,time) in memo.keys():
            return memo[(i,j,time)]
        if i==j:
            return max(S[i]-time,0)
        if i>j:
            return 0
        # jedziemy z lewej (zachód)
        res = 0
        if S[i]-time>0: # mozna zjesc loda z lewej
            res=max(res,dp(i+1,j,time+1)+S[i]-time)
        res=max(res,dp(i+1,j,time))#nie jemy loda z lewej
        if S[j]-time>0:#mozna zjesc loda z prawej
            res=max(res,dp(i,j-1,time+1)+S[j]-time)
        res=max(res,dp(i,j-1,time))# nie jemy loda z prawej
        return res


    return dp(0,n-1,0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )