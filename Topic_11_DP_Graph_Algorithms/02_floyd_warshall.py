def floyd_warshall(graph):
    n=len(graph)
    dist=[row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k]!=float("inf") and dist[k][j]!=float("inf"):
                    dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    return dist

INF=float("inf")
g=[[0,5,INF,10],[INF,0,3,INF],[INF,INF,0,1],[INF,INF,INF,0]]
for row in floyd_warshall(g): print(row)
