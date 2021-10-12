class Knapsack:
    '''
    Given two integer arrays to represent weights and profits of ‘N’ items, we need to find a subset of these items which
    will give us maximum profit such that their cumulative weight is not more than a given number ‘C’.
     Write a function that returns the maximum profit. Each item can only be selected once, which means either we put an
      item in the knapsack or skip it.
    '''
    def knapsack_bottom_up(self, profits, weights, capacity):

        n = len(profits)

        if capacity <= 0 or n == 0 or len(weights) != n:
            return 0

        dp = [[0 for x in range(capacity+1)] for y in range(n)]
        # print(len(dp[0]))

        # for 0 capacity, profits should be 0
        for i in range(n):
            dp[i][0] = 0

        #if there's only 1 element
        for c in range(capacity+1):
            if c >= weights[0]:
                dp[0][c] = profits[0]

        for i in range(1, n):
            for c in range(1, capacity+1):
                p1, p2 = 0, 0
                if weights[i] <= c:
                    p1 = profits[i] + dp[i-1][c - weights[i]]
                p2 = dp[i-1][c]
                dp[i][c] = max(p1, p2)

        return dp[n-1][capacity]

obj = Knapsack()
profits, weights, capacity = [1, 6, 10, 16], [1, 2, 3, 5], 7
print(obj.knapsack_bottom_up(profits, weights, capacity))