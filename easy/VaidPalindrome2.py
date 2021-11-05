'''
https://leetcode.com/problems/valid-palindrome-ii/
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
'''
class ValidPalindrome2:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return self.isPalindrome(s, l, r-1) or self.isPalindrome(s, l+1, r)
            l += 1; r -= 1

        return True

    def isPalindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

obj = ValidPalindrome2()
s = "aba"
print(obj.validPalindrome(s))