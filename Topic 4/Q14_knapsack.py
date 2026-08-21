"""
Topic 3 - Q14
Solve the 0-1 Knapsack Problem using exhaustive search over all subsets.
"""

from itertools import combinations


def total_value(items, values):
    """items: list of selected item indices."""
    return sum(values[i] for i in items)


def total_weight(items, weights):
    return sum(weights[i] for i in items)


def is_feasible(items, weights, capacity):
    """Check if the total weight of the selected items exceeds capacity."""
    return total_weight(items, weights) <= capacity


def knapsack_exhaustive(weights, values, capacity):
    n = len(weights)
    best_value = 0
    best_selection = []

    for r in range(n + 1):
        for combo in combinations(range(n), r):
            items = list(combo)
            if is_feasible(items, weights, capacity):
                value = total_value(items, values)
                if value > best_value:
                    best_value = value
                    best_selection = items

    return best_selection, best_value


def run_test_case(label, weights, values, capacity):
    selection, value = knapsack_exhaustive(weights, values, capacity)
    names = ", ".join(str(i) for i in selection)
    print(f"{label}:")
    print(f"Optimal Selection: {selection} (Items with indices {names})")
    print(f"Total Value: {value}")
    print()


if __name__ == "__main__":
    # Simple Case
    weights_1 = [2, 3, 1]
    values_1 = [4, 5, 3]
    capacity_1 = 4
    run_test_case("Test Case 1", weights_1, values_1, capacity_1)

    # More Complex Case
    weights_2 = [1, 2, 3, 4]
    values_2 = [2, 4, 6, 3]
    capacity_2 = 6
    run_test_case("Test Case 2", weights_2, values_2, capacity_2)
