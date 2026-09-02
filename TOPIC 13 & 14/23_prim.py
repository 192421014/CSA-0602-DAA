import heapq
n=4
edges=[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
g=[[] for _ in range(n)]
for u,v,w in edges:g[u].append((v,w));g[v].append((u,w))
used={0};pq=[(w,0,v) for v,w in g[0]];heapq.heapify(pq);mst=[];total=0
while pq and len(used)<n:
    w,u,v=heapq.heappop(pq)
    if v in used:continue
    used.add(v);mst.append((u,v,w));total+=w
    for to,cost in g[v]:
        if to not in used:heapq.heappush(pq,(cost,v,to))
print("MST edges:",mst)
print("Total weight:",total)
