n=5
graph=[set() for _ in range(n)]
for u,v in [(0,1),(1,2),(2,3),(3,4)]:
    graph[u].add(v); graph[v].add(u)
path=[]; used=set()

def solve(v):
    path.append(v); used.add(v)
    if len(path)==n: return True
    for u in graph[v]:
        if u not in used and solve(u): return True
    used.remove(v); path.pop()
    return False

solve(0)
print("Hamiltonian Path:", " → ".join(map(str,path)))
