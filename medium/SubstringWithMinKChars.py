'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.
'''

class SubstringWithMinKChars:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if len(s) == 0 or k == 0:
            return 0

        sol = 1
        l, r = 0, 0
        idx_map = {}

        while r < len(s):
            idx_map[s[r]] = r
            r += 1

            if len(idx_map) > k:
                del_idx = min(idx_map.values())
                del idx_map[s[del_idx]]
                l = del_idx + 1

            sol = max(sol, r-l)

        return sol


obj = SubstringWithMinKChars()
s = "eceba"; k = 2
print(obj.lengthOfLongestSubstringKDistinct(s, k))