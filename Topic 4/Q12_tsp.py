"""
Topic 3 - Q12
Solve the Travelling Salesman Problem (TSP) using exhaustive search /
brute force. Include test cases with different city configurations and
print the shortest distance and the corresponding path for each test case.
"""

import math
from itertools import permutations


def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def path_distance(path):
    total = 0.0
    for i in range(len(path) - 1):
        total += euclidean_distance(path[i], path[i + 1])
    return total


def tsp_brute_force(cities):
    """
    Fix the first city as the starting point, try every permutation of the
    remaining cities, and return the shortest closed tour (path back to
    the starting city).
    """
    start = cities[0]
    other_cities = cities[1:]

    best_distance = float('inf')
    best_path = None

    for perm in permutations(other_cities):
        candidate_path = [start] + list(perm) + [start]
        d = path_distance(candidate_path)
        if d < best_distance:
            best_distance = d
            best_path = candidate_path

    return best_path, best_distance


def run_test_case(label, cities):
    path, distance = tsp_brute_force(cities)
    print(f"{label}:")
    print(f"Shortest Distance: {distance}")
    print(f"Shortest Path: {path}")
    print()


if __name__ == "__main__":
    test_case_1 = [(1, 2), (4, 5), (7, 1), (3, 6)]
    test_case_2 = [(2, 4), (8, 1), (1, 7), (6, 3), (5, 9)]

    run_test_case("Test Case 1", test_case_1)
    run_test_case("Test Case 2", test_case_2)
