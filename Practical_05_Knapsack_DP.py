"""
================================================================================
PRACTICAL 05: 0/1 KNAPSACK PROBLEM USING DYNAMIC PROGRAMMING
================================================================================
Title: Implementation of 0/1 Knapsack Problem using Dynamic Programming
Algorithm:
  - Bottom-Up Tabulation Dynamic Programming

Description:
  Given weights and values of n items, this program determines the maximum value
  subset of items that can be packed into a knapsack of capacity W without
  exceeding the capacity. It also traces back through the DP table to identify
  the exact items included in the optimal solution.
================================================================================
"""

import time


def knapsack_01_dp(weights, values, capacity):
    """
    Solves 0/1 Knapsack problem using Bottom-Up Dynamic Programming.
    
    Parameters:
      weights (list): Weight of each item.
      values (list): Value/profit of each item.
      capacity (int): Maximum weight capacity of the knapsack.
      
    Returns:
      tuple: (max_value, selected_items, dp_table)
    """
    n = len(values)
    # Initialize DP table of dimensions (n + 1) x (capacity + 1) with zeros
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table dp[][] in bottom-up manner
    for i in range(1, n + 1):
        item_weight = weights[i - 1]
        item_value = values[i - 1]
        for w in range(1, capacity + 1):
            if item_weight <= w:
                # Max of (including current item, excluding current item)
                dp[i][w] = max(item_value + dp[i - 1][w - item_weight], dp[i - 1][w])
            else:
                # Current item cannot be included
                dp[i][w] = dp[i - 1][w]

    max_value = dp[n][capacity]

    # Backtracking to find which items are included in the optimal knapsack
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        # If the value came from dp[i-1][w], the item was not included
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)  # 0-based index of selected item
            w -= weights[i - 1]

    selected_items.reverse()
    return max_value, selected_items, dp


def print_dp_table(dp, n, capacity):
    """Helper function to print the DP matrix cleanly."""
    print("DP Tabulation Matrix (Rows: Items 0..n, Columns: Capacity 0..W):")
    header = "Item \\ W | " + " ".join(f"{c:4d}" for c in range(capacity + 1))
    print(header)
    print("-" * len(header))
    for i in range(n + 1):
        row_str = f"Item {i:2d}  | " + " ".join(f"{dp[i][c]:4d}" for c in range(capacity + 1))
        print(row_str)


def main():
    print("=" * 70)
    print("PRACTICAL 05: 0/1 KNAPSACK USING DYNAMIC PROGRAMMING")
    print("=" * 70)

    # Sample input problem
    item_names = ["Item 1 (Laptop)", "Item 2 (Camera)", "Item 3 (Watch)", "Item 4 (Headphones)"]
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    print(f"Knapsack Capacity (W) : {capacity}")
    print("Items Available:")
    for i in range(len(weights)):
        print(f"  [{i}] {item_names[i]:<20} -> Weight: {weights[i]}, Value: {values[i]}")
    print()

    # Measure execution time
    start_time = time.perf_counter()
    max_val, chosen_indices, dp_table = knapsack_01_dp(weights, values, capacity)
    end_time = time.perf_counter()

    exec_time = end_time - start_time

    # Display DP Table
    print_dp_table(dp_table, len(weights), capacity)
    print()

    # Display results
    print("-" * 50)
    print("OPTIMAL SOLUTION:")
    print("-" * 50)
    print(f"Maximum Total Value Achieved : {max_val}")
    print("Selected Items:")
    total_weight_used = 0
    for idx in chosen_indices:
        print(f"  - {item_names[idx]} (Weight: {weights[idx]}, Value: {values[idx]})")
        total_weight_used += weights[idx]
    print(f"Total Weight Used            : {total_weight_used} / {capacity}")
    print(f"Execution Time               : {exec_time:.8f} seconds ({exec_time * 1000:.4f} ms)\n")

    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - O(n * W), where 'n' is number of items and 'W' is knapsack capacity.")
    print("  Space Complexity:")
    print("    - O(n * W) auxiliary space for DP table (can be optimized to O(W) with 1D array).")
    print("=" * 70)


if __name__ == "__main__":
    main()
