from typing import List
'''
https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
'''

class Solution:
    def wordBreakBFS(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        q = []
        visited = set()

        q.append(0)
        while q:
            start = q.pop(0)
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                if s[start:end] in words:
                    q.append(end)
                    if end == len(s):
                        return True
            visited.add(start)
        return False

    def wordBreakDP(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, (len(s)+1)):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]


obj = Solution()
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
print(obj.wordBreakBFS(s, wordDict))
print(obj.wordBreakDP(s, wordDict))