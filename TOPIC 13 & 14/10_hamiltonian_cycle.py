graph = [[0,1,0,1,0],[1,0,1,1,1],[0,1,0,0,1],[1,1,0,0,1],[0,1,1,1,0]]
n=5
path=[0]+[-1]*(n-1)
used={0}

def solve(pos):
    if pos==n:
        return graph[path[-1]][path[0]] == 1
    for v in range(1,n):
        if v not in used and graph[path[pos-1]][v]:
            path[pos]=v; used.add(v)
            if solve(pos+1): return True
            used.remove(v); path[pos]=-1
    return False

if solve(1): print("Hamiltonian Cycle Exists:", " → ".join(map(str,path+[0])))
else: print("No Hamiltonian Cycle")
