def can_segment(s, dictionary):
    words = set(dictionary)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                break
    return dp[-1]

def min_segments(s, dictionary):
    words = set(dictionary)
    dp = [float("inf")] * (len(s) + 1)
    dp[0] = 0
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] != float("inf") and s[j:i] in words:
                dp[i] = min(dp[i], dp[j] + 1)
    return None if dp[-1] == float("inf") else dp[-1]

def suggest_spacing(s, dictionary):
    words = set(dictionary)
    dp = [False] * (len(s) + 1)
    parent = [-1] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in words:
                dp[i] = True
                parent[i] = j
                break
    if not dp[-1]:
        return None
    parts = []
    i = len(s)
    while i > 0:
        j = parent[i]
        parts.append(s[j:i])
        i = j
    return " ".join(reversed(parts))

def all_segmentations(s, dictionary):
    words = set(dictionary)
    memo = {}
    def solve(start):
        if start == len(s):
            return [""]
        if start in memo:
            return memo[start]
        result = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words:
                for tail in solve(end):
                    result.append(word if not tail else word + " " + tail)
        memo[start] = result
        return result
    return solve(0)

print("Output =", can_segment("applepenapple", ["apple","pen"]))
