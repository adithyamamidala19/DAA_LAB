"""
================================================================================
PRACTICAL 07: COIN CHANGE / MAKING CHANGE PROBLEM USING DYNAMIC PROGRAMMING
================================================================================
Title: Implementation of Making Change Problem using Dynamic Programming
Algorithm:
  - Bottom-Up Tabulation (Minimum Coins Problem)

Description:
  Given a set of coin denominations and a target amount of money, this program
  determines the minimum number of coins needed to make up that exact amount.
  If that amount of money cannot be made by any combination of the coins, it
  identifies that the change is impossible. It also reconstructs the exact
  coins used in the optimal combination.
================================================================================
"""

import time


def min_coins_change(coins, amount):
    """
    Finds the minimum number of coins needed to make change for `amount`.
    
    Parameters:
      coins (list): List of available coin denominations.
      amount (int): Target monetary amount.
      
    Returns:
      tuple: (min_coins, coins_used_list)
        min_coins: Minimum number of coins or -1 if impossible.
        coins_used_list: List of coin denominations used in the optimal solution.
    """
    # dp[i] will store the minimum coins needed for amount i
    # Initialize with infinity (represented as amount + 1)
    dp = [amount + 1] * (amount + 1)
    # parent[i] will track which coin was added to reach amount i
    parent = [-1] * (amount + 1)

    # Base case: 0 coins needed to make amount 0
    dp[0] = 0

    # Build up the table from amount 1 to target amount
    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a:
                if dp[a - coin] + 1 < dp[a]:
                    dp[a] = dp[a - coin] + 1
                    parent[a] = coin

    if dp[amount] > amount:
        return -1, [], dp

    # Reconstruct the coins used
    coins_used = []
    curr = amount
    while curr > 0:
        c = parent[curr]
        coins_used.append(c)
        curr -= c

    return dp[amount], coins_used, dp


def main():
    print("=" * 70)
    print("PRACTICAL 07: COIN CHANGE / MAKING CHANGE (DYNAMIC PROGRAMMING)")
    print("=" * 70)

    # --------------------------------------------------------------------------
    # Case 1: Standard Solvable Case
    # --------------------------------------------------------------------------
    coins1 = [1, 2, 5, 10, 20, 50]
    target1 = 43
    print(f"Coin Denominations Available : {coins1}")
    print(f"Target Amount                : {target1}")

    start_time = time.perf_counter()
    min_count1, used1, dp_table1 = min_coins_change(coins1, target1)
    end_time = time.perf_counter()
    exec_time1 = end_time - start_time

    print("\n[Case 1: Standard Test]")
    if min_count1 != -1:
        print(f"  Minimum Coins Required : {min_count1}")
        print(f"  Coins Chosen           : {used1} (Sum = {sum(used1)})")
    else:
        print("  Change cannot be formed with the given coin denominations.")
    print(f"  Execution Time         : {exec_time1:.8f} seconds ({exec_time1 * 1000:.4f} ms)")

    # --------------------------------------------------------------------------
    # Case 2: Custom Denominations Test (Where greedy fails, DP succeeds)
    # --------------------------------------------------------------------------
    coins2 = [1, 5, 6, 8]
    target2 = 11
    print(f"\n[Case 2: Denominations where Greedy is Suboptimal]")
    print(f"  Coin Denominations Available : {coins2}")
    print(f"  Target Amount                : {target2}")
    
    start_time2 = time.perf_counter()
    min_count2, used2, _ = min_coins_change(coins2, target2)
    end_time2 = time.perf_counter()
    exec_time2 = end_time2 - start_time2

    print(f"  Minimum Coins Required : {min_count2} (e.g., 5 + 6 = 11 using 2 coins)")
    print(f"  Coins Chosen           : {used2}")
    print(f"  Execution Time         : {exec_time2:.8f} seconds ({exec_time2 * 1000:.4f} ms)")

    # --------------------------------------------------------------------------
    # Case 3: Impossible Change Test
    # --------------------------------------------------------------------------
    coins3 = [2, 4, 6]
    target3 = 7
    print(f"\n[Case 3: Impossible Change Test]")
    print(f"  Coin Denominations Available : {coins3}")
    print(f"  Target Amount                : {target3}")

    start_time3 = time.perf_counter()
    min_count3, used3, _ = min_coins_change(coins3, target3)
    end_time3 = time.perf_counter()
    exec_time3 = end_time3 - start_time3

    if min_count3 == -1:
        print("  Result                 : Change is IMPOSSIBLE (No valid combination exists).")
    else:
        print(f"  Result                 : {min_count3} coins")
    print(f"  Execution Time         : {exec_time3:.8f} seconds ({exec_time3 * 1000:.4f} ms)")

    print("\n" + "=" * 70)
    print("Complexity Analysis:")
    print("  Time Complexity:")
    print("    - O(n * Amount), where 'n' is number of coin denominations and 'Amount' is target.")
    print("  Space Complexity:")
    print("    - O(Amount) auxiliary space for the DP array.")
    print("=" * 70)


if __name__ == "__main__":
    main()
