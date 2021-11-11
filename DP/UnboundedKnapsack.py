'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack that has a capacity ‘C’.
 The goal is to get the maximum profit from the items in the knapsack. The only difference between
 the 0/1 Knapsack problem and this problem is that we are allowed to use an unlimited quantity of an item.
'''

def solve_knapsack(profits, weights, capacity):
    n = len(profits)
    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0

    dp = [[-1 for _ in range(capacity+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for j in range(capacity+1):
            p1, p2 = 0, 0
            if weights[i] <= j:
                p1 = profits[i] + dp[i][j-weights[i]]
            if i > 0:
                p2 = dp[i-1][j]
            dp[i][j] = max(p1,p2)
    return dp[n-1][capacity]

print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 8))
print(solve_knapsack([15, 50, 60, 90], [1, 3, 4, 5], 6))