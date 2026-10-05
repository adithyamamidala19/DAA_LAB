# Practical 01: Merge Sort Algorithm

## 1. Practical Number
**Practical 01**

## 2. Practical Name / Topic Name
**Merge Sort Algorithm (Implementation and Time Analysis)**

## 3. Objective
To implement Merge Sort in Python using the Divide-and-Conquer paradigm, sort an unsorted numeric array in ascending order, measure its actual execution time using `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given an array of $n$ numbers, sort the elements in non-decreasing order by dividing the array into two halves, recursively sorting both, and merging the sorted sub-arrays.

---

## 5. Algorithm Explanation

### Core Logic
Merge Sort follows the three classical steps of Divide and Conquer:
1. **Divide**: Find the midpoint $mid = \lfloor n/2 \rfloor$ and divide array $A$ into $L = A[0 \dots mid]$ and $R = A[mid \dots n]$.
2. **Conquer**: Recursively sort sub-arrays $L$ and $R$.
3. **Combine (Merge)**: Merge the two sorted lists $L$ and $R$ by maintaining pointers $i$ and $j$, copying the smaller of $L[i]$ and $R[j]$ into a new merged list until all elements are exhausted.

### Recurrence Relation
$$T(n) = 2T(n/2) + \Theta(n) \implies T(n) = \Theta(n \log n)$$
by the Master Theorem (Case 2).

---

## 6. Step-by-Step Working

1. **Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
2. **Divide**: Splits into `[64, 34, 25, 12, 22]` and `[11, 90, 42, 18, 55]`.
3. **Recursive Halving**: Splits until 10 individual single-element arrays remain.
4. **Merge Phase**:
   - `[64]` and `[34]` merge into `[34, 64]`.
   - `[12]` and `[22]` merge into `[12, 22]`.
   - Merges progressively larger sorted halves until a single sorted list is produced.
5. **Output**: Returns `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`.

---

## 7. Python Implementation File Name
`Practical_01_Merge_Sort.py`

---

## 8. Sample Input
```python
sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 01: MERGE SORT ALGORITHM
======================================================================
Original Input Array : [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]

Sorted Array         : [11, 12, 18, 22, 25, 34, 42, 55, 64, 90]
Execution Time       : 0.00001840 seconds (0.0184 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(n log n)
    - Average Case : O(n log n)
    - Worst Case   : O(n log n)
  Space Complexity:
    - Auxiliary Space : O(n) [For temporary merged subarrays]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Recurrence | Time Complexity |
| :--- | :--- | :--- |
| **Best Case** | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| **Average Case** | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |
| **Worst Case** | $T(n) = 2T(n/2) + O(n)$ | $O(n \log n)$ |

- Tree depth is $\log_2 n$, with each level performing $O(n)$ work during merging.

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(n)$ auxiliary buffer storage during the merge phase.

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` captures high-resolution start and finish times for `merge_sort()`:
```python
start_time = time.perf_counter()
sorted_array = merge_sort(sample_data)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
The input array is correctly sorted into `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`.

---

## 14. Important Concepts Used
- **Divide and Conquer**: Recursive problem splitting.
- **Two-Pointer Linear Merging**: Merges two already-sorted arrays in $O(n_1 + n_2)$ time.
- **Guaranteed Log-Linear Performance**: Consistent $O(n \log n)$ across all input distributions.
