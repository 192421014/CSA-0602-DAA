"""
Experiment 6: Merge Sort
Objective: Analyze divide-and-conquer sorting.
Complexity: Always O(n log n)
"""

import time


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]

    start = time.perf_counter()
    sorted_arr = merge_sort(arr)
    end = time.perf_counter()

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Time Complexity: O(n log n) in the best, average, and worst cases")
    print("Space Complexity: O(n) -> extra arrays used for merging")
    print("Explanation: The array is always split in half regardless of "
          "input order, giving guaranteed O(n log n) performance.")
