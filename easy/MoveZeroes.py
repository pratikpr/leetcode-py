'''
https://leetcode.com/problems/move-zeroes/
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
'''
from typing import List


class MoveZeroes:
    def moveZeroes(self, nums: List[int]) -> None:
        lastnonZero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastnonZero] = nums[i]
                lastnonZero += 1

        for i in range(lastnonZero, len(nums)):
            nums[i] = 0

obj = MoveZeroes()
nums = [0]
print(nums)
obj.moveZeroes(nums)
print(nums)