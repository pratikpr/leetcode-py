from typing import List
'''
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
that the number could represent. Return the answer in any order.
'''

def letterCombinations(digits: str) -> List[str]:
    # If the input is empty, immediately return an empty answer array
    if len(digits) == 0:
        return []

    # Map all the digits to their corresponding letters
    letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    def findCombinations(idx, path):
        if len(path) == len(digits):
            combinations.append("".join(path))
            return

        possible_letters = letters[digits[idx]]

        for letter in possible_letters:
            path.append(letter)
            findCombinations(idx+1, path)
            path.pop()



    # Initiate backtracking with an empty path and starting index of 0
    combinations = []
    findCombinations(0, [])
    return combinations

digits = "23"
print(letterCombinations(digits))