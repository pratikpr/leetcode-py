class Permutation:
	def permute(self, nums):
		def backtrack(first=0):
			if first == n:
				output.append(nums[:])
			
			for i in range(first, n):
				nums[i], nums[first] = nums[first], nums[i]
				backtrack(first + 1)
				nums[i], nums[first] = nums[first], nums[i]
		
		n = len(nums)
		output = []
		backtrack()
		return output


obj = Permutation()
nums = [1, 2, 3]
print(obj.permute(nums))
