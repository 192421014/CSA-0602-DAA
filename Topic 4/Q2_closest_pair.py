"""
Topic 1 - Q2
Find the closest pair of points using exhaustive comparison of all pairs.
"""

import math


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_exhaustive(points):
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


if __name__ == "__main__":
    points = [(2, 3), (5, 4), (1, 7), (8, 9), (4, 6)]

    pair, min_dist = closest_pair_exhaustive(points)

    print(f"Closest pair: {pair[0]} - {pair[1]}")
    print(f"Minimum distance: {min_dist}")
