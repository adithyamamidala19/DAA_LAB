"""
================================================================================
PRACTICAL 04: FACTORIAL USING RECURSIVE METHOD
================================================================================
Practical Number : Practical 04
Topic Name       : Factorial Program (Recursive Method)
Objective        : To implement the Factorial program using a recursive approach 
                   in Python, calculate n!, measure actual execution time using 
                   time.perf_counter(), and analyze its theoretical time and 
                   space complexity.

Algorithm Description:
  The recursive factorial approach uses the recurrence relation n! = n * (n - 1)!
  with base conditions 0! = 1 and 1! = 1. Each recursive call pushes a stack 
  frame onto the call stack until reaching the base case, after which return 
  values propagate up the stack.
================================================================================
"""

import time
import sys

# Ensure recursion depth is sufficient
sys.setrecursionlimit(2000)


def factorial_recursive(n):
    """
    Computes n! recursively.
    
    Parameters:
      n (int): A non-negative integer.
      
    Returns:
      int: The factorial value n!
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    # Base cases
    if n == 0 or n == 1:
        return 1
    
    # Recursive step
    return n * factorial_recursive(n - 1)


def main():
    print("=" * 70)
    print("PRACTICAL 04: FACTORIAL (RECURSIVE METHOD)")
    print("=" * 70)

    n = 20
    print(f"Input Number (n) : {n}\n")

    # Measure execution time
    start_time = time.perf_counter()
    result = factorial_recursive(n)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"Calculated Factorial ({n}!) : {result}")
    print(f"Execution Time              : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(1) [When n = 0 or 1]")
    print("    - Average Case : O(n) [T(n) = T(n-1) + O(1)]")
    print("    - Worst Case   : O(n)")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(n) [Due to n stack frames on the recursion call stack]")
    print("=" * 70)


if __name__ == "__main__":
    main()
