from typing import List


class ThreeSum:
    '''
    https://leetcode.com/problems/3sum
   Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
   such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r, sum = i+1, len(nums)-1, -nums[i]
            while l < r:
                if nums[l] + nums[r] == sum:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
                elif nums[l] + nums[r] > sum:
                    r -= 1
                else:
                    l += 1

        return res

obj = ThreeSum()
nums = [-1,0,1,2,-1,-4]
print(obj.threeSum(nums))