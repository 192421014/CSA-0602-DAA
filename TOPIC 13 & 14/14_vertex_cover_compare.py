import itertools
n=6
edges=[(0,1),(0,2),(1,3),(2,4),(3,5)]

best=set(range(n))
for r in range(n+1):
    for comb in itertools.combinations(range(n),r):
        s=set(comb)
        if all(u in s or v in s for u,v in edges):
            best=s; break
    if len(best)==r: break

remaining=edges[:]; approx=set()
while remaining:
    u,v=remaining[0]; approx.update((u,v))
    remaining=[e for e in remaining if u not in e and v not in e]

print("Exact Vertex Cover Size =",len(best))
print("Approximate Vertex Cover Size =",len(approx))
print("Approximation Ratio =", round(len(approx)/len(best),2))
