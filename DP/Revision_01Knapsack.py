class Revise01Knapsack:
	def knapsack(self, profits, weights, capacity):
		if capacity == 0 or len(profits) == 0 or len(profits) != len(weights):
			return 0

		dp = [[0 for i in range(capacity+1)] for j in range(len(profits) + 1)]

		for i in range(len(profits) + 1):
			for w in range(capacity + 1):
				if i == 0 or w == 0:
					dp[i][w] = 0
				elif weights[i - 1] <= w:
					dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + profits[i - 1])
				else:
					dp[i][w] = dp[i - 1][w]

		return dp[len(profits)][capacity]

obj = Revise01Knapsack()
weights = [1, 2, 3, 5]
profits = [1, 6, 10, 16]
print(obj.knapsack(profits, weights, 7))
print(obj.knapsack(profits, weights, 6))