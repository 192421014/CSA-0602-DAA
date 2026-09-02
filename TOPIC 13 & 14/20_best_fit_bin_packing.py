capacity=10
items=[2,5,4,7,1,3,8]
bins=[]
for x in items:
    best=-1; best_remaining=capacity+1
    for i,b in enumerate(bins):
        rem=capacity-sum(b)
        if x<=rem and rem-x<best_remaining:
            best=i; best_remaining=rem-x
    if best>=0: bins[best].append(x)
    else: bins.append([x])
for i,b in enumerate(bins,1):print(f"Bin {i}:",*b)
print("Total Bins Used =",len(bins))
