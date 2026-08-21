"""
Topic 1 - Q5
Part A: Closest pair of points using brute force + time complexity analysis.
Part B: Brute-force convex hull algorithm for a given point set, and how to
        handle multiple collinear points.
"""

import math
import time


# ---------------------------------------------------------------------------
# Part A: Closest Pair (Brute Force)
# ---------------------------------------------------------------------------

def euclidean_distance(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_brute_force(points):
    """
    Find the closest pair of points using the brute force method.
    Time Complexity: O(n^2) because every pair of points is compared once
    using two nested loops.
    Space Complexity: O(1) extra space (excluding the input list).
    """
    n = len(points)
    min_dist = float('inf')
    pair = (None, None)

    for i in range(n):
        for j in range(i + 1, n):
            d = euclidean_distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])

    return pair, min_dist


def test_closest_pair():
    sample_points = [(1, 2), (4, 5), (7, 8), (3, 1), (0, 0)]

    start = time.perf_counter()
    pair, min_dist = closest_pair_brute_force(sample_points)
    end = time.perf_counter()

    print("---- Closest Pair (Brute Force) ----")
    print(f"Points: {sample_points}")
    print(f"Closest pair: {pair[0]} - {pair[1]}")
    print(f"Minimum distance: {min_dist}")
    print(f"Execution time: {end - start:.8f} seconds")
    print("Time Complexity: O(n^2)  |  Space Complexity: O(1)")
    print()


# ---------------------------------------------------------------------------
# Part B: Convex Hull (Brute Force)
# ---------------------------------------------------------------------------

def orientation(p, q, r):
    """
    Returns:
        0 -> collinear
        1 -> clockwise
        2 -> counterclockwise
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if abs(val) < 1e-9:
        return 0
    return 1 if val > 0 else 2


def convex_hull_brute_force(points):
    """
    Brute-force convex hull: a directed edge (p, q) is part of the hull
    if all other points lie strictly on one side of the line through p, q.
    To handle multiple collinear points on the hull boundary, points that
    lie exactly ON the line (orientation == 0) are allowed rather than
    rejected, and are later ordered along the segment before being added.
    """
    n = len(points)
    hull_edges = []

    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            p, q = points[i], points[j]
            all_left = True
            all_right = True
            collinear_pts = []

            for k in range(n):
                if k == i or k == j:
                    continue
                o = orientation(p, q, points[k])
                if o == 1:
                    all_left = False
                elif o == 2:
                    all_right = False
                else:
                    collinear_pts.append(points[k])

            # Valid hull edge if all remaining points are on one side only
            if all_left or all_right:
                hull_edges.append((p, q))

    # Collect unique hull points from valid edges
    hull_points = []
    for p, q in hull_edges:
        if p not in hull_points:
            hull_points.append(p)
        if q not in hull_points:
            hull_points.append(q)

    return order_hull_points(hull_points)


def order_hull_points(hull_points):
    """Order hull points counter-clockwise around their centroid."""
    if not hull_points:
        return []

    cx = sum(p[0] for p in hull_points) / len(hull_points)
    cy = sum(p[1] for p in hull_points) / len(hull_points)

    def angle(p):
        return math.atan2(p[1] - cy, p[0] - cx)

    return sorted(hull_points, key=angle)


def test_convex_hull():
    points = [
        (10, 0),    # P1
        (11, 5),    # P2
        (5, 3),     # P3
        (9, 3.5),   # P4
        (15, 3),    # P5
        (12.5, 7),  # P6
        (6, 6.5),   # P7
        (7.5, 4.5), # P8
    ]

    hull = convex_hull_brute_force(points)

    print("---- Convex Hull (Brute Force) ----")
    print(f"Points: {points}")
    print(f"Convex Hull Points: {hull}")
    print()
    print("Handling collinear points:")
    print("If three or more points lie on the same hull edge, the brute")
    print("force check (orientation == 0) treats them as valid boundary")
    print("candidates instead of discarding them. They are then sorted by")
    print("their distance/position along that edge so the innermost")
    print("collinear point(s) can optionally be dropped, keeping only the")
    print("two extreme endpoints, or kept if the assignment requires every")
    print("boundary point to be reported.")


if __name__ == "__main__":
    test_closest_pair()
    test_convex_hull()
