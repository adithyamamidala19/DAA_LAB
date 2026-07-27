# Sorting Algorithm Playground

A small command-line tool that lets you pick a sorting algorithm, feed it a list of numbers, and see it sorted — along with the algorithm's time complexity and how long it actually took to run on your machine.

I built this mostly to have a quick reference for comparing sorting algorithms side by side instead of digging through six different scripts.

## What it does

Run the script, pick an algorithm from the menu, and either type in your own numbers or ask it to generate a random list. It sorts the list and prints:

- the input you gave it
- the sorted output
- the algorithm's Big-O time complexity
- the actual execution time, measured with `time.perf_counter()`

## Algorithms included

| # | Algorithm | Time Complexity (worst case) |
|---|-----------|-------------------------------|
| 1 | Bubble Sort | O(n²) |
| 2 | Selection Sort | O(n²) |
| 3 | Insertion Sort | O(n²) |
| 4 | Merge Sort | O(n log n) |
| 5 | Quick Sort | O(n²) worst, O(n log n) average |
| 6 | Heap Sort | O(n log n) |

## Requirements

Just Python 3. No external libraries.

## Running it

```bash
python3 sort_menu.py
```

You'll get a menu like this:

```
Pick an algorithm:
  1. Bubble Sort  (O(n^2))
  2. Selection Sort  (O(n^2))
  3. Insertion Sort  (O(n^2))
  4. Merge Sort  (O(n log n))
  5. Quick Sort  (O(n^2) worst, O(n log n) average)
  6. Heap Sort  (O(n log n))
  0. Quit
```

Pick a number, then choose whether to type your own numbers or have it generate a random list for you. It'll print the sorted result plus the timing info.

## Example

```
Your choice: 4

How do you want to provide the numbers?
  1. Type them in myself
  2. Generate a random list
Choice: 1
Enter numbers separated by spaces (e.g. 5 3 8 1): 5 3 8 1 9 2

--- Merge Sort ---
Input:            [5, 3, 8, 1, 9, 2]
Sorted output:    [1, 2, 3, 5, 8, 9]
Time complexity:  O(n log n)
Execution time:   0.000043 seconds
```

## A note on the timing numbers

For small lists, execution time mostly measures Python overhead, not the algorithm itself — the differences between algorithms only really show up once you're sorting a few thousand elements or more. Try the random-list option with a size of 5000+ to see O(n²) algorithms fall noticeably behind O(n log n) ones.

## Why I made this

Time complexity numbers on their own can feel abstract. Being able to type in a list and watch bubble sort take visibly longer than merge sort on the same input makes it click faster than reading a table.

## License

Do whatever you want with it.
