'''
Given an infinite supply of ‘n’ coin denominations and a total money amount,
we are asked to find the minimum number of coins needed to make up that amount.
'''
import math


def count_change(denominations, total):
    n = len(denominations)
    dp = [[math.inf for _ in range(total+1)] for _ in range(n)]

    for i in range(n):
        dp[i][0] = 0

    for i in range(n):
        for j in range(1, total+1):
            if i > 0:
                dp[i][j] = dp[i-1][j]
            if j >= denominations[i]:
                if dp[i][j-denominations[i]] != math.inf:
                    dp[i][j] = min(dp[i][j], dp[i][j-denominations[i]]+1)
    return -1 if dp[n-1][total] == math.inf else dp[n-1][total]

print(count_change([1, 2, 3], 5))
print(count_change([1, 2, 3], 11))
print(count_change([1, 2, 3], 7))
print(count_change([3, 5], 7))