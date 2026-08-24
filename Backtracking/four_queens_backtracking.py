def is_safe(board, row, col):
    for i in range(row):
        if board[i] == col:
            return False
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve(board, row):
    if row == 4:
        print_board(board)
        return True

    for col in range(4):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False


def print_board(board):
    for i in range(4):
        for j in range(4):
            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


board = [-1] * 4
solve(board, 0)
