def all_nqueens(n):
    solutions = []
    board = [[0] * n for _ in range(n)]
    cols, d1, d2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            solutions.append([r[:] for r in board])
            return
        for col in range(n):
            if col in cols or row - col in d1 or row + col in d2:
                continue
            board[row][col] = 1
            cols.add(col); d1.add(row-col); d2.add(row+col)
            backtrack(row+1)
            board[row][col] = 0
            cols.remove(col); d1.remove(row-col); d2.remove(row+col)

    backtrack(0)
    return solutions

solutions = all_nqueens(4)
print("Total Solutions =", len(solutions))
for i, sol in enumerate(solutions, 1):
    print("Solution", i)
    for row in sol:
        print(*row)
