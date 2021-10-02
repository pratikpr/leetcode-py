from typing import List

'''
https://leetcode.com/problems/maximum-subarray/
Given an integer array nums, 
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
'''
class MaximumSubarray:
    #TODO: learn and use Kadane's algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [0]*len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]

        for i in range(1, len(nums)):
            if dp[i - 1] > 0:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]
            max_sum = max(max_sum, dp[i])

        return max_sum


obj = MaximumSubarray()
nums = [5, 4, -1, 7, 8]
print(MaximumSubarray.maxSubArray(obj, nums))
