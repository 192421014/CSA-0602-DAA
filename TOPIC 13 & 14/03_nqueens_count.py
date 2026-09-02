def count_nqueens(n):
    cols, d1, d2 = set(), set(), set()

    def backtrack(row):
        if row == n:
            return 1
        count = 0
        for col in range(n):
            if col in cols or row-col in d1 or row+col in d2:
                continue
            cols.add(col); d1.add(row-col); d2.add(row+col)
            count += backtrack(row+1)
            cols.remove(col); d1.remove(row-col); d2.remove(row+col)
        return count

    return backtrack(0)

print("Total Number of Solutions =", count_nqueens(8))
