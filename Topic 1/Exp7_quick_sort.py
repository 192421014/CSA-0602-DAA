"""
Experiment 7: Quick Sort
Objective: Analyze recursive quick sort.
Complexity: Omega = O(n log n), Big-O = O(n^2), Theta = Theta(n log n)
"""

import time


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]

    start = time.perf_counter()
    sorted_arr = quick_sort(arr)
    end = time.perf_counter()

    print(f"Original array: {arr}")
    print(f"Sorted array: {sorted_arr}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Omega (best case)  : O(n log n) -> balanced partitions each time")
    print("Big-O (worst case) : O(n^2)     -> already sorted/reverse-sorted "
          "input with a poor pivot choice")
    print("Theta (average case): Theta(n log n) -> random pivots give "
          "balanced partitions on average")
    print("Explanation: Pivot selection strategy strongly affects performance.")
