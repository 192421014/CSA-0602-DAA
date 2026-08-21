"""Sequential Search - Q6: Sentinel Search vs Ordinary Sequential Search."""


def ordinary_sequential_search(arr, key):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == key:
            return i, comparisons
    return -1, comparisons


def sentinel_search(arr, key):
    """
    Sentinel search places the key at the end of the array so the loop
    never needs a separate bounds check (i < n) — only a value check is
    needed each iteration, which reduces the number of comparisons in
    the underlying machine code even though the logical comparison
    count reported here is the same for a found element.
    """
    n = len(arr)
    temp = arr.copy()
    last = temp[n - 1]
    temp[n - 1] = key  # place sentinel

    comparisons = 0
    i = 0
    while temp[i] != key:
        comparisons += 1
        i += 1
    comparisons += 1  # comparison that matched

    temp[n - 1] = last  # restore

    if i == n - 1 and last != key:
        return -1, comparisons
    return i, comparisons


if __name__ == "__main__":
    arr = [14, 9, 22, 35, 18, 41, 27]
    key = 18

    ord_index, ord_comparisons = ordinary_sequential_search(arr, key)
    sen_index, sen_comparisons = sentinel_search(arr, key)

    print("Ordinary Sequential Search:")
    if ord_index != -1:
        print(f"Position found = {ord_index + 1}")
    else:
        print("Position not found")
    print(f"Comparison count = {ord_comparisons}")
    print()

    print("Sentinel Search:")
    if sen_index != -1:
        print(f"Position found = {sen_index + 1}")
    else:
        print("Position not found")
    print(f"Comparison count = {sen_comparisons}")
