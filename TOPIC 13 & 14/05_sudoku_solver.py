grid = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]]

def solve():
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:
                for n in range(1, 10):
                    if valid(r,c,n):
                        grid[r][c] = n
                        if solve(): return True
                        grid[r][c] = 0
                return False
    return True

def valid(r,c,n):
    return (n not in grid[r] and
            all(grid[i][c] != n for i in range(9)) and
            all(grid[i][j] != n for i in range(r//3*3,r//3*3+3)
                for j in range(c//3*3,c//3*3+3)))

print("Solved Sudoku Grid:" if solve() else "No solution")
for row in grid: print(*row)
