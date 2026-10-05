# Practical 01: Selection Sort Algorithm

## 1. Practical Number
**Practical 01**

## 2. Practical Name / Topic Name
**Selection Sort Algorithm (Implementation and Time Analysis)**

## 3. Objective
To implement Selection Sort in Python, sort an unsorted numeric array in ascending order, measure its actual execution time using `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given an array of $n$ numbers, sort the list by repeatedly finding the smallest element from the unsorted region and placing it at the beginning.

---

## 5. Algorithm Explanation

### Core Logic
Selection Sort divides the array into two logical parts:
1. **Sorted sublist** at the left end.
2. **Unsorted sublist** at the right end.

In each iteration $i$ from $0$ to $n-1$:
- Searches the unsorted subarray $A[i \dots n-1]$ to identify the minimum element index `min_idx`.
- Swaps $A[i]$ with $A[\text{min\_idx}]$, moving the smallest element into the sorted sublist.
- Performs at most $n-1$ swaps across the entire sorting process.

---

## 6. Step-by-Step Working

1. **Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
2. **Iteration 0**: Finds smallest `11` at index 5, swaps with `64` $\to$ `[11, 34, 25, 12, 22, 64, 90, 42, 18, 55]`.
3. **Iteration 1**: Finds next smallest `12` at index 3, swaps with `34`.
4. **Iterations 2 to $n-1$**: Continues scanning unsorted suffixes and placing minimum elements in position.
5. **Output**: Returns the fully sorted array.

---

## 7. Python Implementation File Name
`Practical_01_Selection_Sort.py`

---

## 8. Sample Input
```python
sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 01: SELECTION SORT ALGORITHM
======================================================================
Original Input Array : [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]

Sorted Array         : [11, 12, 18, 22, 25, 34, 42, 55, 64, 90]
Execution Time       : 0.00001080 seconds (0.0108 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(n^2) [Always performs n(n-1)/2 comparisons]
    - Average Case : O(n^2)
    - Worst Case   : O(n^2)
  Space Complexity:
    - Auxiliary Space : O(1) [In-place comparison sort]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Condition | Time Complexity |
| :--- | :--- | :--- |
| **Best Case** | Regardless of array order (comparisons are always made) | $O(n^2)$ |
| **Average Case** | Random order | $O(n^2)$ |
| **Worst Case** | Reverse order | $O(n^2)$ |

- Total comparisons: $\sum_{i=1}^{n-1} i = \frac{n(n-1)}{2} = \Theta(n^2)$.
- Total swaps: At most $O(n)$ swaps.

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(1)$ (In-place sort).

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` is called around the `selection_sort()` function:
```python
start_time = time.perf_counter()
sorted_array = selection_sort(sample_data)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
The input array is correctly sorted into `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`.

---

## 14. Important Concepts Used
- **Minimum Element Selection**: Linear scanning of unsorted suffixes.
- **Minimum Swap Count**: Makes only $O(n)$ writes to memory, advantageous when memory write costs are high.
- **Non-Adaptive Nature**: Performs the same number of comparisons regardless of initial ordering.
