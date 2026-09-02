import heapq
n=5
edges=[(0,1,4),(0,2,1),(2,1,2),(1,3,1),(2,3,5),(3,4,3)]
g=[[] for _ in range(n)]
for u,v,w in edges:g[u].append((v,w));g[v].append((u,w))
dist=[float("inf")]*n; parent=[-1]*n; dist[0]=0; pq=[(0,0)]
while pq:
    d,u=heapq.heappop(pq)
    if d!=dist[u]:continue
    for v,w in g[u]:
        if d+w<dist[v]:dist[v]=d+w;parent[v]=u;heapq.heappush(pq,(dist[v],v))
print("Distances from 0:",dist)
