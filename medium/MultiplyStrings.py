'''
https://leetcode.com/problems/multiply-strings/
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2,
 also represented as a string.
'''
class MultiplyStrings:
    def multiply(self, num1: str, num2: str) -> str:
        sum = 0
        res = 0
        carry = 0
        for i in reversed(range(len(num1))):
            for j in reversed(range(len(num2))):
                ans = int(num1[i]) * int(num2[j]) + carry
                s = ans%10
                sum += s*pow(10, len(num2)-j-1)
                carry = ans//10
            if carry > 0:
                sum +=carry*pow(10, len(num2))
            res += sum * pow(10, len(num1)-i-1)
            carry = 0
            s = 0
            sum = 0
        return str(res)

obj = MultiplyStrings()
num1 = "100"
num2 = "100"
print(obj.multiply(num1, num2))