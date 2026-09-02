def fractional_knapsack(weights,profits,capacity):
    items=sorted(zip(weights,profits),key=lambda x:x[1]/x[0],reverse=True)
    total=0
    for w,p in items:
        take=min(w,capacity)
        total+=take*(p/w)
        capacity-=take
        if capacity==0: break
    return total
print("Maximum profit =",fractional_knapsack([2,3,5,7],[10,5,15,7],8))
