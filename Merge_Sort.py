import time

def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) // 2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

print("Merge Sort")

arr = list(map(int, input("Enter numbers separated by space: ").split()))

start = time.perf_counter()

merge_sort(arr)

end = time.perf_counter()

print("Sorted Array:", arr)
print(f"Execution Time: {(end-start)*1000:.6f} ms")

print("\nTime Complexity")
print("Best Case   : O(n log n)")
print("Average Case: O(n log n)")
print("Worst Case  : O(n log n)")
print("Space Complexity: O(n)")