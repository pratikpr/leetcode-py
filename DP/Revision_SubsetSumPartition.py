class Revise_Partition:
	def can_partition(self, nums):
		n = len(nums)
		sum_nums = sum(nums)
		if sum_nums%2 == 1:
			return False
		sum_nums //= 2
		
		dp = [[False for i in range(sum_nums+1)] for j in range(n)]
		
		# only when the required sum is the value, the number is good
		for i in range(sum_nums+1):
			dp[0][i] = (i == nums[0])
			
		# 0 sum can be achieved with an empty set
		for i in range(n):
			dp[i][0] = True
		
		for i in range(1, n):
			for j in range(1, sum_nums+1):
				if dp[i-1][j]:
					dp[i][j] = True
				elif j >= nums[i]:
					dp[i][j] = dp[i-1][j-nums[i]]
					
		return dp[n-1][sum_nums]
	
obj = Revise_Partition()
nums = [1,1,1,5]
print(obj.can_partition(nums))
