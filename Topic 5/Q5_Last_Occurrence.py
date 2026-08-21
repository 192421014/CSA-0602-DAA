def last_occurrence(arr, key):
    low, high = 0, len(arr) - 1
    answer = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            answer = mid
            low = mid + 1
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return answer


n = int(input())
arr = list(map(int, input().split()))
key = int(input())

index = last_occurrence(arr, key)

if index != -1:
    print("Last occurrence at index", index)
else:
    print("Element not found")
