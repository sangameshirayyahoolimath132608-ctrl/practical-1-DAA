def making_change(coins, amount):
    # dp[i] stores the minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins needed for amount 0
    
    # Build the DP table bottom-up
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount] if dp[amount] != float('inf') else -1


# Example Usage
coins = [1, 3, 4]
amount = 6
result = making_change(coins, amount)
print(f"Coins available: {coins}")
print(f"Target amount: {amount}")
print(f"Minimum coins required: {result}")

# ---------------------------------------------------------
# TIME AND SPACE COMPLEXITY:
# Where n = number of coin denominations, m = target amount
# Time Complexity:  O(n * m) - Nested loops over amount and coins
# Space Complexity: O(m)     - DP array of size (amount + 1)
# ---------------------------------------------------------