def min_coins(coins,amount):
    dp=[float("inf")]*(amount+1)
    dp[0]=0
    for i in range(1,amount+1):
        for c in coins:
            if c<=i: dp[i]=min(dp[i],dp[i-c]+1)
    return dp[amount]

print("Minimum Coins =",min_coins([1,2,5],11))
