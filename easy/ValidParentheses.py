'''
https://leetcode.com/problems/valid-parentheses/
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
'''
class ValidParentheses:
    def isValid(self, s: str) -> bool:
        stk = []

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stk.append(i)
                continue
            if not stk:
                return False
            c = stk.pop()
            if i == ")":
                if c is not None and c != "(":
                    return False
            elif i == "}":
                if c is not None and c != "{":
                    return False
            elif i == "]":
                if c is not None and c != "[":
                    return False
        return not stk

obj = ValidParentheses()
s = "(]"
print(obj.isValid(s))
