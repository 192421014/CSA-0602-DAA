def dice_ways(n, faces, target):
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for d in range(1, n + 1):
        for s in range(1, target + 1):
            for face in range(1, faces + 1):
                if s >= face:
                    dp[d][s] += dp[d - 1][s - face]

    return dp[n][target]

n = 3
faces = 6
target = 12

print("Number of Dice =", n)
print("Faces per Dice =", faces)
print("Target Sum =", target)
print("Number of ways =", dice_ways(n, faces, target))
