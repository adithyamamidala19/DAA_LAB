# Practical 05: 0/1 Knapsack Problem using Dynamic Programming

## 1. Practical Number
**Practical 05**

## 2. Practical Name
**Implementation of 0/1 Knapsack Problem using Dynamic Programming**

## 3. Objective
To solve the classic 0/1 Knapsack optimization problem using Dynamic Programming (Bottom-Up Tabulation), construct the DP state table, find the maximum attainable value within a given capacity constraint, reconstruct the subset of selected items, measure execution time, and evaluate time and space complexity.

---

## 4. Problem Statement
Given $n$ items, each with a given weight $w_i$ and value $v_i$, and a knapsack with maximum weight capacity $W$, select a subset of items such that:
1. The total weight does not exceed $W$: $\sum w_i \le W$.
2. The total value is maximized: $\max \sum v_i$.
3. Each item can either be taken (1) or not taken (0) — no fractional items are allowed.

---

## 5. Algorithm Explanation

### A. Principle of Optimality & DP State
Let $dp[i][w]$ represent the maximum value attainable using a subset of the first $i$ items with a maximum allowable capacity $w$.

### B. Recurrence Relation
For $i = 1 \dots n$ and $w = 1 \dots W$:
$$dp[i][w] = \begin{cases} 
\max(v_{i-1} + dp[i-1][w - w_{i-1}],\; dp[i-1][w]) & \text{if } w_{i-1} \le w \\
dp[i-1][w] & \text{if } w_{i-1} > w 
\end{cases}$$

- **Base Cases**: $dp[0][w] = 0$ for all $w$, and $dp[i][0] = 0$ for all $i$.

### C. Solution Reconstruction (Backtracking)
To find which items were selected:
- Start from $(n, W)$.
- If $dp[i][w] \neq dp[i-1][w]$, item $i-1$ was selected: record it and reduce $w \leftarrow w - w_{i-1}$.
- Decrement $i \leftarrow i - 1$ until $i = 0$.

---

## 6. Step-by-Step Working

1. **Given Data**:
   - Weights: `[2, 3, 4, 5]`
   - Values: `[3, 4, 5, 6]`
   - Capacity $W = 5$
2. **DP Matrix Construction**:
   - Build table of size $(4+1) \times (5+1)$.
   - Fill row by row evaluating inclusion vs exclusion.
3. **Optimum Value**:
   - Stored at $dp[4][5] = 7$ (formed by Item 1 of weight 2, value 3 + Item 2 of weight 3, value 4).
4. **Time & Metric Recording**: Execution runtime measured using `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_05_Knapsack_DP.py`

---

## 8. Sample Input
```python
item_names = ["Item 1 (Laptop)", "Item 2 (Camera)", "Item 3 (Watch)", "Item 4 (Headphones)"]
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 05: 0/1 KNAPSACK USING DYNAMIC PROGRAMMING
======================================================================
Knapsack Capacity (W) : 5
Items Available:
  [0] Item 1 (Laptop)      -> Weight: 2, Value: 3
  [1] Item 2 (Camera)      -> Weight: 3, Value: 4
  [2] Item 3 (Watch)       -> Weight: 4, Value: 5
  [3] Item 4 (Headphones)  -> Weight: 5, Value: 6

DP Tabulation Matrix (Rows: Items 0..n, Columns: Capacity 0..W):
Item \ W |    0    1    2    3    4    5
------------------------------------------
Item  0  |    0    0    0    0    0    0
Item  1  |    0    0    3    3    3    3
Item  2  |    0    0    3    4    4    7
Item  3  |    0    0    3    4    5    7
Item  4  |    0    0    3    4    5    7

--------------------------------------------------
OPTIMAL SOLUTION:
--------------------------------------------------
Maximum Total Value Achieved : 7
Selected Items:
  - Item 1 (Laptop) (Weight: 2, Value: 3)
  - Item 2 (Camera) (Weight: 3, Value: 4)
Total Weight Used            : 5 / 5
Execution Time               : 0.00002140 seconds (0.0214 ms)

Complexity Analysis:
  Time Complexity:
    - O(n * W), where 'n' is number of items and 'W' is knapsack capacity.
  Space Complexity:
    - O(n * W) auxiliary space for DP table (can be optimized to O(W) with 1D array).
======================================================================
```

---

## 10. Time Complexity Analysis

| Scenario | Complexity | Explanation |
| :--- | :--- | :--- |
| **Tabulation Filling** | $O(n \times W)$ | Table of size $(n+1) \times (W+1)$ filled in constant $O(1)$ operations per cell. |
| **Backtracking Items** | $O(n)$ | Traverses at most $n$ rows. |
| **Total Time Complexity** | $O(n \times W)$ | Pseudo-polynomial time complexity. |

---

## 11. Space Complexity Analysis

- **2D Tabulation Space**: $O(n \times W)$ memory cells to hold the subproblem solutions and allow backtracking.
- **Space-Optimized Alternative**: $O(W)$ if only the maximum value is required (using a single 1D array traversed backwards).

---

## 12. Explanation of Execution-Time Measurement
Execution time is computed using `time.perf_counter()` encapsulating table construction and solution reconstruction:
```python
start_time = time.perf_counter()
max_val, chosen_indices, dp_table = knapsack_01_dp(weights, values, capacity)
end_time = time.perf_counter()
exec_time = end_time - start_time
```

---

## 13. Expected Result
The maximum attainable value is **7** with total weight **5** by selecting Item 1 and Item 2.

---

## 14. Important Concepts Used
- **Overlapping Subproblems & Optimal Substructure**: Defining traits of Dynamic Programming.
- **0/1 Decision Property**: An item is either wholly included or wholly excluded.
- **Backtracking from DP Table**: Tracing predecessor cells to reconstruct the optimal decision path.
