"""Brute Force String Matching - Q9: Display every alignment of pattern with text."""


def brute_force_all_alignments(text, pattern):
    n = len(text)
    m = len(pattern)
    positions = []

    for i in range(n - m + 1):
        window = text[i:i + m]
        j = 0
        while j < m and text[i + j] == pattern[j]:
            j += 1
        result = "Match" if j == m else "Mismatch"

        print(f"Alignment {i + 1}: text[{i}:{i + m}] = '{window}'  vs  "
              f"pattern = '{pattern}'  ->  {result}")

        if j == m:
            positions.append(i)

    return positions


if __name__ == "__main__":
    text = "ABCDABCABCDA"
    pattern = "ABCDA"

    positions = brute_force_all_alignments(text, pattern)

    print()
    print(f"Pattern occurrence positions: {positions}")
