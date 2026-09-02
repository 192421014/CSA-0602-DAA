def tsp_dp(graph):
    n=len(graph)
    dp=[[float("inf")]*n for _ in range(1<<n)]
    dp[1][0]=0
    for mask in range(1<<n):
        for u in range(n):
            if mask&(1<<u):
                for v in range(n):
                    if not mask&(1<<v):
                        dp[mask|(1<<v)][v]=min(dp[mask|(1<<v)][v],dp[mask][u]+graph[u][v])
    return min(dp[(1<<n)-1][i]+graph[i][0] for i in range(1,n))

g=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
print("Minimum Cost =",tsp_dp(g))
