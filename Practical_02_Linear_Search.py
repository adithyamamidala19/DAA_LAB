"""
================================================================================
PRACTICAL 02: LINEAR SEARCH ALGORITHM
================================================================================
Practical Number : Practical 02
Topic Name       : Linear Search Algorithm
Objective        : To implement Linear Search in Python, search for target keys 
                   in an input dataset, measure actual execution time using 
                   time.perf_counter(), and analyze its theoretical time and 
                   space complexity.

Algorithm Description:
  Linear Search (Sequential Search) checks each element of the dataset one by one 
  from the beginning to the end until a match is found or the list is exhausted. 
  It requires no preconditions regarding array ordering.
================================================================================
"""

import time


def linear_search(arr, target):
    """
    Performs Linear Search on an array for a given target.
    
    Parameters:
      arr (list): List of elements to search through.
      target: Value to search for.
      
    Returns:
      int: 0-based index of target if found, else -1.
    """
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


def main():
    print("=" * 70)
    print("PRACTICAL 02: LINEAR SEARCH ALGORITHM")
    print("=" * 70)

    dataset = [45, 12, 89, 34, 67, 23, 78, 90, 11, 56]
    target_present = 67
    target_absent = 99

    print(f"Dataset : {dataset}\n")

    # --------------------------------------------------------------------------
    # Case 1: Searching for an existing element
    # --------------------------------------------------------------------------
    print(f"[Test Case 1: Searching for target = {target_present} (Present)]")
    start_time_1 = time.perf_counter()
    index_1 = linear_search(dataset, target_present)
    end_time_1 = time.perf_counter()
    exec_time_1 = end_time_1 - start_time_1

    if index_1 != -1:
        print(f"  Result         : Target {target_present} found at index {index_1} (Position {index_1 + 1})")
    else:
        print(f"  Result         : Target {target_present} not found")
    print(f"  Execution Time : {exec_time_1:.8f} seconds ({exec_time_1 * 1000:.4f} ms)\n")

    # --------------------------------------------------------------------------
    # Case 2: Searching for a non-existing element
    # --------------------------------------------------------------------------
    print(f"[Test Case 2: Searching for target = {target_absent} (Absent)]")
    start_time_2 = time.perf_counter()
    index_2 = linear_search(dataset, target_absent)
    end_time_2 = time.perf_counter()
    exec_time_2 = end_time_2 - start_time_2

    if index_2 != -1:
        print(f"  Result         : Target {target_absent} found at index {index_2}")
    else:
        print(f"  Result         : Target {target_absent} not found in dataset (returned -1)")
    print(f"  Execution Time : {exec_time_2:.8f} seconds ({exec_time_2 * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(1) [When target is the first element]")
    print("    - Average Case : O(n) [When target is in the middle]")
    print("    - Worst Case   : O(n) [When target is at the end or not present]")
    print("  Space Complexity:")
    print("    - Auxiliary Space : O(1) [Constant memory overhead]")
    print("=" * 70)


if __name__ == "__main__":
    main()
