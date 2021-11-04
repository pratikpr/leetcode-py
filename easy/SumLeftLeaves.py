from typing import Optional
'''
https://leetcode.com/problems/sum-of-left-leaves/
Given the root of a binary tree, return the sum of all left leaves
'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SumOfLeftLeaves:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sum = 0
        queue = []

        queue.append(root)

        while queue:
            node = queue.pop(0)
            if node.left:
                queue.append(node.left)
                if not node.left.left and not node.left.right:
                    sum += node.left.val
            if node.right:
                queue.append(node.right)
        return sum

obj = SumOfLeftLeaves()
root = TreeNode(10)
root.left = TreeNode(8)
root.right = TreeNode(8)
root.left.left = TreeNode(6)
root.left.right = TreeNode(9)
root.right.left = TreeNode(9)
root.right.right = TreeNode(16)
print(obj.sumOfLeftLeaves(root))