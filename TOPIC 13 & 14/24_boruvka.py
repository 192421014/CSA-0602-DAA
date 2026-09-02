n=4
edges=[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
parent=list(range(n))
def find(x):
    if parent[x]!=x:parent[x]=find(parent[x])
    return parent[x]
mst=[];total=0
while len(mst)<n-1:
    cheapest=[None]*n
    for u,v,w in edges:
        a,b=find(u),find(v)
        if a==b:continue
        if cheapest[a] is None or w<cheapest[a][2]:cheapest[a]=(u,v,w)
        if cheapest[b] is None or w<cheapest[b][2]:cheapest[b]=(u,v,w)
    for e in cheapest:
        if e:
            u,v,w=e;a,b=find(u),find(v)
            if a!=b:parent[a]=b;mst.append(e);total+=w
print("MST edges:",mst)
print("Total weight:",total)
