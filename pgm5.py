import math
points = [
    ("A", (2, 3)),
    ("B", (12, 30)),
    ("C", (40, 50)),
    ("D", (5, 1)),
    ("E", (12, 10))
]
minimum = float('inf')
pair = ()
comparisons = 0
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        x1, y1 = points[i][1]
        x2, y2 = points[j][1]
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        print(points[i][0], "-", points[j][0], "=", round(distance, 2))
        comparisons += 1
        if distance < minimum:
            minimum = distance
            pair = (points[i][0], points[j][0])
print("\nClosest Pair:", pair)
print("Minimum Distance:", round(minimum, 2))
print("Total Comparisons:", comparisons)
print("Time Complexity: O(n^2)")