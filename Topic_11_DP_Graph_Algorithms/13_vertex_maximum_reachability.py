def max_reach(g):
    n=len(g); r=[row[:] for row in g]
    for k in range(n):
        for i in range(n):
            for j in range(n): r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    counts=[sum(r[i]) for i in range(n)]
    return min(((-counts[i],i) for i in range(n)))[1]

print(max_reach([[0,1,1,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]]))
