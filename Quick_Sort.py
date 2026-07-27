import time

def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr)//2]

    left = [x for x in arr if x < pivot]

    middle = [x for x in arr if x == pivot]

    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

print("Quick Sort")

arr = list(map(int, input("Enter numbers separated by space: ").split()))

start = time.perf_counter()

sorted_arr = quick_sort(arr)

end = time.perf_counter()

print("Sorted Array:", sorted_arr)
print(f"Execution Time: {(end-start)*1000:.6f} ms")

print("\nTime Complexity")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(log n)")