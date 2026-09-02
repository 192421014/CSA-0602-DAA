def job_sequencing(jobs,deadlines,profits):
    data=sorted(zip(jobs,deadlines,profits),key=lambda x:x[2],reverse=True)
    slots=[None]*(max(deadlines)+1)
    total=0
    for job,d,p in data:
        for t in range(min(d,len(slots)-1),0,-1):
            if slots[t] is None:
                slots[t]=job; total+=p; break
    return [x for x in slots[1:] if x],total

jobs=['A', 'B', 'C', 'D']; deadlines=[2, 1, 2, 1]; profits=[100, 19, 27, 25]
selected,total=job_sequencing(jobs,deadlines,profits)
print("Selected jobs =",selected)
print("Maximum profit =",total)
