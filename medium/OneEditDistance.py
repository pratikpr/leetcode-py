'''
https://leetcode.com/problems/one-edit-distance/
Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.
'''
class OneEditDistance:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ns, nt = len(s), len(t)

        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):
            if s[i] != t[i]:
                if ns == nt:
                    return s[i+1:] == t[i+1:]
                else:
                    return s[i:] == t[i+1:]

        return ns+1 == nt

obj = OneEditDistance()
s = ""
t = "a"
print(obj.isOneEditDistance(s, t))