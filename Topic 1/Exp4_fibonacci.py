"""
Experiment 4: Fibonacci Series
Objective: Analyze recursive vs iterative Fibonacci generation.
Complexity: Iterative O(n), Recursive naive O(2^n), Recursive with memoization O(n)
"""

import time


def fibonacci_iterative(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series


def fibonacci_recursive_naive(k, memo=None):
    if k <= 1:
        return k
    return fibonacci_recursive_naive(k - 1) + fibonacci_recursive_naive(k - 2)


def fibonacci_recursive_memo(k, memo=None):
    if memo is None:
        memo = {}
    if k <= 1:
        return k
    if k in memo:
        return memo[k]
    memo[k] = fibonacci_recursive_memo(k - 1, memo) + fibonacci_recursive_memo(k - 2, memo)
    return memo[k]


if __name__ == "__main__":
    n = 6

    start = time.perf_counter()
    series_iterative = fibonacci_iterative(n)
    end = time.perf_counter()
    print(f"Iterative Fibonacci (first {n} terms): {series_iterative}")
    print(f"Iterative execution time: {end - start:.8f} seconds")

    start = time.perf_counter()
    series_naive = [fibonacci_recursive_naive(k) for k in range(n)]
    end = time.perf_counter()
    print(f"Recursive (naive) Fibonacci (first {n} terms): {series_naive}")
    print(f"Naive recursive execution time: {end - start:.8f} seconds")

    start = time.perf_counter()
    series_memo = [fibonacci_recursive_memo(k) for k in range(n)]
    end = time.perf_counter()
    print(f"Recursive (memoized) Fibonacci (first {n} terms): {series_memo}")
    print(f"Memoized recursive execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Iterative Fibonacci        : O(n) time, O(n) space (for storing series)")
    print("Recursive (naive) Fibonacci: O(2^n) time -> exponential due to repeated "
          "recomputation of overlapping subproblems")
    print("Recursive (memoized)       : O(n) time -> each subproblem solved once "
          "and cached")
