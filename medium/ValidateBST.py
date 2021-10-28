import math
from typing import Optional

'''
https://leetcode.com/problems/validate-binary-search-tree/
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ValidateBST:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder(root):
            if not root:
                return True
            if not inorder(root.left):
                return False
            if root.val <= self.prev:
                return False
            self.prev = root.val
            return inorder(root.right)

        self.prev = -math.inf
        return inorder(root)

    def isValidBSTBFS(self, root: Optional[TreeNode]) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if root.val <= prev:
                return False

            prev = root.val
            root = root.right
        return True

obj = ValidateBST()
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(12)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(11)
root.right.right = TreeNode(15)
print(obj.isValidBSTBFS(root))