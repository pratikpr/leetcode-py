'''
https://leetcode.com/problems/next-permutation/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.
'''
from typing import List


class NextPermutation:
    def nextPermutation(self, nums: List[int]) -> None:
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        if i >= 0:
            j = len(nums)-1
            while nums[j] <= nums[i]:
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i+1)


    def swap(self, nums, i, j):
        t = nums[i]
        nums[i] = nums[j]
        nums[j] = t

    def reverse(self, nums, i):
        j = len(nums)-1
        while i < j:
            self.swap(nums, i, j)
            i+=1
            j-=1

obj = NextPermutation()
nums = [1,2,1,7,5,3]
print("Before: ", nums)
obj.nextPermutation(nums)
print("After", nums)