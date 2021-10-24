from typing import List

'''
https://leetcode.com/problems/group-anagrams/
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.
'''
class GroupAnagrams:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ss = "bats"
        s1 = "".join(sorted(ss))
        print(s1)
        anagrams = {}
        res = []

        for word in strs:
            s = "".join(sorted(word))
            if s not in anagrams.keys():
                anagrams[s] = []
            anagrams[s].append(word)

        for k in anagrams.keys():
            res.append(anagrams[k])
        return res

obj = GroupAnagrams()
strs = ["eat","tea","tan","ate","nat","bat"]
print(obj.groupAnagrams(strs))