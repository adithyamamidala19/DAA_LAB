"""
================================================================================
PRACTICAL 01: QUICK SORT ALGORITHM
================================================================================
Practical Number : Practical 01
Topic Name       : Quick Sort Algorithm
Objective        : To implement Quick Sort in Python using the Divide-and-Conquer
                   technique, sort an input array in ascending order, measure 
                   actual execution time using time.perf_counter(), and analyze 
                   its theoretical time and space complexity.

Algorithm Description:
  Quick Sort selects an element as pivot and partitions the array such that all 
  elements smaller than the pivot are placed in the left subarray, equal elements 
  in the middle, and greater elements in the right subarray. It then recursively 
  sorts the left and right subarrays.
================================================================================
"""

import time
import copy


def quick_sort(arr):
    """
    Sorts an array in ascending order using Quick Sort (Divide and Conquer).
    
    Parameters:
      arr (list): List of numeric elements to be sorted.
      
    Returns:
      list: New sorted list in ascending order.
    """
    def _quick_sort_recursive(a):
        # Base case: arrays of length 0 or 1 are already sorted
        if len(a) <= 1:
            return a
        
        # Select middle element as pivot
        pivot = a[len(a) // 2]
        
        # Partition step: divide elements around pivot
        left = [x for x in a if x < pivot]
        middle = [x for x in a if x == pivot]
        right = [x for x in a if x > pivot]
        
        # Recursively sort left and right partitions and concatenate
        return _quick_sort_recursive(left) + middle + _quick_sort_recursive(right)

    return _quick_sort_recursive(copy.deepcopy(arr))


def main():
    print("=" * 70)
    print("PRACTICAL 01: QUICK SORT ALGORITHM")
    print("=" * 70)

    # Sample input
    sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
    print(f"Original Input Array : {sample_data}\n")

    # Measure execution time
    start_time = time.perf_counter()
    sorted_array = quick_sort(sample_data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"Sorted Array         : {sorted_array}")
    print(f"Execution Time       : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(n log n) [When pivot partitions array into equal halves]")
    print("    - Average Case : O(n log n)")
    print("    - Worst Case   : O(n^2) [When partition is extremely unbalanced, e.g. 0 and n-1]")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(log n) [Recursion call stack in balanced cases]")
    print("=" * 70)


if __name__ == "__main__":
    main()
