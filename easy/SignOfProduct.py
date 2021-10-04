from typing import List

'''
https://leetcode.com/problems/sign-of-the-product-of-an-array/
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
'''
class SignOfProduct:
    def arraySign(self, nums: List[int]) -> int:
        neg = 1
        for i in nums:
            if i < 0:
                neg *= -1
            elif i == 0:
                neg = 0

        return neg

obj = SignOfProduct()
nums = [-1,-2,-4,3,2,1]
print(SignOfProduct.arraySign(obj, nums))
