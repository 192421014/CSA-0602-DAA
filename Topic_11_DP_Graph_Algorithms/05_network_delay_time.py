def network_delay(times,n,k):
    d=[float("inf")]*(n+1); d[k]=0
    for _ in range(n-1):
        for u,v,w in times:
            if d[u]!=float("inf"): d[v]=min(d[v],d[u]+w)
    ans=max(d[1:])
    return -1 if ans==float("inf") else ans

print(network_delay([[2,1,1],[2,3,1],[3,4,1]],4,2))
