"""
================================================================================
PRACTICAL 06: MATRIX CHAIN MULTIPLICATION USING DYNAMIC PROGRAMMING
================================================================================
Title: Implementation of Matrix Chain Multiplication using Dynamic Programming
Algorithm:
  - Bottom-Up Tabulation Dynamic Programming (Chain Length Approach)

Description:
  Given a sequence of matrices, this program finds the most efficient way to
  multiply these matrices together. The problem is not actually to perform the
  multiplications, but merely to decide in which order the multiplications
  should be performed (optimal parenthesization) to minimize the total scalar
  multiplication operations.
================================================================================
"""

import time
import sys


def matrix_chain_order(p):
    """
    Finds the minimum number of scalar multiplications needed to multiply a chain
    of n matrices of dimensions given in array p, along with optimal parenthesization.
    
    Parameters:
      p (list): Array of dimensions where matrix A_i has dimension p[i-1] x p[i].
      
    Returns:
      tuple: (m, s, min_cost, optimal_parens_str)
        m: Cost table where m[i][j] is min scalar multiplications for A_i..A_j
        s: Split table where s[i][j] is index k at which optimal split occurs
    """
    n = len(p) - 1  # Number of matrices (1 to n)

    # m[i][j] will hold minimum multiplications needed for Ai..Aj (1-indexed)
    m = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # s[i][j] stores optimal split point k
    s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # L is chain length (from 2 matrices up to n matrices)
    for L in range(2, n + 1):
        for i in range(1, n - L + 2):
            j = i + L - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                # Cost = cost(Ai..Ak) + cost(Ak+1..Aj) + cost to multiply the two resulting matrices
                cost = m[i][k] + m[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    def construct_optimal_parens(s, i, j):
        if i == j:
            return f"A{i}"
        else:
            left = construct_optimal_parens(s, i, s[i][j])
            right = construct_optimal_parens(s, s[i][j] + 1, j)
            return f"({left} x {right})"

    optimal_parens_str = construct_optimal_parens(s, 1, n)
    return m, s, m[1][n], optimal_parens_str


def print_matrix_table(table, name, n):
    """Prints the upper triangular cost or split table."""
    print(f"\n{name} Matrix (1-indexed):")
    header = "     " + " ".join(f"Col {j:2d}" for j in range(1, n + 1))
    print(header)
    print("-" * len(header))
    for i in range(1, n + 1):
        row_str = f"Row {i:2d} |"
        for j in range(1, n + 1):
            if j < i:
                row_str += "       "
            else:
                row_str += f" {table[i][j]:6d}"
        print(row_str)


def main():
    print("=" * 70)
    print("PRACTICAL 06: CHAIN MATRIX MULTIPLICATION (DYNAMIC PROGRAMMING)")
    print("=" * 70)

    # Matrix dimensions:
    # A1: 10 x 20, A2: 20 x 30, A3: 30 x 40, A4: 40 x 30
    p = [10, 20, 30, 40, 30]
    num_matrices = len(p) - 1

    print(f"Dimension Array p: {p}")
    print("Matrices to multiply:")
    for i in range(1, num_matrices + 1):
        print(f"  Matrix A{i}: {p[i - 1]} x {p[i]}")
    print()

    # Measure execution time
    start_time = time.perf_counter()
    m_table, s_table, min_cost, optimal_parens = matrix_chain_order(p)
    end_time = time.perf_counter()

    exec_time = end_time - start_time

    # Display tables
    print_matrix_table(m_table, "Minimum Cost (M)", num_matrices)
    print_matrix_table(s_table, "Optimal Split (S)", num_matrices)

    print("\n" + "-" * 50)
    print("OPTIMAL SOLUTION:")
    print("-" * 50)
    print(f"Minimum Scalar Multiplications Cost : {min_cost}")
    print(f"Optimal Parenthesization Order      : {optimal_parens}")
    print(f"Execution Time                      : {exec_time:.8f} seconds ({exec_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - O(n^3), where n is the number of matrices (three nested loops).")
    print("  Space Complexity:")
    print("    - O(n^2) auxiliary space for the DP cost and split tables.")
    print("=" * 70)


if __name__ == "__main__":
    main()
