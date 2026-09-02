grid=[
[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
count=0
def bt():
    global count
    for r in range(9):
        for c in range(9):
            if grid[r][c]==0:
                for x in range(1,10):
                    if x not in grid[r] and all(grid[i][c]!=x for i in range(9)) and all(grid[i][j]!=x for i in range(r//3*3,r//3*3+3) for j in range(c//3*3,c//3*3+3)):
                        grid[r][c]=x; bt(); grid[r][c]=0
                return
    count+=1
    return
bt()
print("Number of Valid Solutions =",count)
