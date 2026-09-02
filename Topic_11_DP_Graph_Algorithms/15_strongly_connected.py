def strongly_connected(g):
    n=len(g); r=[row[:] for row in g]
    for k in range(n):
        for i in range(n):
            for j in range(n): r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    return all(r[i][j] or i==j for i in range(n) for j in range(n))

g=[[0,1,0],[0,0,1],[1,0,0]]
print("Strongly Connected" if strongly_connected(g) else "Not Strongly Connected")
