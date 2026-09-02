def reachable(graph,u,v):
    n=len(graph); r=[row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    return bool(r[u][v])

g=[[0,1,0],[0,0,1],[0,0,0]]
print("Path Exists" if reachable(g,0,2) else "Path Does Not Exist")
