graph = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]
n, m = 4, 3
color = [0] * n

def safe(v, c):
    return all(graph[v][u] == 0 or color[u] != c for u in range(n))

def solve(v):
    if v == n: return True
    for c in range(1, m+1):
        if safe(v,c):
            color[v] = c
            if solve(v+1): return True
            color[v] = 0
    return False

solve(0)
for i,c in enumerate(color): print(f"Vertex {i} → Color {c}")
