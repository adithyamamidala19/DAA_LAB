# Practical 04: Recursive Factorial Algorithm

## 1. Practical Number
**Practical 04**

## 2. Practical Name / Topic Name
**Factorial Program — Recursive Method (Implementation and Time Analysis)**

## 3. Objective
To implement the factorial function using recursion in Python, calculate $n!$, measure execution time using `time.perf_counter()`, and analyze its theoretical time complexity and auxiliary space complexity (call stack depth).

---

## 4. Problem Statement
Given a non-negative integer $n$, calculate $n!$ using a recursive function based on the mathematical recurrence relation.

---

## 5. Algorithm Explanation

### Core Logic
Recursion breaks down a problem into identical smaller instances:
- **Base Case**: If $n = 0$ or $n = 1$, return $1$.
- **Recursive Step**: For $n > 1$, return $n \times \text{factorial\_recursive}(n - 1)$.

### Recurrence Relation
$$T(n) = T(n - 1) + O(1) \implies T(n) = O(n)$$

---

## 6. Step-by-Step Working

1. **Input**: $n = 20$.
2. **Call Chain Expansion**:
   - `fact(20)` $\to 20 \times \text{fact}(19)$
   - `fact(19)` $\to 19 \times \text{fact}(18)$
   - $\dots$
   - `fact(1)` $\to 1$ (Base case).
3. **Stack Unwinding**:
   - Returns multiply upwards to compute $2432902008176640000$.
4. **Timing**: Measured via `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_04_Recursive_Factorial.py`

---

## 8. Sample Input
```python
n = 20
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 04: FACTORIAL (RECURSIVE METHOD)
======================================================================
Input Number (n) : 20

Calculated Factorial (20!) : 2432902008176640000
Execution Time              : 0.00000350 seconds (0.0035 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(1) [When n = 0 or 1]
    - Average Case : O(n) [T(n) = T(n-1) + O(1)]
    - Worst Case   : O(n)
  Space Complexity:
    - Auxiliary Space : O(n) [Due to n stack frames on the recursion call stack]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Condition | Time Complexity |
| :--- | :--- | :--- |
| **Best Case** | $n \le 1$ | $O(1)$ |
| **Average Case** | $n > 1$ ($n$ recursive activations) | $O(n)$ |
| **Worst Case** | Arbitrary $n$ | $O(n)$ |

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(n)$ auxiliary memory on the system call stack due to $n$ activation frames.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` records execution duration across recursive calls:
```python
start_time = time.perf_counter()
result = factorial_recursive(n)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
For $n = 20$, returns `2432902008176640000`.

---

## 14. Important Concepts Used
- **Base Case Validation**: Essential for preventing infinite recursion / stack overflow.
- **Activation Records (Stack Frames)**: Pushed during calls, popped on returns.
- **Recursion Limits**: In Python, managed via `sys.setrecursionlimit()`.
