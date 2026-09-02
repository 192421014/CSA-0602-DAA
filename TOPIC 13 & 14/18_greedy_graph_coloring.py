n=5
edges=[(0,1),(0,2),(1,2),(1,3),(2,4)]
adj=[set() for _ in range(n)]
for u,v in edges: adj[u].add(v); adj[v].add(u)
color=[0]*n
for v in range(n):
    used={color[u] for u in adj[v]}
    c=1
    while c in used:c+=1
    color[v]=c
for v,c in enumerate(color):print(f"Vertex {v} → Color {c}")
print("Total Colors Used =",max(color))
