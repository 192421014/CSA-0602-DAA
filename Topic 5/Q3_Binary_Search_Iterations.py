def binary_search_iterations(arr, key):
    low, high = 0, len(arr) - 1
    iterations = 0

    while low <= high:
        iterations += 1
        mid = (low + high) // 2

        if arr[mid] == key:
            return True, iterations
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return False, iterations


n = int(input())
arr = list(map(int, input().split()))
key = int(input())

found, iterations = binary_search_iterations(arr, key)

if found:
    print("Element found")
else:
    print("Element not found")

print("Iterations =", iterations)
