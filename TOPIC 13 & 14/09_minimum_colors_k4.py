n = 4
edges = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]

for k in range(1,n+1):
    color=[0]*n
    def solve(v):
        if v==n: return True
        for c in range(1,k+1):
            if all(color[u]!=c for u,w in edges for u,w in []): pass
            ok=True
            for u,w in edges:
                if (u==v and color[w]==c) or (w==v and color[u]==c):
                    ok=False
            if ok:
                color[v]=c
                if solve(v+1): return True
                color[v]=0
        return False
    if solve(0):
        print("Minimum Colors Required =", k); break
