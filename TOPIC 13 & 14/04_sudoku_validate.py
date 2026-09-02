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

row, col, num = 0, 2, 4

safe = (num not in grid[row] and
        all(grid[r][col] != num for r in range(9)) and
        all(grid[r][c] != num
            for r in range(row//3*3, row//3*3+3)
            for c in range(col//3*3, col//3*3+3)))
print("Safe Placement:", "YES" if safe else "NO")
