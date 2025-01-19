import random

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)
print(f"Random number: {random_number}")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)  # Random number: 42 (example)


# 生成一个动态规划题目和解法的 Python 代码示例
# 动态规划示例：背包问题
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1): 
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]

# 示例
weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
capacity = 7
max_value = knapsack(weights, values, capacity)
print(f"最大价值: {max_value}")