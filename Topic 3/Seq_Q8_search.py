"""Sequential Search - Q8: Search for string data."""


def sequential_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


if __name__ == "__main__":
    names = ["Anu", "Bala", "Charan", "Deepa", "Esha", "Farhan"]
    search_name = "Deepa"

    index = sequential_search(names, search_name)

    if index != -1:
        print(f"Name found at position {index + 1}")
    else:
        print("Name not found")
