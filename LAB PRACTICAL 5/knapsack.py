def knapsack_dp(wt, val, cap):
    n = len(wt)
    dp = [[0] * (cap + 1) for _ in range(n)]

    # Handle the first row first, considering only the first item
    for w in range(wt[0], cap + 1):
        dp[0][w] = val[0]

    # Fill the remaining rows
    for i in range(1, n):
        for w in range(cap + 1):
            not_pick = dp[i - 1][w] # Do not pick the current item
            pick = 0
            if wt[i] <= w:
                pick = val[i] + dp[i - 1][w - wt[i]] # Pick the current item
            dp[i][w] = max(pick, not_pick)

    return dp[n - 1][cap]


if __name__ == "__main__":
    weights = [1, 2, 4, 5]
    values = [5, 4, 8, 6]
    capacity = 5

    result = knapsack_dp(weights, values, capacity)
    print("Maximum value in Knapsack: {result}")