import time

def insertion_sort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

print("Insertion Sort")

arr = list(map(int, input("Enter numbers separated by space: ").split()))

start = time.perf_counter()

insertion_sort(arr)

end = time.perf_counter()

print("Sorted Array:", arr)
print(f"Execution Time: {(end-start)*1000:.6f} ms")

print("\nTime Complexity")
print("Best Case   : O(n)")
print("Average Case: O(n²)")
print("Worst Case  : O(n²)")
print("Space Complexity: O(1)")