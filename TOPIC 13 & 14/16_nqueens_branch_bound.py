def solve(n):
    board=[["."]*n for _ in range(n)]
    cols=[False]*n; d1=[False]*(2*n-1); d2=[False]*(2*n-1)
    def bt(r):
        if r==n:return True
        for c in range(n):
            if not cols[c] and not d1[r-c+n-1] and not d2[r+c]:
                board[r][c]="Q"; cols[c]=d1[r-c+n-1]=d2[r+c]=True
                if bt(r+1):return True
                board[r][c]="."; cols[c]=d1[r-c+n-1]=d2[r+c]=False
        return False
    bt(0); return board

for row in solve(8): print(*row)
