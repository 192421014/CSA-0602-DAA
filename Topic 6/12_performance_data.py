def merge_sort_count(arr):
    comparisons = [0]

    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons[0] += 1

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def sort(a):
        if len(a) <= 1:
            return a[:]

        mid = len(a) // 2
        return merge(sort(a[:mid]), sort(a[mid:]))

    return sort(arr), comparisons[0]


def quick_sort_count(arr):
    a = arr[:]
    comparisons = [0]

    def partition(low, high):
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            comparisons[0] += 1

            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]

        a[i + 1], a[high] = a[high], a[i + 1]
        return i + 1

    def sort(low, high):
        if low < high:
            p = partition(low, high)
            sort(low, p - 1)
            sort(p + 1, high)

    sort(0, len(a) - 1)
    return a, comparisons[0]


test_arrays = [
    [5, 4, 3, 2, 1],
    [8, 7, 6, 5, 4, 3, 2, 1]
]

print("N\tMerge Comparisons\tQuick Comparisons")

for arr in test_arrays:
    _, merge_count = merge_sort_count(arr)
    _, quick_count = quick_sort_count(arr)

    print(len(arr), "\t", merge_count, "\t\t\t", quick_count)
