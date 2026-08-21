"""Brute Force String Matching - Q5: Determine best/average/worst case."""


def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    total_comparisons = 0
    comparisons_per_alignment = []

    for i in range(n - m + 1):
        j = 0
        comparisons = 0
        while j < m:
            comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        total_comparisons += comparisons
        comparisons_per_alignment.append(comparisons)
        if j == m:
            positions.append(i)

    return positions, total_comparisons, comparisons_per_alignment


if __name__ == "__main__":
    text = "AAAAAAAAAB"
    pattern = "AAAAB"

    positions, total_comparisons, per_alignment = brute_force_string_match(text, pattern)

    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Pattern found at position(s): {positions}")
    print(f"Comparisons at each alignment: {per_alignment}")
    print(f"Total number of comparisons: {total_comparisons}")

    m = len(pattern)
    max_possible = m * (len(text) - m + 1)
    if total_comparisons == max_possible:
        case = "Worst Case (almost every alignment matches m-1 characters before failing)"
    elif total_comparisons == (len(text) - m + 1):
        case = "Best Case (every alignment fails on the very first comparison)"
    else:
        case = "Average Case"

    print(f"This run represents the: {case}")
