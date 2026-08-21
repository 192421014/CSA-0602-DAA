"""Brute Force String Matching - Q10: Full program with complexity analysis."""


def brute_force_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []
    total_comparisons = 0

    for i in range(n - m + 1):
        j = 0
        print(f"Shift {i}: aligning pattern with text[{i}:{i + m}] = "
              f"'{text[i:i + m]}'")
        while j < m:
            total_comparisons += 1
            if text[i + j] != pattern[j]:
                print(f"   Mismatch at pattern[{j}] = '{pattern[j]}' "
                      f"vs text[{i + j}] = '{text[i + j]}'")
                break
            j += 1
        if j == m:
            print("   Full match found!")
            positions.append(i)

    return positions, total_comparisons


if __name__ == "__main__":
    text = "TTATAGATCTCGTATTCTTTATAGATCTCCTATTCTT"
    pattern = "TATCTT"

    positions, comparisons = brute_force_string_match(text, pattern)

    print()
    print(f"All occurrences of the pattern: {positions}")
    print(f"Total comparisons: {comparisons}")
    print()

    n = len(text)
    m = len(pattern)
    print("Complexity Analysis:")
    print(f"Best-case complexity : O(n)   -> each alignment mismatches on the "
          f"first character comparison")
    print(f"Worst-case complexity: O(n*m) -> up to {n - m + 1} alignments each "
          f"needing up to {m} comparisons (highly repetitive text/pattern)")
    print(f"Space complexity     : O(1)   -> no extra space is used besides "
          f"the input text and pattern")
