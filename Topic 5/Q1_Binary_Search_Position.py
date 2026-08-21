def binary_search_position(arr, key):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1


n = int(input())
arr = list(map(int, input().split()))
key = int(input())

position = binary_search_position(arr, key)

if position != -1:
    print("Element found at position", position)
else:
    print("Element not found")
