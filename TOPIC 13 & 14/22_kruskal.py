edges=[(0,1,10),(0,2,6),(0,3,5),(1,3,15),(2,3,4)]
parent=list(range(4))
def find(x):
    while parent[x]!=x: parent[x]=parent[parent[x]];x=parent[x]
    return x
mst=[];weight=0
for u,v,w in sorted(edges,key=lambda e:e[2]):
    a,b=find(u),find(v)
    if a!=b: parent[a]=b;mst.append((u,v,w));weight+=w
print("Edges in MST:",mst)
print("Total weight of MST:",weight)
