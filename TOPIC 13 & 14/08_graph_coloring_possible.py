n, m = 5, 3
edges = [(0,1),(0,2),(1,2),(1,3),(2,4)]
graph = [[] for _ in range(n)]
for u,v in edges:
    graph[u].append(v); graph[v].append(u)
color = [0]*n

def solve(v):
    if v == n: return True
    for c in range(1,m+1):
        if all(color[u] != c for u in graph[v]):
            color[v]=c
            if solve(v+1): return True
            color[v]=0
    return False

print("Graph can be colored using 3 colors." if solve(0) else "Graph cannot be colored using 3 colors.")
