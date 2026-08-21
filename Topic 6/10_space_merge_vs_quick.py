def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

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


def quick_sort(arr):
    a = arr[:]
    max_depth = [0]

    def partition(low, high):
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def sort(low, high, depth):
        if low < high:
            max_depth[0] = max(max_depth[0], depth)
            p = partition(low, high)
            sort(low, p - 1, depth + 1)
            sort(p + 1, high, depth + 1)

    if a:
        sort(0, len(a) - 1, 1)

    return a, max_depth[0]


arr = [5, 3, 8, 4, 2]

merge_result = merge_sort(arr)
quick_result, quick_depth = quick_sort(arr)

print("Sorted :", merge_result)
print("Merge Auxiliary Space : O(n)")
print("Quick Auxiliary Space : O(log n) average, O(n) worst case")
print("Quick Recursion Depth for this input :", quick_depth)
