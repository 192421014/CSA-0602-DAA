def find_vertex(g):
    n=len(g); r=[row[:] for row in g]
    for k in range(n):
        for i in range(n):
            for j in range(n): r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    for v in range(n):
        if all(i==v or r[i][v] for i in range(n)): return v
    return -1

print(find_vertex([[0,1,1],[0,0,1],[0,0,0]]))
