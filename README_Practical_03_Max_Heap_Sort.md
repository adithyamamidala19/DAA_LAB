# Practical 03: Max-Heap Sort Algorithm

## 1. Practical Number
**Practical 03**

## 2. Practical Name
**Implementation of Max-Heap Sort Algorithm**

## 3. Objective
To implement the Max-Heap Sort algorithm from scratch in Python, demonstrate binary heap construction (Heapify and Build-Heap), perform sorting in ascending order, measure execution runtime, and analyze time/space complexity.

---

## 4. Problem Statement
Given an unsorted list of elements, build a complete binary tree satisfying the Max-Heap property ($A[\text{parent}] \ge A[\text{child}]$) and sort the list in non-decreasing order without using any built-in sorting libraries.

---

## 5. Algorithm Explanation

### A. Binary Heap Representation
An array `arr` can represent a complete binary tree where for node at index `i`:
- **Left child**: `2 * i + 1`
- **Right child**: `2 * i + 2`
- **Parent**: `(i - 1) // 2`

### B. Max-Heap Property
For every node $i$ (other than root):
$$\text{arr}[\text{parent}(i)] \ge \text{arr}[i]$$
Hence, the root at index 0 always holds the maximum element.

### C. Heapify Operation
- Given an array where left and right subtrees of root `i` are valid max heaps, `heapify` bubbles down the element at `i` to its proper location.
- Takes $O(\log n)$ time.

### D. Build Max Heap
- Starts from the last non-leaf node $\lfloor n/2 \rfloor - 1$ down to root $0$, calling `heapify` on each node.
- Runs in $O(n)$ time.

### E. Sorting Procedure
1. Build Max Heap from input array ($O(n)$).
2. Swap root (largest element, `arr[0]`) with the last element (`arr[i]`).
3. Reduce heap size by 1.
4. Call `heapify(arr, i, 0)` on the root to restore the max-heap property.
5. Repeat steps 2–4 until the heap size reduces to 1.

---

## 6. Step-by-Step Working

1. **Input**: `[12, 11, 13, 5, 6, 7, 33, 1, 45, 23, 19]`
2. **Build Max-Heap**:
   - Starting from non-leaf nodes, heapify transforms the array into a valid Max Heap: `[45, 23, 33, 12, 19, 7, 13, 1, 5, 11, 6]`.
3. **Extraction & Re-heapification**:
   - Swap `45` with `6`, heapify root `6` $\to$ heap size becomes 10.
   - Swap `33` with `11`, heapify root `11` $\to$ heap size becomes 9.
   - Continue until array is completely sorted in ascending order.
4. **Timing & Metrics**: Execution time is measured using `time.perf_counter()`.

---

## 7. Python Implementation File Name
`Practical_03_Max_Heap_Sort.py`

---

## 8. Sample Input
```python
sample_array = [12, 11, 13, 5, 6, 7, 33, 1, 45, 23, 19]
```

---

## 9. Sample Output
```
======================================================================
PRACTICAL 03: MAX-HEAP SORT ALGORITHM
======================================================================
Original Array : [12, 11, 13, 5, 6, 7, 33, 1, 45, 23, 19]
Max-Heap Array : [45, 23, 33, 12, 19, 7, 13, 1, 5, 11, 6]

Sorted Array   : [1, 5, 6, 7, 11, 12, 13, 19, 23, 33, 45]
Execution Time : 0.00001850 seconds (0.0185 ms)

Theoretical Complexity Analysis:
  Time Complexity:
    - Building Max-Heap : O(n)
    - Extracting Max (n times): O(n log n)
    - Best Case Time    : O(n log n)
    - Average Case Time : O(n log n)
    - Worst Case Time   : O(n log n)
  Space Complexity:
    - Auxiliary Space   : O(1) (In-place sorting)
======================================================================
```

---

## 10. Time Complexity Analysis

| Phase | Time Complexity |
| :--- | :--- |
| **`heapify` on subtree of height $h$** | $O(h) = O(\log n)$ |
| **`build_max_heap`** | $O(n)$ (Sum of series $\sum \frac{h}{2^h}$) |
| **Sorting Phase ($n-1$ extractions)** | $(n-1) \times O(\log n) = O(n \log n)$ |
| **Overall Best Case** | $O(n \log n)$ |
| **Overall Average Case** | $O(n \log n)$ |
| **Overall Worst Case** | $O(n \log n)$ |

---

## 11. Space Complexity Analysis
- **Auxiliary Space**: $O(1)$ (In-place sorting; modifies array elements directly without additional data structures).

---

## 12. Explanation of Execution-Time Measurement
`time.perf_counter()` is used to measure the elapsed time of `max_heap_sort()`:
```python
start_time = time.perf_counter()
sorted_array = max_heap_sort(sample_array)
end_time = time.perf_counter()
execution_time = end_time - start_time
```

---

## 13. Expected Result
The unsorted array `[12, 11, 13, 5, 6, 7, 33, 1, 45, 23, 19]` is correctly sorted into `[1, 5, 6, 7, 11, 12, 13, 19, 23, 33, 45]`.

---

## 14. Important Concepts Used
- **Complete Binary Tree**: A binary tree in which every level is completely filled except possibly the last level, filled from left to right.
- **Max-Heap Invariant**: Parent value is $\ge$ child values.
- **Sift-Down / Sink Operation**: Restores heap structure efficiently.
