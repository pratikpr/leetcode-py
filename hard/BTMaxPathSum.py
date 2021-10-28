import sys
from typing import Optional

'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them.
 A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

globalMax = -sys.maxsize
class MaxPathSum:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.findSum(root, 0)

    def findSum(self, root: TreeNode, sum: int):
        if not root:
            return sum

        sum += root.val
        l = self.findSum(root.left, sum)
        r = self.findSum(root.right, sum)

        return max(l,r)

    def findMaxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxFullPathSum((root))
        return globalMax

    def maxFullPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxFullPathSum(root.left)
        right = self.maxFullPathSum(root.right)

        max_left_right = max(max(left, right)  +root.val, root.val)

        maximum = max(max_left_right, left+right+root.val)

        global globalMax
        if maximum > globalMax:
            globalMax = maximum

        return max_left_right

obj = MaxPathSum()
root = TreeNode(0)
# root = TreeNode(1)
# root.left = TreeNode(13)
# root.right = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(6)
# root.right.left = TreeNode(5)
# root.right.right = TreeNode(7)
# print(obj.zigzagLevelOrder(root))
print(obj.findMaxPathSum(root))