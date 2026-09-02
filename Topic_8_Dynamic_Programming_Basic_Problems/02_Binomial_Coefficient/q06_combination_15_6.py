def binomial(n, r):
    dp = [[0] * (r + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = 1
    for i in range(1, n + 1):
        for j in range(1, min(i, r) + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
    return dp[n][r]

n, r = 15, 6
print("n =", n)
print("r =", r)
print("C(15,6) =", binomial(n, r))
