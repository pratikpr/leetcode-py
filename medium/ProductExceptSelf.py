from typing import List

'''
https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums except nums[i]
'''
class ProductExceptSelf:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1; countZeroes = 0

        for i in nums:
            if i == 0:
                countZeroes += 1
            else:
                product *= i

        for i in nums:
            if i == 0:
                if countZeroes <= 1:
                    res.append(product)
                else:
                    res.append(0)
            else:
                if countZeroes >= 1:
                    res.append(0)
                else:
                    res.append((product//i))

        return res


    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        length = len(nums)
        sol = [0] * length

        sol[0] = 1

        for i in range(1, length):
            sol[i] = sol[i-1] * nums[i-1]

        end = 1

        for i in reversed(range(length)):
            sol[i] *= end
            end *= nums[i]

        return sol

obj = ProductExceptSelf()
nums = [1,2,3,4]
print(obj.productExceptSelf(nums))
print(obj.productExceptSelf2(nums))
