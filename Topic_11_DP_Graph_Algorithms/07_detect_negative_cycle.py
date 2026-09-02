def has_negative_cycle(n,edges):
    d=[0]*n
    for i in range(n):
        changed=False
        for u,v,w in edges:
            if d[u]+w<d[v]:
                d[v]=d[u]+w; changed=True
        if not changed: return False
    return True

e=[(0,1,1),(1,2,-1),(2,3,-1),(3,0,-1)]
print("Negative Weight Cycle Exists" if has_negative_cycle(4,e) else "No Negative Weight Cycle")
