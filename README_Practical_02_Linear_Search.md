# Practical 02: Linear Search Algorithm

## 1. Practical Number
**Practical 02**

## 2. Practical Name / Topic Name
**Linear Search Algorithm (Implementation and Time Analysis)**

## 3. Objective
To implement Linear Search in Python, search for present and absent target keys in an unordered dataset, measure actual execution time using `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given an array $A$ of $n$ elements and a target key $K$, determine whether $K$ exists in $A$. If found, return its index; otherwise, return $-1$.

---

## 5. Algorithm Explanation

### Core Logic
Linear Search sequentially inspects each element of the collection:
1. Start from index $i = 0$.
2. Compare $A[i]$ with target $K$.
3. If $A[i] == K$, return $i$ immediately.
4. If $i < n-1$, increment $i$ by 1 and repeat from Step 2.
5. If the loop completes without finding a match, return $-1$.

---

## 6. Step-by-Step Working

1. **Input**: `dataset = [45, 12, 89, 34, 67, 23, 78, 90, 11, 56]`
2. **Case 1 (Target = 67)**:
   - Index 0: 45 $\ne$ 67
   - Index 1: 12 $\ne$ 67
   - Index 2: 89 $\ne$ 67
   - Index 3: 34 $\ne$ 67
   - Index 4: 67 $==$ 67 $\implies$ **Match found at index 4**.
3. **Case 2 (Target = 99)**:
   - Compares all 10 elements $\implies$ No match found, returns $-1$.
4. **Timing**: Measures execution time using `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_02_Linear_Search.py`

---

## 8. Sample Input
```python
dataset = [45, 12, 89, 34, 67, 23, 78, 90, 11, 56]
target_present = 67
target_absent = 99
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 02: LINEAR SEARCH ALGORITHM
======================================================================
Dataset : [45, 12, 89, 34, 67, 23, 78, 90, 11, 56]

[Test Case 1: Searching for target = 67 (Present)]
  Result         : Target 67 found at index 4 (Position 5)
  Execution Time : 0.00000210 seconds (0.0021 ms)

[Test Case 2: Searching for target = 99 (Absent)]
  Result         : Target 99 not found in dataset (returned -1)
  Execution Time : 0.00000180 seconds (0.0018 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(1) [When target is the first element]
    - Average Case : O(n) [When target is in the middle]
    - Worst Case   : O(n) [When target is at the end or not present]
  Space Complexity:
    - Auxiliary Space : O(1) [Constant memory overhead]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Condition | Comparisons | Time Complexity |
| :--- | :--- | :--- | :--- |
| **Best Case** | Target at index 0 | $1$ | $O(1)$ |
| **Average Case** | Target randomly distributed | $(n+1)/2$ | $O(n)$ |
| **Worst Case** | Target at index $n-1$ or not present | $n$ | $O(n)$ |

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(1)$ (No additional memory required beyond iteration variables).

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` is used to wrap search invocations:
```python
start_time = time.perf_counter()
index = linear_search(dataset, target)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
- Target `67` is found at index 4.
- Target `99` is reported as absent ($-1$).

---

## 14. Important Concepts Used
- **Exhaustive / Sequential Search**: Inspecting every item sequentially.
- **No Ordering Precondition**: Can operate directly on unsorted, arbitrary datasets.
