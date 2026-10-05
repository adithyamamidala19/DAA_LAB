# Practical 01: Bubble Sort Algorithm

## 1. Practical Number
**Practical 01**

## 2. Practical Name / Topic Name
**Bubble Sort Algorithm (Implementation and Time Analysis)**

## 3. Objective
To implement Bubble Sort in Python with an early stopping optimization flag, sort an unsorted numeric array in ascending order, measure the actual execution time using `time.perf_counter()`, and analyze its theoretical time and space complexity.

---

## 4. Problem Statement
Given an unordered list of $n$ numbers, rearrange the elements in non-decreasing order using adjacent element comparisons and swaps.

---

## 5. Algorithm Explanation

### Core Logic
Bubble Sort is a comparison-based sorting algorithm:
1. Iteratively passes through the array from index $0$ to $n-i-1$.
2. In each pass, compares adjacent elements $A[j]$ and $A[j+1]$.
3. If $A[j] > A[j+1]$, swaps them so the larger element bubbles up toward the end.
4. An optimization flag `swapped` tracks whether any swap occurred during the pass. If no swap occurs, the array is already sorted, terminating the algorithm early in $O(n)$ time.

---

## 6. Step-by-Step Working

1. **Input**: `[64, 34, 25, 12, 22, 11, 90, 42, 18, 55]`
2. **Pass 1**: Compares adjacent pairs, bubbling maximum element `90` to the last index.
3. **Pass 2 to $n-1$**: Continues placing the next largest elements in their correct sorted suffix positions.
4. **Early Termination**: Stops if a full pass completes without any swaps.
5. **Output**: Returns the fully sorted array.

---

## 7. Python Implementation File Name
`Practical_01_Bubble_Sort.py`

---

## 8. Sample Input
```python
sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 01: BUBBLE SORT ALGORITHM
======================================================================
Original Input Array : [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]

Sorted Array         : [11, 12, 18, 22, 25, 34, 42, 55, 64, 90]
Execution Time       : 0.00001520 seconds (0.0152 ms)

Complexity Analysis:
  Time Complexity:
    - Best Case    : O(n) [When input array is already sorted]
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
| **Best Case** | Array is already sorted (terminates after 1 pass) | $O(n)$ |
| **Average Case** | Array elements are in arbitrary order | $O(n^2)$ |
| **Worst Case** | Array is sorted in reverse order | $O(n^2)$ |

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(1)$ (In-place sort modifying array without extra buffer memory).

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` captures high-precision timestamps before and after invoking `bubble_sort()`:
```python
start_time = time.perf_counter()
sorted_array = bubble_sort(sample_data)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
The input array is correctly sorted in ascending order: `[11, 12, 18, 22, 25, 34, 42, 55, 64, 90]`.

---

## 14. Important Concepts Used
- **Adjacent Comparisons & Swapping**: Pushing largest unsorted element to the end.
- **Adaptive Optimization**: `swapped` flag enables $O(n)$ best-case detection.
- **Stable Sorting**: Preserves original relative order of equal elements.
