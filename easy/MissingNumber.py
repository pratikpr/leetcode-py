from typing import List


class MissingNumber:
    def missingNumber(self, nums: List[int]) -> int:
        sigma_n = 0
        for i in range(1, len(nums)+1):
            sigma_n += i
        sum = 0
        for i in nums:
            if i != 0:
                sum += i

        return sigma_n-sum

obj = MissingNumber()
nums = [9,6,4,2,3,5,7,0,1]
print(obj.missingNumber(nums))