'''
Given an infinite supply of ‘n’ coin denominations and a total money amount,
we are asked to find the total number of distinct ways to make up that amount.
'''
def count_change(denominations, total):
    n = len(denominations)
    dp = [[0 for _ in range(total+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 1

    for i in range(n):
        for j in range(total+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= denominations[i]:
                dp[i][j] += dp[i][j-denominations[i]]

    return dp[n-1][total]

print(count_change([1, 2, 3], 5))