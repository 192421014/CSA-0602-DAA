"""Sequential Search - Q7: Search student register numbers."""


def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    register_numbers = [101, 102, 103, 104, 105, 106]
    search_key = 104

    index = sequential_search(register_numbers, search_key)

    if index != -1:
        print(f"Register Number found at position {index + 1}")
    else:
        print("Register Number not found")
