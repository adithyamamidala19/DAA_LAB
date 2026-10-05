# Practical 07: Making Change Problem using Dynamic Programming

## 1. Practical Number
**Practical 07**

## 2. Practical Name
**Implementation of Making Change Problem using Dynamic Programming**

## 3. Objective
To solve the Making Change / Coin Change problem using Dynamic Programming (Bottom-Up Tabulation), determine the minimum number of coins needed to make a target amount, reconstruct the selected coin denominations, gracefully handle impossible amounts, measure execution time, and analyze time/space complexities.

---

## 4. Problem Statement
Given an unlimited supply of coins of denominations $C = \{c_1, c_2, \dots, c_n\}$ and a target amount $V$, find the minimum number of coins required to form the total amount $V$. If the amount cannot be made by any combination of the coins, return $-1$ (Impossible).

---

## 5. Algorithm Explanation

### A. Why Greedy Can Fail
While the standard canonical currency systems (e.g., US or Indian currency: 1, 2, 5, 10, 20, 50, 100) allow a greedy choice, arbitrary coin denominations can cause greedy algorithms to fail.
- *Example*: Coins = $\{1, 5, 6, 8\}$, Target = $11$
  - Greedy choice: $8 + 1 + 1 + 1 = 11$ (4 coins).
  - DP optimal choice: $5 + 6 = 11$ (2 coins).
- Hence, Dynamic Programming guarantees the globally optimal solution.

### B. Dynamic Programming Formulation
Let $dp[a]$ be the minimum number of coins needed to make amount $a$.

### C. Recurrence Relation
$$dp[a] = \begin{cases}
0 & \text{if } a = 0 \\
\min_{c \in C, c \le a} (dp[a - c] + 1) & \text{if } a > 0
\end{cases}$$

- **Initialization**: $dp[0] = 0$ and $dp[a] = \infty$ (or $amount + 1$) for $a > 0$.
- **Tracking Chosen Coins**: Array $parent[a]$ stores the coin $c$ that achieved the minimum value for amount $a$.

---

## 6. Step-by-Step Working

1. **Input**:
   - Case 1: Coins `[1, 2, 5, 10, 20, 50]`, Target = 43.
   - Case 2: Coins `[1, 5, 6, 8]`, Target = 11 (Demonstrating non-greedy optimality).
   - Case 3: Coins `[2, 4, 6]`, Target = 7 (Demonstrating impossible change).
2. **Tabulation**:
   - Iterate $a$ from $1$ to target.
   - For each coin $c \le a$, check if $dp[a - c] + 1 < dp[a]$. If so, update $dp[a]$ and $parent[a] = c$.
3. **Reconstruction**:
   - Start from $curr = amount$, trace back using $parent[curr]$ until $curr = 0$.
4. **Timing**: Monitored using `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_07_Coin_Change_DP.py`

---

## 8. Sample Input
```python
coins1 = [1, 2, 5, 10, 20, 50]
target1 = 43

coins2 = [1, 5, 6, 8]
target2 = 11

coins3 = [2, 4, 6]
target3 = 7
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 07: COIN CHANGE / MAKING CHANGE (DYNAMIC PROGRAMMING)
======================================================================
Coin Denominations Available : [1, 2, 5, 10, 20, 50]
Target Amount                : 43

[Case 1: Standard Test]
  Minimum Coins Required : 4
  Coins Chosen           : [1, 2, 20, 20] (Sum = 43)
  Execution Time         : 0.00001820 seconds (0.0182 ms)

[Case 2: Denominations where Greedy is Suboptimal]
  Coin Denominations Available : [1, 5, 6, 8]
  Target Amount                : 11
  Minimum Coins Required : 2 (e.g., 5 + 6 = 11 using 2 coins)
  Coins Chosen           : [5, 6]
  Execution Time         : 0.00000670 seconds (0.0067 ms)

[Case 3: Impossible Change Test]
  Coin Denominations Available : [2, 4, 6]
  Target Amount                : 7
  Result                 : Change is IMPOSSIBLE (No valid combination exists).
  Execution Time         : 0.00000510 seconds (0.0051 ms)

======================================================================
Complexity Analysis:
  Time Complexity:
    - O(n * Amount), where 'n' is number of coin denominations and 'Amount' is target.
  Space Complexity:
    - O(Amount) auxiliary space for the DP array.
======================================================================
```

---

## 10. Time Complexity Analysis

- **DP State Calculation**: We compute values for $1 \dots \text{Amount}$, and for each amount, check up to $n$ coin denominations.
- **Total Time Complexity**: $O(n \times \text{Amount})$ where $n = |C|$.

---

## 11. Space Complexity Analysis

- **DP Table & Parent Array**: 1D array of size $(\text{Amount} + 1)$.
- **Auxiliary Space Complexity**: $O(\text{Amount})$.

---

## 12. Explanation of Execution-Time Measurement
Runtime is recorded with `time.perf_counter()` directly before and after the DP function invocation:
```python
start_time = time.perf_counter()
min_count, used, dp_table = min_coins_change(coins, target)
end_time = time.perf_counter()
exec_time = end_time - start_time
```

---

## 13. Expected Result
- Target 43 with standard coins requires **4 coins** ($20 + 20 + 2 + 1$).
- Target 11 with coins `[1, 5, 6, 8]` requires **2 coins** ($5 + 6$).
- Target 7 with coins `[2, 4, 6]` correctly reports impossible ($-1$).

---

## 14. Important Concepts Used
- **Unbounded Knapsack Variation**: Multiple instances of any coin denomination may be chosen.
- **Bottom-Up State Transitions**: Solving all smaller amounts $0 \dots a-1$ before resolving amount $a$.
- **Path Backtracking**: Maintaining predecessor links to retrieve exact solution choices.
