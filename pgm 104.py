arr = [25, 14, 31, 19, 25, 8]
comparisons = 0
swaps = 0
n = len(arr)
print("Initial Array:", arr)
for i in range(n - 1):
    for j in range(n - i - 1):
        comparisons += 1
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            swaps += 1
    print("After Pass", i + 1, ":", arr)
print("\nSorted Array:", arr)
print("Total Comparisons:", comparisons)
print("Total Swaps:", swaps)
print("Time Complexity:")
print("Best Case: O(n)")
print("Average Case: O(n^2)")
print("Worst Case: O(n^2)")