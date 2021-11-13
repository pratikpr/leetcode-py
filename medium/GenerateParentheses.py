'''
https://leetcode.com/problems/generate-parentheses
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
from typing import List


def generateParenthesis(n: int) -> List[str]:
    ans = []

    def generate(S=[], l=0, r=0):
        if len(S) == 2*n:
            ans.append("".join(S))
            return

        if l < n:
            S.append("(")
            generate(S, l+1, r)
            S.pop()

        if r < l:
            S.append(")")
            generate(S, l, r+1)
            S.pop()

    generate()
    return ans

n = 4
ans = generateParenthesis(n)
print(ans, len(ans))