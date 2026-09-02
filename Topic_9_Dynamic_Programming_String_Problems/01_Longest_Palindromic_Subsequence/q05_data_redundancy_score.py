def lps_length(s):
    n = len(s)
    if n == 0:
        return 0
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 if length == 2 else dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

def palindrome_score(s):
    return lps_length(s)

def symmetry_ratio(s):
    return 0 if not s else lps_length(s) / len(s)

def base_pair_estimate(s):
    return lps_length(s) // 2

def is_compression_candidate(s):
    return lps_length(s) - len(s) / 2 > 0

def reconstruct_lps(s):
    n = len(s)
    if not s:
        return ""
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 if length == 2 else dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    i, j = 0, n - 1
    left, right = [], []
    while i <= j:
        if i == j:
            left.append(s[i])
            break
        if s[i] == s[j]:
            left.append(s[i]); right.append(s[j])
            i += 1; j -= 1
        elif dp[i + 1][j] >= dp[i][j - 1]:
            i += 1
        else:
            j -= 1
    return "".join(left + right[::-1])

def lps_length_optimized(s):
    n = len(s)
    prev = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        curr = [0] * (n + 1)
        curr[i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                curr[j] = prev[j - 1] + 2
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev = curr
    return prev[n - 1] if n else 0

def is_weak_password(password, threshold=0.6):
    return bool(password) and lps_length_optimized(password) / len(password) > threshold

s = "bbbab"
print("Input =", s)
print("Output =", result)
