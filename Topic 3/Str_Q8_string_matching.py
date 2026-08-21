"""Brute Force String Matching - Q8: Successful vs unsuccessful search."""


def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    total_comparisons = 0
    position = -1

    for i in range(n - m + 1):
        j = 0
        while j < m:
            total_comparisons += 1
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            position = i
            break

    return position, total_comparisons


if __name__ == "__main__":
    text = "PROGRAMMINGLAB"
    pattern1 = "LAB"
    pattern2 = "TEST"

    pos1, comp1 = brute_force_string_match(text, pattern1)
    pos2, comp2 = brute_force_string_match(text, pattern2)

    print("Successful Search:")
    print(f"Pattern '{pattern1}' found at position: {pos1}")
    print(f"Comparison count = {comp1}")
    print()

    print("Unsuccessful Search:")
    print(f"Pattern '{pattern2}' found at position: {pos2}")
    print(f"Comparison count = {comp2}")
