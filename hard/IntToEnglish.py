'''
https://leetcode.com/problems/integer-to-english-words/submissions/
Convert a non-negative integer num to its English words representation.
'''
class IntegerToEnglish:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        english = {1:"One ", 2:"Two ", 3:"Three ", 4:"Four ", 5:"Five ", 6:"Six ", 7:"Seven ", 8:"Eight ", 9:"Nine ", 10:"Ten ",
                   11:"Eleven ", 12:"Twelve ", 13:"Thirteen ", 14:"Fourteen ", 15:"Fifteen ",16:"Sixteen ",17:"Seventeen ", 18:"Eighteen ", 19: "Nineteen "}
        positional = {2:"Twenty ",3:"Thirty ",4:"Forty ",5:"Fifty ",6:"Sixty ",7:"Seventy ",8:"Eighty ",9:"Ninety "}
        ns = {5: "Quadrillion ", 4: "Trillion", 3:"Billion ", 2:"Million ", 1: "Thousand ", 0: ""}

        n = num
        number = []
        while n > 0:
            number.insert(0, n%1000)
            n = n // 1000

        sol = ""
        for j in (range(len(number))):
            i = number[j]
            if i == 0:
                continue
            if len(str(i)) == 3 and str(i)[0] != '0':
                sol += english[int(str(i//100))] + "Hundred "
            i %= 100
            if int(str(i)[:]) in english.keys():
                sol += english[int(str(i)[:])]
                sol += ns[len(number)-j-1]
                continue
            if int(str(i)[0]) != 0:
                sol += positional[int(str(i)[0])]
            i %= 10
            if str(i)[0] != '0':
                sol = sol + english[i]
            sol += ns[len(number)-j-1]

        return sol.strip()

obj = IntegerToEnglish()
num = 1234567
print(obj.numberToWords(num))