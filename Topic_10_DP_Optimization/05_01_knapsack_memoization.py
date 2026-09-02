def knapsack(W,wt,val,n,memo):
    if n==0 or W==0: return 0
    if memo[n][W]!=-1: return memo[n][W]
    if wt[n-1]<=W:
        memo[n][W]=max(val[n-1]+knapsack(W-wt[n-1],wt,val,n-1,memo),
                       knapsack(W,wt,val,n-1,memo))
    else:
        memo[n][W]=knapsack(W,wt,val,n-1,memo)
    return memo[n][W]

wt=[1,3,4,5]; val=[1,4,5,7]; W=7
memo=[[-1]*(W+1) for _ in range(len(wt)+1)]
print("Maximum Profit =",knapsack(W,wt,val,len(wt),memo))
