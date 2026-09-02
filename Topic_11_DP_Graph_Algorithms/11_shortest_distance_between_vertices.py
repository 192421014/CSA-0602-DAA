INF=float("inf")
g=[[0,3,INF,7],[8,0,2,INF],[5,INF,0,1],[2,INF,INF,0]]
n=len(g); d=[r[:] for r in g]
for k in range(n):
    for i in range(n):
        for j in range(n): d[i][j]=min(d[i][j],d[i][k]+d[k][j])
print("Shortest Distance =",d[0][3])
