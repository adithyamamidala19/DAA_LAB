"""
================================================================================
PRACTICAL 04: FACTORIAL USING ITERATIVE METHOD
================================================================================
Practical Number : Practical 04
Topic Name       : Factorial Program (Iterative Method)
Objective        : To implement the Factorial program using an iterative 
                   (loop-based) approach in Python, calculate n!, measure actual 
                   execution time using time.perf_counter(), and analyze its 
                   theoretical time and space complexity.

Algorithm Description:
  The iterative factorial approach computes n! by executing a loop from 2 to n,
  accumulating the product in a single integer variable. It uses constant O(1)
  auxiliary memory and avoids call stack overhead.
================================================================================
"""

import time


def factorial_iterative(n):
    """
    Computes n! iteratively using a for loop.
    
    Parameters:
      n (int): A non-negative integer.
      
    Returns:
      int: The factorial value n!
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
        
    return result


def main():
    print("=" * 70)
    print("PRACTICAL 04: FACTORIAL (ITERATIVE METHOD)")
    print("=" * 70)

    n = 20
    print(f"Input Number (n) : {n}\n")

    # Measure execution time
    start_time = time.perf_counter()
    result = factorial_iterative(n)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"Calculated Factorial ({n}!) : {result}")
    print(f"Execution Time              : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(1) [When n = 0 or 1]")
    print("    - Average Case : O(n) [Performs n-1 multiplications]")
    print("    - Worst Case   : O(n)")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(1) [Requires only a single accumulator variable]")
    print("=" * 70)


if __name__ == "__main__":
    main()
