from typing import List

'''
https://leetcode.com/problems/verifying-an-alien-dictionary/
In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. 
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, 
return true if and only if the given words are sorted lexicographically in this alien language.
'''
class AlienDictionary:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        map = {char: idx for idx, char in enumerate(order)}
        int_words = [[map[char] for char in word] for word in words]
        return all(w1 <= w2 for w1, w2 in zip(int_words, int_words[1:]))


obj = AlienDictionary()
words = ["ubg","kwh"]
order = "qcipyamwvdjtesbghlorufnkzx"
print(obj.isAlienSorted(words, order))