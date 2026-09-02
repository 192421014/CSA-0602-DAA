def min_cost(cost):
    m,n=len(cost),len(cost[0])
    dp=[[0]*n for _ in range(m)]
    dp[0][0]=cost[0][0]
    for i in range(1,m): dp[i][0]=dp[i-1][0]+cost[i][0]
    for j in range(1,n): dp[0][j]=dp[0][j-1]+cost[0][j]
    for i in range(1,m):
        for j in range(1,n):
            dp[i][j]=cost[i][j]+min(dp[i-1][j],dp[i][j-1])
    return dp[-1][-1]

print("Minimum Cost =",min_cost([[1,3,1],[1,5,1],[4,2,1]]))
