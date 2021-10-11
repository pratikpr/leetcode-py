class IntToRoman:

    '''
    https://leetcode.com/problems/integer-to-roman/
    '''
    def intToRoman(self, num: int) -> str:
        romans = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
                  10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        res, i = "", 0

        for i in romans:
            res += (num // i) * romans[i]
            num %= i

        return res

obj = IntToRoman()
num = 59
print(obj.intToRoman(num))