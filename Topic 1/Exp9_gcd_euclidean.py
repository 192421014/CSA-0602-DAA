"""
Experiment 9: GCD (Euclidean Algorithm)
Objective: Analyze recursive GCD.
Complexity: O(log n)
"""

import time


def gcd_recursive(a, b, depth=0):
    if b == 0:
        return a, depth
    return gcd_recursive(b, a % b, depth + 1)


if __name__ == "__main__":
    a, b = 48, 18

    start = time.perf_counter()
    result, recursive_calls = gcd_recursive(a, b)
    end = time.perf_counter()

    print(f"GCD of {a} and {b} = {result}")
    print(f"Recursive calls made: {recursive_calls}")
    print(f"Execution time: {end - start:.8f} seconds")

    print("\nComplexity Analysis:")
    print("Time Complexity: O(log(min(a, b))) -> each recursive step reduces "
          "the problem size roughly by the modulus operation, similar to "
          "Fibonacci-related shrinkage")
    print("Space Complexity: O(log n) -> recursion stack depth")
    print("Explanation: The Euclidean algorithm converges quickly because "
          "the remainder shrinks fast with each step.")
