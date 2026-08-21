"""Brute Force String Matching - Q7: Case-insensitive searching."""


def brute_force_case_insensitive(text, pattern):
    text_lower = text.lower()
    pattern_lower = pattern.lower()

    n = len(text_lower)
    m = len(pattern_lower)

    for i in range(n - m + 1):
        j = 0
        while j < m and text_lower[i + j] == pattern_lower[j]:
            j += 1
        if j == m:
            return i

    return -1


if __name__ == "__main__":
    text = "DataStructuresAndAlgorithms"
    pattern = "ALGORITHMS"

    position = brute_force_case_insensitive(text, pattern)

    if position != -1:
        print(f"Pattern found position: {position}")
    else:
        print("Pattern not found")
