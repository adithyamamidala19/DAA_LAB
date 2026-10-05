"""
================================================================================
PRACTICAL 01: MERGE SORT ALGORITHM
================================================================================
Practical Number : Practical 01
Topic Name       : Merge Sort Algorithm
Objective        : To implement Merge Sort in Python using the Divide-and-Conquer
                   technique, sort an input array in ascending order, measure 
                   actual execution time using time.perf_counter(), and analyze 
                   its theoretical time and space complexity.

Algorithm Description:
  Merge Sort recursively splits the array into two equal halves until base case
  subarrays of length <= 1 are reached. It then merges the sorted halves back
  together in linear time by comparing corresponding elements from each half.
================================================================================
"""

import time
import copy


def merge_sort(arr):
    """
    Sorts an array in ascending order using Merge Sort (Divide and Conquer).
    
    Parameters:
      arr (list): List of numeric elements to be sorted.
      
    Returns:
      list: New sorted list in ascending order.
    """
    def _merge_sort_recursive(a):
        # Base case: single element or empty array is already sorted
        if len(a) <= 1:
            return a
        
        mid = len(a) // 2
        # Divide into two halves and recursively sort
        left = _merge_sort_recursive(a[:mid])
        right = _merge_sort_recursive(a[mid:])
        
        # Conquer: Merge two sorted halves
        return _merge(left, right)

    def _merge(left, right):
        merged = []
        i = j = 0
        
        # Compare elements from left and right halves and append smaller element
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                
        # Append remaining elements
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    return _merge_sort_recursive(copy.deepcopy(arr))


def main():
    print("=" * 70)
    print("PRACTICAL 01: MERGE SORT ALGORITHM")
    print("=" * 70)

    # Sample input
    sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
    print(f"Original Input Array : {sample_data}\n")

    # Measure execution time
    start_time = time.perf_counter()
    sorted_array = merge_sort(sample_data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"Sorted Array         : {sorted_array}")
    print(f"Execution Time       : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(n log n)")
    print("    - Average Case : O(n log n)")
    print("    - Worst Case   : O(n log n)")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(n) [For temporary merged subarrays]")
    print("=" * 70)


if __name__ == "__main__":
    main()
