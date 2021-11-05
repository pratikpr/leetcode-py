from typing import List
'''
https://leetcode.com/problems/subarray-sum-equals-k
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.
'''

class SubarraySumK:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        for start in range(len(nums)):
            sum = 0
            for end in range(start, len(nums)):
                sum += nums[end]
                if sum == k:
                    count += 1

        return count

    def subArraySumMap(self, nums, k):
        count, sum = 0,0
        sum_map = {}
        sum_map[0] = 1

        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in sum_map:
                count += sum_map[sum-k]
            if sum in sum_map:
                sum_map[sum] += 1
            else:
                sum_map[sum] = 1

        return count

obj = SubarraySumK()
nums = [1,2,3]
k = 4
print(obj.subarraySum(nums, k))
print(obj.subArraySumMap(nums, k))