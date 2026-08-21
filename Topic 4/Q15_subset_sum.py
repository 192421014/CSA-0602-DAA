"""
Topic 3 - Q15
Solve the subset sum problem by generating all possible subsets and
checking their sums.
"""

from itertools import combinations


def subset_sum_all_subsets(nums, target):
    n = len(nums)
    for r in range(1, n + 1):
        for combo in combinations(nums, r):
            if sum(combo) == target:
                return list(combo)
    return None


if __name__ == "__main__":
    nums = [15, 10, 12, 7, 5]
    target = 22

    result = subset_sum_all_subsets(nums, target)

    if result:
        print(f"Subset found: {result}")
        print(f"Sum: {sum(result)}")
    else:
        print("No subset with the given sum exists.")
