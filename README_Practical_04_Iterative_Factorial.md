# Practical 04: Iterative Factorial Algorithm

## 1. Practical Number
**Practical 04**

## 2. Practical Name / Topic Name
**Factorial Program — Iterative Method (Implementation and Time Analysis)**

## 3. Objective
To implement the factorial function using a loop-based iterative algorithm in Python, compute $n!$, measure execution runtime using `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given a non-negative integer $n$, compute its factorial $n! = 1 \times 2 \times 3 \times \dots \times n$ (with $0! = 1$) without using recursion.

---

## 5. Algorithm Explanation

### Core Logic
1. If $n < 0$, raise an invalid input exception.
2. If $n = 0$ or $n = 1$, return $1$.
3. Initialize an accumulator variable `result = 1`.
4. Loop $i$ from $2$ to $n$:
   - Multiply `result *= i`.
5. Return `result`.

---

## 6. Step-by-Step Working

1. **Input**: $n = 20$.
2. **Loop Execution**:
   - $i=2 \implies result = 2$
   - $i=3 \implies result = 6$
   - $\dots$
   - $i=20 \implies result = 2432902008176640000$.
3. **Timing**: Monitored using `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_04_Iterative_Factorial.py`

---

## 8. Sample Input
```python
n = 20
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 04: FACTORIAL (ITERATIVE METHOD)
======================================================================
Input Number (n) : 20

Calculated Factorial (20!) : 2432902008176640000
Execution Time              : 0.00000280 seconds (0.0028 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(1) [When n = 0 or 1]
    - Average Case : O(n) [Performs n-1 multiplications]
    - Worst Case   : O(n)
  Space Complexity:
    - Auxiliary Space : O(1) [Requires only a single accumulator variable]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Condition | Time Complexity |
| :--- | :--- | :--- |
| **Best Case** | $n = 0$ or $n = 1$ | $O(1)$ |
| **Average Case** | $n > 1$ ($n-1$ loop iterations) | $O(n)$ |
| **Worst Case** | Arbitrary positive integer $n$ | $O(n)$ |

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(1)$ (Only one integer accumulator in memory).

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` surrounds the iterative function call:
```python
start_time = time.perf_counter()
result = factorial_iterative(n)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
For $n = 20$, returns `2432902008176640000`.

---

## 14. Important Concepts Used
- **Loop-based State Accumulation**: Efficient linear multiplication.
- **Constant Memory Footprint**: Eliminates stack frame creation overhead.
