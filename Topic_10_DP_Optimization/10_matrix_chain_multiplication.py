def matrix_chain(arr):
    n=len(arr)
    dp=[[0]*n for _ in range(n)]
    for L in range(2,n):
        for i in range(1,n-L+1):
            j=i+L-1
            dp[i][j]=float("inf")
            for k in range(i,j):
                q=dp[i][k]+dp[k+1][j]+arr[i-1]*arr[k]*arr[j]
                dp[i][j]=min(dp[i][j],q)
    return dp[1][n-1]

print("Minimum Multiplications =",matrix_chain([10,20,30,40,30]))
