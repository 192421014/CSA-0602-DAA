from functools import lru_cache

def tsp(graph):
    n=len(graph)
    @lru_cache(None)
    def visit(mask,pos):
        if mask==(1<<n)-1:
            return graph[pos][0]
        ans=float("inf")
        for city in range(n):
            if not mask & (1<<city):
                ans=min(ans,graph[pos][city]+visit(mask|(1<<city),city))
        return ans
    return visit(1,0)

graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
print("Minimum Cost:",tsp(graph))
