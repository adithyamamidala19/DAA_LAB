"""
================================================================================
PRACTICAL 01: BUBBLE SORT ALGORITHM
================================================================================
Practical Number : Practical 01
Topic Name       : Bubble Sort Algorithm
Objective        : To implement Bubble Sort in Python, sort an input array in 
                   ascending order, measure actual execution time using 
                   time.perf_counter(), and analyze its theoretical time and 
                   space complexity.

Algorithm Description:
  Bubble Sort repeatedly steps through the list, compares adjacent elements,
  and swaps them if they are in the wrong order. A boolean flag 'swapped' is used 
  to detect if any swap occurred in a pass; if no swaps happen, the array is 
  already sorted and the algorithm terminates early in O(n) best-case time.
================================================================================
"""

import time
import copy


def bubble_sort(arr):
    """
    Sorts an array in ascending order using Bubble Sort with early stopping optimization.
    
    Parameters:
      arr (list): List of numeric elements to be sorted.
      
    Returns:
      list: New sorted list in ascending order.
    """
    a = copy.deepcopy(arr)
    n = len(a)
    
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # Swap adjacent elements
                swapped = True
        # If no two elements were swapped in inner loop, array is sorted
        if not swapped:
            break
            
    return a


def main():
    print("=" * 70)
    print("PRACTICAL 01: BUBBLE SORT ALGORITHM")
    print("=" * 70)

    # Sample input
    sample_data = [64, 34, 25, 12, 22, 11, 90, 42, 18, 55]
    print(f"Original Input Array : {sample_data}\n")

    # Measure execution time
    start_time = time.perf_counter()
    sorted_array = bubble_sort(sample_data)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    # Output results
    print(f"Sorted Array         : {sorted_array}")
    print(f"Execution Time       : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(n) [When input array is already sorted]")
    print("    - Average Case : O(n^2)")
    print("    - Worst Case   : O(n^2) [When array is sorted in reverse order]")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(1) [In-place comparison sort]")
    print("=" * 70)


if __name__ == "__main__":
    main()
