n=4
graph=[[i!=j for j in range(n)] for i in range(n)]
cycles=[]; path=[0]; used={0}

def solve():
    if len(path)==n:
        if graph[path[-1]][0]: cycles.append(path[:] + [0])
        return
    for v in range(1,n):
        if v not in used and graph[path[-1]][v]:
            used.add(v); path.append(v); solve(); path.pop(); used.remove(v)

solve()
for c in cycles: print(" → ".join(map(str,c)))
print("Total Cycles =", len(cycles))
