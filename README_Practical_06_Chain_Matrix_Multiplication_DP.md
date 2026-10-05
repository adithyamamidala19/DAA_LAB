# Practical 06: Matrix Chain Multiplication using Dynamic Programming

## 1. Practical Number
**Practical 06**

## 2. Practical Name
**Implementation of Chain Matrix Multiplication using Dynamic Programming**

## 3. Objective
To implement the Matrix Chain Multiplication (MCM) problem using Dynamic Programming, determine the minimum number of scalar multiplications required to multiply a chain of matrices, output the optimal parenthesization order, measure execution runtime, and evaluate time and space complexities.

---

## 4. Problem Statement
Given a sequence of $n$ matrices $\langle A_1, A_2, \dots, A_n \rangle$ where matrix $A_i$ has dimension $p_{i-1} \times p_i$, determine the parenthesization of the product $A_1 A_2 \dots A_n$ that minimizes the total count of scalar multiplications.

---

## 5. Algorithm Explanation

### A. Problem Characteristics
Matrix multiplication is associative $((AB)C = A(BC))$, but the number of scalar multiplications depends heavily on parenthesization order:
- If $A$ is $10 \times 100$, $B$ is $100 \times 5$, and $C$ is $5 \times 50$:
  - $(AB)C$ costs $(10 \times 100 \times 5) + (10 \times 5 \times 50) = 5,000 + 2,500 = 7,500$ multiplications.
  - $A(BC)$ costs $(100 \times 5 \times 50) + (10 \times 100 \times 50) = 25,000 + 50,000 = 75,000$ multiplications (10x slower).

### B. Recurrence Formulation
Let $m[i][j]$ denote the minimum number of scalar multiplications needed to compute $A_i \dots A_j$:
$$m[i][j] = \begin{cases}
0 & \text{if } i = j \\
\min_{i \le k < j} \left( m[i][k] + m[k+1][j] + p_{i-1} p_k p_j \right) & \text{if } i < j
\end{cases}$$

### C. Split Tracking ($s$-table)
Let $s[i][j]$ store the index $k$ that achieves the minimum cost for subchain $A_i \dots A_j$.

### D. Bottom-Up Computation (By Chain Length $L$)
Subproblems are solved in order of increasing chain length $L = 2, 3, \dots, n$, ensuring subproblems $m[i][k]$ and $m[k+1][j]$ are already computed before computing $m[i][j]$.

---

## 6. Step-by-Step Working

1. **Input Dimensions**: $p = [10, 20, 30, 40, 30]$ (4 matrices: $A_1: 10\times 20, A_2: 20\times 30, A_3: 30\times 40, A_4: 40\times 30$).
2. **Chain Lengths**:
   - $L = 1$: $m[i][i] = 0$.
   - $L = 2$: Compute for chains of length 2 ($A_1 A_2, A_2 A_3, A_3 A_4$).
   - $L = 3$: Compute for chains of length 3 ($A_1 \dots A_3, A_2 \dots A_4$).
   - $L = 4$: Compute for full chain $A_1 \dots A_4$.
3. **Parenthesization Generation**: Recursively traverse $s[1][n]$ to construct string formatted as `((A1 x (A2 x A3)) x A4)`.
4. **Timing**: Measured using `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_06_Chain_Matrix_Multiplication_DP.py`

---

## 8. Sample Input
```python
p = [10, 20, 30, 40, 30]
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 06: CHAIN MATRIX MULTIPLICATION (DYNAMIC PROGRAMMING)
======================================================================
Dimension Array p: [10, 20, 30, 40, 30]
Matrices to multiply:
  Matrix A1: 10 x 20
  Matrix A2: 20 x 30
  Matrix A3: 30 x 40
  Matrix A4: 40 x 30


Minimum Cost (M) Matrix (1-indexed):
     Col  1 Col  2 Col  3 Col  4
--------------------------------
Row  1 |      0   6000  18000  30000
Row  2 |             0  24000  48000
Row  3 |                    0  36000
Row  4 |                           0

Optimal Split (S) Matrix (1-indexed):
     Col  1 Col  2 Col  3 Col  4
--------------------------------
Row  1 |      0      1      1      3
Row  2 |             0      2      3
Row  3 |                    0      3
Row  4 |                           0

--------------------------------------------------
OPTIMAL SOLUTION:
--------------------------------------------------
Minimum Scalar Multiplications Cost : 30000
Optimal Parenthesization Order      : (((A1 x A2) x A3) x A4)
Execution Time                      : 0.00003420 seconds (0.0342 ms)

Complexity Analysis:
  Time Complexity:
    - O(n³), where n is the number of matrices (three nested loops).
  Space Complexity:
    - O(n²) auxiliary space for the DP cost and split tables.
======================================================================
```

---

## 10. Time Complexity Analysis

- **Nested Loops Structure**:
  - Outer loop for chain length $L$: $2 \dots n \implies O(n)$
  - Middle loop for chain start index $i$: $1 \dots n - L + 1 \implies O(n)$
  - Inner loop for split point $k$: $i \dots j - 1 \implies O(n)$
- **Total Time Complexity**: $O(n^3)$ operations.

---

## 11. Space Complexity Analysis

- **$m$-table & $s$-table**: Two 2D matrices of size $(n+1) \times (n+1)$.
- **Auxiliary Space Complexity**: $O(n^2)$.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` is called around the `matrix_chain_order()` function:
```python
start_time = time.perf_counter()
m_table, s_table, min_cost, optimal_parens = matrix_chain_order(p)
end_time = time.perf_counter()
exec_time = end_time - start_time
```

---

## 13. Expected Result
For matrix chain dimensions `[10, 20, 30, 40, 30]`, the minimum scalar multiplication cost is **30,000**, and the optimal grouping is `(((A1 x A2) x A3) x A4)`.

---

## 14. Important Concepts Used
- **Catalan Numbers**: Number of possible parenthesizations grows exponentially as $C(n-1) = \frac{1}{n} \binom{2n-2}{n-1} = \Omega\left(\frac{4^n}{n^{3/2}}\right)$, necessitating Dynamic Programming.
- **Optimal Substructure**: An optimal parenthesization of $A_i \dots A_j$ splits at $k$ contains optimal parenthesizations of $A_i \dots A_k$ and $A_{k+1} \dots A_j$.
- **Chain Length Ordering**: Solving smaller subchains first so that larger subchains can reference already-computed values.
