def diameter(g):
    n=len(g); d=[r[:] for r in g]
    for k in range(n):
        for i in range(n):
            for j in range(n): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
    return max(d[i][j] for i in range(n) for j in range(n) if d[i][j]!=float("inf"))

INF=float("inf")
print(diameter([[0,2,INF],[2,0,3],[INF,3,0]]))
