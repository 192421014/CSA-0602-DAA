import heapq

def huffman(chars,freq):
    heap=[[f,[c,""]] for c,f in zip(chars,freq)]
    heapq.heapify(heap)
    while len(heap)>1:
        a=heapq.heappop(heap); b=heapq.heappop(heap)
        for x in a[1:]: x[1]="0"+x[1]
        for x in b[1:]: x[1]="1"+x[1]
        heapq.heappush(heap,[a[0]+b[0]]+a[1:]+b[1:])
    return sorted(heap[0][1:],key=lambda x:x[0])

for c,code in huffman(["a","b","c","d","e","f"],[5,9,12,13,16,45]):
    print(c,":",code)
