def rod_cut(price,n):
    dp=[0]*(n+1)
    for i in range(1,n+1):
        for j in range(i):
            dp[i]=max(dp[i],price[j]+dp[i-j-1])
    return dp[n]

print("Maximum Revenue =",rod_cut([1,5,8,9,10,17,17,20],8))
