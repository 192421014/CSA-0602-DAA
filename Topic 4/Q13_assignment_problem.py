"""
Topic 3 - Q13
Solve the Assignment Problem using exhaustive search (brute force over
all permutations of worker-task pairings).
"""

from itertools import permutations


def total_cost(assignment, cost_matrix):
    """
    assignment: list where assignment[i] = task assigned to worker i
    cost_matrix: 2D list, cost_matrix[i][j] = cost of worker i doing task j
    """
    total = 0
    for worker, task in enumerate(assignment):
        total += cost_matrix[worker][task]
    return total


def assignment_problem(cost_matrix):
    n = len(cost_matrix)
    tasks = list(range(n))

    best_cost = float('inf')
    best_assignment = None

    for perm in permutations(tasks):
        cost = total_cost(perm, cost_matrix)
        if cost < best_cost:
            best_cost = cost
            best_assignment = perm

    readable = [(f"worker {w + 1}", f"task {t + 1}") for w, t in enumerate(best_assignment)]
    return readable, best_cost


def run_test_case(label, cost_matrix):
    assignment, cost = assignment_problem(cost_matrix)
    print(f"{label}:")
    print(f"Optimal Assignment: {assignment}")
    print(f"Total Cost: {cost}")
    print()


if __name__ == "__main__":
    test_case_1 = [
        [3, 10, 7],
        [8, 5, 12],
        [4, 6, 9],
    ]

    test_case_2 = [
        [15, 9, 4],
        [8, 7, 18],
        [6, 12, 11],
    ]

    run_test_case("Test Case 1", test_case_1)
    run_test_case("Test Case 2", test_case_2)
