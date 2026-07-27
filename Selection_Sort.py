import time

def selection_sort(arr):
    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

print("Selection Sort")

arr = list(map(int, input("Enter numbers separated by space: ").split()))

start = time.perf_counter()

selection_sort(arr)

end = time.perf_counter()

print("Sorted Array:", arr)
print(f"Execution Time: {(end-start)*1000:.6f} ms")

print("\nTime Complexity")
print("Best Case   : O(n²)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(1)")