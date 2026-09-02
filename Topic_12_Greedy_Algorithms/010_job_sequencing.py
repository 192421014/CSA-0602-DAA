def job_sequencing(jobs,deadlines,profits):
    data=sorted(zip(jobs,deadlines,profits),key=lambda x:x[2],reverse=True)
    slots=[None]*(max(deadlines)+1)
    total=0
    for job,d,p in data:
        for t in range(min(d,len(slots)-1),0,-1):
            if slots[t] is None:
                slots[t]=job; total+=p; break
    return [x for x in slots[1:] if x],total

jobs=['P1', 'P2', 'P3', 'P4']; deadlines=[1, 1, 2, 2]; profits=[40, 30, 20, 10]
selected,total=job_sequencing(jobs,deadlines,profits)
print("Selected jobs =",selected)
print("Maximum profit =",total)
