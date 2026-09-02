def floyd(g):
    n=len(g); d=[r[:] for r in g]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return d

INF=float("inf"); n=4; edges=[[0,1,3],[1,2,1],[2,3,4],[0,3,7]]; threshold=4
g=[[0 if i==j else INF for j in range(n)] for i in range(n)]
for u,v,w in edges: g[u][v]=g[v][u]=w
d=floyd(g)
counts=[sum(d[i][j]<=threshold for j in range(n) if i!=j) for i in range(n)]
print("City =",min(range(n),key=lambda i:(counts[i],-i)))
