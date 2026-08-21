"""
Topic 2 - Q7
Determine the boundary points forming the convex hull using the basic approach.
"""

import math


def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if abs(val) < 1e-9:
        return 0
    return 1 if val > 0 else 2


def convex_hull_basic(points):
    n = len(points)
    hull_set = set()

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            p, q = points[i], points[j]
            all_left = True
            all_right = True

            for k in range(n):
                if k == i or k == j:
                    continue
                o = orientation(p, q, points[k])
                if o == 1:
                    all_left = False
                elif o == 2:
                    all_right = False

            if all_left or all_right:
                hull_set.add(p)
                hull_set.add(q)

    return order_points(list(hull_set))


def order_points(hull_points):
    if not hull_points:
        return []
    cx = sum(p[0] for p in hull_points) / len(hull_points)
    cy = sum(p[1] for p in hull_points) / len(hull_points)
    return sorted(hull_points, key=lambda p: math.atan2(p[1] - cy, p[0] - cx))


if __name__ == "__main__":
    points = [(1, 2), (3, 1), (5, 3), (4, 6), (2, 5)]

    hull = convex_hull_basic(points)

    print("Convex Hull Points:")
    print(", ".join(str(p) for p in hull))
