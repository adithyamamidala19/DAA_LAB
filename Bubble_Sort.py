import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

print("Bubble Sort")

arr = list(map(int, input("Enter numbers separated by space: ").split()))

start = time.perf_counter()

bubble_sort(arr)

end = time.perf_counter()

print("Sorted Array:", arr)
print(f"Execution Time: {(end-start)*1000:.6f} ms")

print("\nTime Complexity")
print("Best Case   : O(n)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(1)")