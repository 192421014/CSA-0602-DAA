edges=[(0,1),(0,2),(1,3),(2,4)]
remaining=edges[:]; cover=set()
while remaining:
    u,v=remaining[0]
    cover.update((u,v))
    remaining=[e for e in remaining if u not in e and v not in e]
print("Approximate Vertex Cover:", cover)
print("Cover Size =", len(cover))
