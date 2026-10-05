# Practical 02: Binary Search Algorithm

## 1. Practical Number
**Practical 02**

## 2. Practical Name / Topic Name
**Binary Search Algorithm (Implementation and Time Analysis)**

## 3. Objective
To implement Binary Search in Python (both iterative and recursive methods), perform search operations on a sorted array for present and absent target elements, measure execution time with `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given a sorted array $A$ of $n$ elements in non-decreasing order and a target key $K$, find the index of $K$ in $O(\log n)$ logarithmic time. If $K$ is not present, return $-1$.

---

## 5. Algorithm Explanation

### Core Logic
Binary Search employs the Divide-and-Conquer strategy on an ordered list:
1. Maintain two pointers: $low = 0$ and $high = n - 1$.
2. While $low \le high$:
   - Calculate midpoint $mid = low + \lfloor (high - low)/2 \rfloor$.
   - If $A[mid] == K$, return $mid$.
   - If $A[mid] < K$, search the right subarray: $low = mid + 1$.
   - If $A[mid] > K$, search the left subarray: $high = mid - 1$.
3. If $low > high$, target does not exist; return $-1$.

---

## 6. Step-by-Step Working

1. **Sorted Input**: `[11, 12, 23, 34, 45, 56, 67, 78, 89, 90]` ($n = 10$).
2. **Case 1 (Target = 67)**:
   - Iteration 1: $low=0, high=9, mid=4$ ($A[4]=45$). Since $45 < 67 \implies low = 5$.
   - Iteration 2: $low=5, high=9, mid=7$ ($A[7]=78$). Since $78 > 67 \implies high = 6$.
   - Iteration 3: $low=5, high=6, mid=5$ ($A[5]=56$). Since $56 < 67 \implies low = 6$.
   - Iteration 4: $low=6, high=6, mid=6$ ($A[6]=67$). **Match found at index 6**.
3. **Case 2 (Target = 99)**:
   - Interval narrows until $low > high$, returning $-1$.
4. **Timing**: Measured using `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_02_Binary_Search.py`

---

## 8. Sample Input
```python
sorted_dataset = [11, 12, 23, 34, 45, 56, 67, 78, 89, 90]
target_present = 67
target_absent = 99
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 02: BINARY SEARCH ALGORITHM
======================================================================
Sorted Dataset : [11, 12, 23, 34, 45, 56, 67, 78, 89, 90]

[Test Case 1: Searching for target = 67 (Present)]
  Result         : Target 67 found at index 6 (Position 7)
  Execution Time : 0.00000150 seconds (0.0015 ms)

[Test Case 2: Searching for target = 99 (Absent)]
  Result         : Target 99 not found in dataset (returned -1)
  Execution Time : 0.00000090 seconds (0.0009 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(1) [When target is the middle element]
    - Average Case : O(log n)
    - Worst Case   : O(log n) [When target is at extreme or absent]
  Space Complexity:
    - Iterative Approach : O(1) [Auxiliary space]
    - Recursive Approach : O(log n) [Call stack frames]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Condition | Time Complexity |
| :--- | :--- | :--- |
| **Best Case** | Target is at exact initial middle index | $O(1)$ |
| **Average Case** | Target found after intermediate interval splits | $O(\log n)$ |
| **Worst Case** | Target at interval ends or not present ($\log_2 n$ splits) | $O(\log n)$ |

---

## 11. Space Complexity Analysis
- **Iterative Approach**: $O(1)$ auxiliary memory.
- **Recursive Approach**: $O(\log n)$ call stack frames.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` wraps the search call:
```python
start_time = time.perf_counter()
index = binary_search_iterative(sorted_dataset, target)
end_time = time.perf_counter()
exec_time = end_time - start_time
```

---

## 13. Expected Result
- Target `67` is located at index 6.
- Target `99` returns `-1`.

---

## 14. Important Concepts Used
- **Logarithmic Reduction**: Halves search space at each iteration.
- **Precondition of Sorted Order**: Monotonicity is essential.
- **Overflow-Safe Midpoint**: $low + \lfloor(high - low)/2\rfloor$.
