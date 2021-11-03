'''
https://leetcode.com/problems/valid-palindrome/
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters,
 it reads the same forward and backward. Alphanumeric characters include letters and numbers.
'''
class ValidPalindrome:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s)-1

        while i < j:
            # skip through spaces and punctuations
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True

obj = ValidPalindrome()
s = "race a car"
print(obj.isPalindrome(s))