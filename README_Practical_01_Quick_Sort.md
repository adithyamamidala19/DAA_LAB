# Practical 01: Quick Sort Algorithm

## 1. Practical Number
**Practical 01**

## 2. Practical Name / Topic Name
**Quick Sort Algorithm (Implementation and Time Analysis)**

## 3. Objective
To implement Quick Sort in Python using the Divide-and-Conquer paradigm, sort an unsorted numeric array in ascending order, measure its actual execution time using `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given an array of $n$ numbers, sort the list efficiently by selecting a pivot, partitioning the array such that smaller elements lie on the left and larger on the right, and recursively sorting the partitions.

---

## 5. Algorithm Explanation

### Core Logic
1. **Pivot Selection**: Choose a pivot element (e.g., median or middle element $A[\lfloor n/2 \rfloor]$).
2. **Partitioning**: Rearrange the array into three segments:
   - `left`: Elements strictly less than `pivot`.
   - `middle`: Elements equal to `pivot`.
   - `right`: Elements strictly greater than `pivot`.
3. **Recursive Sorting**: Recursively sort `left` and `right`.
4. **Concatenation**: Combine `quick_sort(left) + middle + quick_sort(right)`.

---

## 6. Step-by-Step Working

1. **Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
2. **Pivot**: Choose middle element `22` or `11`.
3. **Partition**:
   - Elements $< 22$: `[12, 11, 18]`
   - Elements $== 22$: `[22]`
   - Elements $> 22$: `[64, 34, 25, 90, 42, 55]`
4. **Recursive Sub-calls**: Sorts `[12, 11, 18]` $\to$ `[11, 12, 18]`, and right partition $\to$ `[25, 34, 42, 55, 64, 90]`.
5. **Output**: Returns concatenated result `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`.

---

## 7. Python Implementation File Name
`Practical_01_Quick_Sort.py`

---

## 8. Sample Input
```python
sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 01: QUICK SORT ALGORITHM
======================================================================
Original Input Array : [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]

Sorted Array         : [11, 12, 18, 22, 25, 34, 42, 55, 64, 90]
Execution Time       : 0.00001710 seconds (0.0171 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(n log n) [When pivot partitions array into equal halves]
    - Average Case : O(n log n)
    - Worst Case   : O(n^2) [When partition is extremely unbalanced, e.g. 0 and n-1]
  Space Complexity:
    - Auxiliary Space : O(log n) [Recursion call stack in balanced cases]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Condition | Time Complexity |
| :--- | :--- | :--- |
| **Best Case** | Balanced partition: $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| **Average Case** | Random pivot behavior: $O(n \log n)$ average comparisons | $O(n \log n)$ |
| **Worst Case** | Skewed partition: $T(n) = T(n-1) + O(n)$ | $O(n^2)$ |

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(\log n)$ recursion stack frames for balanced partitions ($O(n)$ in worst-case degenerate recursion).

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` captures high-precision timing before and after calling `quick_sort()`:
```python
start_time = time.perf_counter()
sorted_array = quick_sort(sample_data)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
The input array is correctly sorted into `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`.

---

## 14. Important Concepts Used
- **Divide and Conquer**: Partition around pivot.
- **Pivot Selection**: Impact of pivot on recurrence balance.
- **Cache Efficiency**: Small constant factors making it one of the fastest practical sorting algorithms.
