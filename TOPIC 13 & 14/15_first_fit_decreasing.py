capacity=10
items=[2,5,4,7,1,3,8]
items.sort(reverse=True)
bins=[]
for x in items:
    for b in bins:
        if sum(b)+x <= capacity:
            b.append(x); break
    else: bins.append([x])
print("Sorted Items:",items)
for i,b in enumerate(bins,1): print(f"Bin {i}:",*b)
print("Total Bins Used =",len(bins))
