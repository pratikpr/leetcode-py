class RomanToInt:
    '''
    https://leetcode.com/problems/roman-to-integer/
    '''
    def romanToInt(self, s: str) -> int:
        ints = {"M": 1000, "CM": 900, "D": 500, "CD": 400, "C": 100, "XC": 90, "L": 50, "XL": 40, "X": 10,
                "IX": 9, "V": 5, "IV": 4, "I": 1}
        res, idx = 0, 0

        # //MMCXL
        for i in ints.keys():
            while (idx < len(s) and s[idx] == i) or (idx+1 < len(s) and s[idx:idx+2] == i):
                res += ints[i]
                if (idx < len(s) and s[idx] == i):
                    idx += 1
                else:
                    idx += 2

        return res

obj = RomanToInt()
s = "MCMXCIV"
print(obj.romanToInt(s))