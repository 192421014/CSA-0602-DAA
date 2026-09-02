def cheapest(flights,n,src,dst,K):
    INF=10**9; d=[INF]*n; d[src]=0
    for _ in range(K+1):
        nd=d[:]
        for u,v,c in flights:
            if d[u]!=INF: nd[v]=min(nd[v],d[u]+c)
        d=nd
    return -1 if d[dst]==INF else d[dst]

print(cheapest([[0,1,100],[1,2,100],[2,3,100],[0,3,500]],4,0,3,2))
