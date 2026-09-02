def optimal_bst(keys,freq):
    n=len(keys)
    cost=[[0]*n for _ in range(n)]
    for i in range(n): cost[i][i]=freq[i]
    for length in range(2,n+1):
        for i in range(n-length+1):
            j=i+length-1
            total=sum(freq[i:j+1])
            cost[i][j]=float("inf")
            for r in range(i,j+1):
                left=cost[i][r-1] if r>i else 0
                right=cost[r+1][j] if r<j else 0
                cost[i][j]=min(cost[i][j],left+right+total)
    return cost[0][n-1]

print("Optimal BST Cost:",optimal_bst([10,20,30],[34,8,50]))
