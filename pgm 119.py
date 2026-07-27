arr = [16, 28, 16, 39, 52, 64, 16]
target = 16
comparisons = 0
found = False
for i in range(len(arr)):
    comparisons += 1
    if arr[i] == target:
        print("Target found at Index:", i)
        found = True
        break
if not found:
    print("Target not found")
print("Total Comparisons:", comparisons)
print("Time Complexity:")
print("Best Case: O(1)")
print("Average Case: O(n)")
print("Worst Case: O(n)")