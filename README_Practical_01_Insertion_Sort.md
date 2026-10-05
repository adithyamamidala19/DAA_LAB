# Practical 01: Insertion Sort Algorithm

## 1. Practical Number
**Practical 01**

## 2. Practical Name / Topic Name
**Insertion Sort Algorithm (Implementation and Time Analysis)**

## 3. Objective
To implement Insertion Sort in Python, sort an unsorted numeric array in ascending order, measure its actual execution time using `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given an array of $n$ numbers, sort the list by incrementally inserting each unsorted element into its proper position within the already-sorted portion of the array.

---

## 5. Algorithm Explanation

### Core Logic
Insertion Sort works analogous to sorting playing cards in hand:
1. The first element $A[0]$ is trivially sorted.
2. For each element $A[i]$ from $i = 1$ to $n-1$:
   - Set `key = A[i]`.
   - Compare `key` with preceding sorted elements $A[j]$ (where $j = i-1, i-2, \dots, 0$).
   - Shift all elements greater than `key` one position to the right.
   - Insert `key` into the empty position $A[j+1]$.

---

## 6. Step-by-Step Working

1. **Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
2. **Step 1 ($i=1$)**: `key = 34` $\to$ shift `64` right $\to$ `[34, 64, 25, ...]`.
3. **Step 2 ($i=2$)**: `key = 25` $\to$ shift `64, 34` right $\to$ `[25, 34, 64, ...]`.
4. **Subsequent Steps**: Inserts remaining keys into their respective sorted positions.
5. **Output**: Returns the fully sorted array.

---

## 7. Python Implementation File Name
`Practical_01_Insertion_Sort.py`

---

## 8. Sample Input
```python
sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 01: INSERTION SORT ALGORITHM
======================================================================
Original Input Array : [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]

Sorted Array         : [11, 12, 18, 22, 25, 34, 42, 55, 64, 90]
Execution Time       : 0.00000950 seconds (0.0095 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(n) [When array is already sorted]
    - Average Case : O(n^2)
    - Worst Case   : O(n^2) [When array is sorted in reverse order]
  Space Complexity:
    - Auxiliary Space : O(1) [In-place comparison sort]
======================================================================
```

---

## 10. Time Complexity Analysis

| Case | Condition | Time Complexity |
| :--- | :--- | :--- |
| **Best Case** | Array is already sorted (only 1 comparison per element) | $O(n)$ |
| **Average Case** | Random array order | $O(n^2)$ |
| **Worst Case** | Reverse sorted array (maximum shifts) | $O(n^2)$ |

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(1)$ (In-place sort).

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` is called around the `insertion_sort()` function:
```python
start_time = time.perf_counter()
sorted_array = insertion_sort(sample_data)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
The input array is correctly sorted into `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`.

---

## 14. Important Concepts Used
- **Incremental Construction**: Sorted subarray grows one element per loop iteration.
- **Adaptive Sorting**: Excellent performance on small or nearly sorted datasets ($O(n)$).
- **Stability**: Equal elements maintain their initial relative order.
