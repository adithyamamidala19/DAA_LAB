"""
================================================================================
PRACTICAL 03: MAX-HEAP SORT ALGORITHM
================================================================================
Title: Implementation of Max-Heap Sort Algorithm
Algorithm Implemented:
  - Max-Heap Sort (from scratch without built-in libraries)

Description:
  This program implements the Max-Heap Sort algorithm from scratch.
  It transforms an input array into a Max-Heap structure where every parent
  node is greater than or equal to its child nodes. It then iteratively removes
  the maximum element (root) and places it at the end of the array, reheapifying
  the remaining elements until the entire array is sorted in ascending order.
================================================================================
"""

import time
import copy


def heapify(arr, n, i):
    """
    Maintains the max-heap property for a subtree rooted at index `i`.
    
    Parameters:
      arr (list): The array representing the binary heap.
      n (int): Size of the heap.
      i (int): Root index of the subtree to heapify.
      
    Logic:
      - Left child is at index 2*i + 1
      - Right child is at index 2*i + 2
      - Finds the largest among root, left child, and right child.
      - If root is not the largest, swaps root with largest and recursively
        heapifies the affected subtree.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater than current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)


def build_max_heap(arr):
    """
    Builds a Max-Heap from an unordered array.
    
    Logic:
      Starts from the last non-leaf node (index n // 2 - 1) and calls
      heapify for each node down to index 0.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


def max_heap_sort(arr):
    """
    Performs Heap Sort in ascending order using a Max-Heap.
    
    Steps:
      1. Build a Max Heap from input data.
      2. At this point, the largest item is stored at the root (index 0).
         Swap it with the last item of the heap.
      3. Reduce the heap size by 1.
      4. Heapify the root of the tree.
      5. Repeat steps 2-4 until heap size becomes 1.
    """
    a = copy.deepcopy(arr)
    n = len(a)

    # Step 1: Build max heap
    build_max_heap(a)

    # Step 2: One by one extract elements from heap
    for i in range(n - 1, 0, -1):
        # Move current root (maximum element) to end
        a[0], a[i] = a[i], a[0]
        # Call heapify on the reduced heap
        heapify(a, i, 0)

    return a


def main():
    print("=" * 70)
    print("PRACTICAL 03: MAX-HEAP SORT ALGORITHM")
    print("=" * 70)

    sample_array = [12, 11, 13, 5, 6, 7, 33, 1, 45, 23, 19]
    print(f"Original Array : {sample_array}")

    # Build heap demonstration
    demo_heap = copy.deepcopy(sample_array)
    build_max_heap(demo_heap)
    print(f"Max-Heap Array : {demo_heap}\n")

    # Measure execution time
    start_time = time.perf_counter()
    sorted_array = max_heap_sort(sample_array)
    end_time = time.perf_counter()

    execution_time = end_time - start_time

    print(f"Sorted Array   : {sorted_array}")
    print(f"Execution Time : {execution_time:.8f} seconds ({execution_time * 1000:.4f} ms)\n")

    print("Theoretical Complexity Analysis:")
    print("  Time Complexity:")
    print("    - Building Max-Heap : O(n)")
    print("    - Extracting Max (n times): O(n log n)")
    print("    - Best Case Time    : O(n log n)")
    print("    - Average Case Time : O(n log n)")
    print("    - Worst Case Time   : O(n log n)")
    print("  Space Complexity:")
    print("    - Auxiliary Space   : O(1) (In-place sorting)")
    print("=" * 70)


if __name__ == "__main__":
    main()
