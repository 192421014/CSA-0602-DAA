"""
Topic 3 - Q11
Find whether a subset exists with a given sum using exhaustive search.
"""

from itertools import combinations


def subset_sum_exhaustive(nums, target):
    n = len(nums)
    for r in range(1, n + 1):
        for combo in combinations(nums, r):
            if sum(combo) == target:
                return list(combo)
    return None


if __name__ == "__main__":
    nums = [3, 34, 4, 12, 5, 2]
    target = 9

    result = subset_sum_exhaustive(nums, target)

    if result:
        print(f"Subset found: {result}")
        print(f"Sum: {sum(result)}")
    else:
        print("No subset with the given sum exists.")
