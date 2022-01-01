class ReviseStaircase:
	def countWays(self, n):
		dp = [0 for i in range(n+1)]
		dp[1], dp[2], dp[3] = 1, 1, 1

		for i in range(2, n+1):
			dp[i] += dp[i-1] + dp[i-2]
			if i >= 3:
				dp[i] += dp[i-3]

		return dp[n]

obj = ReviseStaircase()
n = 27
print(obj.countWays(n))