def min_wrap_cost(words, width):
    n = len(words)
    dp = [float("inf")] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        length = 0
        for j in range(i, n):
            length += words[j]
            if j > i:
                length += 1
            if length > width:
                break
            extra = width - length
            cost = 0 if j == n - 1 else extra * extra
            dp[i] = min(dp[i], cost + dp[j + 1])
    return dp[0]

def wrap_lines(words, width):
    n = len(words)
    dp = [float("inf")] * (n + 1)
    parent = [-1] * (n + 1)
    dp[n] = 0
    for i in range(n - 1, -1, -1):
        length = 0
        for j in range(i, n):
            length += words[j]
            if j > i:
                length += 1
            if length > width:
                break
            extra = width - length
            cost = 0 if j == n - 1 else extra * extra
            if cost + dp[j + 1] < dp[i]:
                dp[i] = cost + dp[j + 1]
                parent[i] = j + 1
    result = []
    i = 0
    while i < n:
        j = parent[i]
        result.append(words[i:j])
        i = j
    return result

def greedy_wrap_cost(words, width):
    cost = 0
    length = 0
    for i, word in enumerate(words):
        if length == 0:
            length = word
        elif length + 1 + word <= width:
            length += 1 + word
        else:
            cost += (width - length) ** 2
            length = word
    return cost

words = [3, 2, 2, 5]
width = 6
print("Minimum Cost =", min_wrap_cost(words, width))
