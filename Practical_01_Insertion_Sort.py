"""
================================================================================
PRACTICAL 01: INSERTION SORT ALGORITHM
================================================================================
Practical Number : Practical 01
Topic Name       : Insertion Sort Algorithm
Objective        : To implement Insertion Sort in Python, sort an input array in 
                   ascending order, measure actual execution time using 
                   time.perf_counter(), and analyze its theoretical time and 
                   space complexity.

Algorithm Description:
  Insertion Sort builds the final sorted array one element at a time. It iterates
  through the input elements, removing one element per iteration and finding the
  location it belongs to in the already-sorted sublist, shifting greater elements
  one position to the right.
================================================================================
"""

import time
import copy


def insertion_sort(arr):
    """
    Sorts an array in ascending order using Insertion Sort.
    
    Parameters:
      arr (list): List of numeric elements to be sorted.
      
    Returns:
      list: New sorted list in ascending order.
    """
    a = copy.deepcopy(arr)
    
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        
        # Move elements of a[0..i-1] that are greater than key to one position ahead
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
            
        a[j + 1] = key
        
    return a


def main():
    print("=" * 70)
    print("PRACTICAL 01: INSERTION SORT ALGORITHM")
    print("=" * 70)

    # Sample input
    sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
    print(f"Original Input Array : {sample_data}\n")

    # Measure execution time
    start_time = time.perf_counter()
    sorted_array = insertion_sort(sample_data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"Sorted Array         : {sorted_array}")
    print(f"Execution Time       : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(n) [When array is already sorted]")
    print("    - Average Case : O(n^2)")
    print("    - Worst Case   : O(n^2) [When array is sorted in reverse order]")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(1) [In-place comparison sort]")
    print("=" * 70)


if __name__ == "__main__":
    main()
