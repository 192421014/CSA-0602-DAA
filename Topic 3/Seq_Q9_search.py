"""Sequential Search - Q9: Search on a 2-D matrix."""


def search_2d_matrix(matrix, key):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == key:
                return r, c
    return -1, -1


if __name__ == "__main__":
    matrix = [
        [12, 8, 15],
        [5, 18, 27],
        [9, 11, 24],
    ]
    key = 24

    row, col = search_2d_matrix(matrix, key)

    if row != -1:
        print(f"Element found at Row {row + 1} Column {col + 1}")
    else:
        print("Element not found")
