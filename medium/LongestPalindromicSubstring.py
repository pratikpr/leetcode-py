'''
https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.
'''
class LongestPalindromicSubstring:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start, end = 0,0

        for i in range(0, len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCenter(s, i, i+1)
            max_len = max(len1, len2)
            if max_len > end-start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start:end+1]

    def expandAroundCenter(self, s, l, r):
        L, R = l, r
        while L >= 0 and R < len(s) and s[L] == s[R]:
            L -= 1; R += 1
        return R-L-1

obj = LongestPalindromicSubstring()
s = "abbad"
print(obj.longestPalindrome(s))