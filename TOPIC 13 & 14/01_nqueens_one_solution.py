def solve_nqueens(n):
    board = [[0] * n for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            return True
        for col in range(n):
            if col in cols or row - col in diag1 or row + col in diag2:
                continue
            board[row][col] = 1
            cols.add(col); diag1.add(row - col); diag2.add(row + col)
            if backtrack(row + 1):
                return True
            board[row][col] = 0
            cols.remove(col); diag1.remove(row - col); diag2.remove(row + col)
        return False

    backtrack(0)
    return board

n = 4
for row in solve_nqueens(n):
    print(*row)
