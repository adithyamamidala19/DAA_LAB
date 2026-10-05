"""
================================================================================
PRACTICAL 02: BINARY SEARCH ALGORITHM
================================================================================
Practical Number : Practical 02
Topic Name       : Binary Search Algorithm
Objective        : To implement Binary Search (Iterative and Recursive) in Python, 
                   search for target keys in a sorted dataset, measure actual 
                   execution time using time.perf_counter(), and analyze its 
                   theoretical time and space complexity.

Algorithm Description:
  Binary Search is a Divide-and-Conquer search algorithm for sorted datasets.
  It repeatedly compares the search target with the middle element of the interval.
  If the target is smaller, the search continues in the left half; if greater,
  in the right half. Each step cuts the search space in half.
================================================================================
"""

import time


def binary_search_iterative(arr, target):
    """
    Performs Binary Search iteratively on a sorted array.
    
    Parameters:
      arr (list): Sorted list of numeric elements.
      target: Value to search for.
      
    Returns:
      int: 0-based index of target if found, else -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # Prevents integer overflow
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, low, high, target):
    """
    Performs Binary Search recursively on a sorted array.
    """
    if low > high:
        return -1

    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, low, mid - 1, target)
    else:
        return binary_search_recursive(arr, mid + 1, high, target)


def main():
    print("=" * 70)
    print("PRACTICAL 02: BINARY SEARCH ALGORITHM")
    print("=" * 70)

    # Note: Binary search requires a sorted array
    sorted_dataset = [11, 12, 23, 34, 45, 56, 67, 78, 89, 90]
    target_present = 67
    target_absent = 99

    print(f"Sorted Dataset : {sorted_dataset}\n")

    # --------------------------------------------------------------------------
    # Case 1: Searching for an existing element (Iterative)
    # --------------------------------------------------------------------------
    print(f"[Test Case 1: Searching for target = {target_present} (Present)]")
    start_time_1 = time.perf_counter()
    index_1 = binary_search_iterative(sorted_dataset, target_present)
    end_time_1 = time.perf_counter()
    exec_time_1 = end_time_1 - start_time_1

    if index_1 != -1:
        print(f"  Result         : Target {target_present} found at index {index_1} (Position {index_1 + 1})")
    else:
        print(f"  Result         : Target {target_present} not found")
    print(f"  Execution Time : {exec_time_1:.8f} seconds ({exec_time_1 * 1000:.4f} ms)\n")

    # --------------------------------------------------------------------------
    # Case 2: Searching for a non-existing element (Iterative)
    # --------------------------------------------------------------------------
    print(f"[Test Case 2: Searching for target = {target_absent} (Absent)]")
    start_time_2 = time.perf_counter()
    index_2 = binary_search_iterative(sorted_dataset, target_absent)
    end_time_2 = time.perf_counter()
    exec_time_2 = end_time_2 - start_time_2

    if index_2 != -1:
        print(f"  Result         : Target {target_absent} found at index {index_2}")
    else:
        print(f"  Result         : Target {target_absent} not found in dataset (returned -1)")
    print(f"  Execution Time : {exec_time_2:.8f} seconds ({exec_time_2 * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Best Case    : O(1) [When target is the middle element]")
    print("    - Average Case : O(log n)")
    print("    - Worst Case   : O(log n) [When target is at extreme or absent]")
    print("  Space Complexity:")
    print("    - Iterative Approach : O(1) [Auxiliary space]")
    print("    - Recursive Approach : O(log n) [Call stack frames]")
    print("=" * 70)


if __name__ == "__main__":
    main()
