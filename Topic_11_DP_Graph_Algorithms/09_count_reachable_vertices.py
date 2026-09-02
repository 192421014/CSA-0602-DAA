def count_reachable(graph,source):
    n=len(graph); r=[row[:] for row in graph]
    for k in range(n):
        for i in range(n):
            for j in range(n): r[i][j]=r[i][j] or (r[i][k] and r[k][j])
    return sum(r[source][j] for j in range(n) if j!=source)

print(count_reachable([[0,1,0,0],[0,0,1,0],[0,0,0,1],[0,0,0,0]],0))
