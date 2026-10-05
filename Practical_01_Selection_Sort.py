"""
================================================================================
PRACTICAL 01: SELECTION SORT ALGORITHM
================================================================================
Practical Number : Practical 01
Topic Name       : Selection Sort Algorithm
Objective        : To implement Selection Sort in Python, sort an input array in 
                   ascending order, measure actual execution time using 
                   time.perf_counter(), and analyze its theoretical time and 
                   space complexity.

Algorithm Description:
  Selection Sort divides the array into a sorted prefix and an unsorted suffix.
  In each iteration, it finds the minimum element in the unsorted suffix and swaps
  it with the first unsorted element, expanding the sorted prefix by one element.
================================================================================
"""

import time
import copy


def selection_sort(arr):
    """
    Sorts an array in ascending order using Selection Sort.
    
    Parameters:
      arr (list): List of numeric elements to be sorted.
      
    Returns:
      list: New sorted list in ascending order.
    """
    a = copy.deepcopy(arr)
    n = len(a)

    for i in range(n):
        min_idx = i
        # Find index of the smallest element in unsorted subarray a[i..n-1]
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        # Swap found minimum element with element at index i
        a[i], a[min_idx] = a[min_idx], a[i]

    return a


def main():
    print("=" * 70)
    print("PRACTICAL 01: SELECTION SORT ALGORITHM")
    print("=" * 70)

    # Sample input
    sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
    print(f"Original Input Array : {sample_data}\n")

    # Measure execution time
    start_time = time.perf_counter()
    sorted_array = selection_sort(sample_data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"Sorted Array         : {sorted_array}")
    print(f"Execution Time       : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(n^2) [Always performs n(n-1)/2 comparisons]")
    print("    - Average Case : O(n^2)")
    print("    - Worst Case   : O(n^2)")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(1) [In-place comparison sort]")
    print("=" * 70)


if __name__ == "__main__":
    main()
